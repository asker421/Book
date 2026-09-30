#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import re
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / "chapters_v4"
PREFACE = ROOT / "V4_PREFACE.md"
OUT = ROOT / "release_v4_english"
OUT.mkdir(exist_ok=True)

TITLE = "The Red Booth"
AUTHOR = "Asker Ismayilov"
LANG = "en"
YEAR = "2026"
DESCRIPTION = (
    "After stepping into an impossible red telephone booth, Asgar becomes trapped "
    "inside the emergency return sequence of a machine from the far future. Each "
    "new window carries him farther through the history of Earth and the universe, "
    "while the journey to the source turns into a question of what remains human "
    "when the past finally comes within reach."
)

ORDER = [
    "01","02","03","04","04a","05","06","07","08","08a","09","10","11","12",
    "13","14","15","15a","16","17","18","19","20","21","22","22a","23","24",
    "25","26","27","28","29","30"
]

def split_section(text: str):
    text = text.replace("\ufeff", "").replace("\r\n", "\n").replace("\r", "\n").strip()
    lines = text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    if not lines:
        return "Untitled", []
    title = lines[0].lstrip("#").strip()
    lines = lines[1:]
    blocks, buf = [], []
    def flush():
        nonlocal buf
        if buf:
            p = " ".join(x.strip() for x in buf).strip()
            if p:
                blocks.append(("p", p))
            buf = []
    for line in lines:
        t = line.strip()
        if not t:
            flush()
            continue
        if t in {"---", "***", "* * *"}:
            flush()
            blocks.append(("break", ""))
            continue
        if t.startswith("#"):
            flush()
            continue
        buf.append(line)
    flush()
    return title, blocks

def sections():
    if not PREFACE.exists():
        raise SystemExit(f"Missing {PREFACE}")
    out = [("preface", *split_section(PREFACE.read_text(encoding="utf-8")))]
    for key in ORDER:
        p = CH / f"{key}.md"
        if not p.exists():
            raise SystemExit(f"Missing {p}")
        out.append((key, *split_section(p.read_text(encoding="utf-8"))))
    if len(out) != 35:
        raise SystemExit(f"Expected 35 sections including preface, got {len(out)}")
    return out

def esc(s: str) -> str:
    return html.escape(s, quote=False)

def xhtml_doc(title: str, body: str) -> bytes:
    s = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta charset="utf-8"/>
<title>{esc(title)}</title>
<link rel="stylesheet" href="styles.css" type="text/css"/>
</head>
<body>{body}</body>
</html>'''
    return s.encode("utf-8")

def build():
    secs = sections()
    digest = hashlib.sha256()
    digest.update(PREFACE.read_bytes())
    for key in ORDER:
        digest.update((CH / f"{key}.md").read_bytes())
    revision = digest.hexdigest()[:16]
    book_id = f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, 'asker421/Book:v4-english:' + revision)}"
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    files = {}
    files["styles.css"] = b"""
body{font-family:serif;line-height:1.52;margin:5%;color:#111}
h1{text-align:center;font-size:1.55em;margin:2.2em 0 1.8em}
p{margin:0;text-indent:1.25em;text-align:justify;orphans:2;widows:2}
h1+p,.noindent{text-indent:0}
.scene{text-align:center;margin:1.25em 0}
.cover{margin:0;padding:0;text-align:center}
.cover img{max-width:100%;height:auto}
.titlepage{text-align:center;margin-top:30%}
.titlepage h1{font-size:2em;margin-bottom:.5em}
.titlepage p{text-indent:0;text-align:center}
nav ol{list-style:none;padding-left:0}
nav li{margin:.5em 0}
"""

    cover_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="2560" viewBox="0 0 1600 2560">
<rect width="1600" height="2560" fill="#111111"/>
<rect x="520" y="560" width="560" height="1180" rx="12" fill="#a3131b"/>
<rect x="585" y="650" width="430" height="345" fill="#161616" stroke="#d9d9d9" stroke-width="10"/>
<rect x="585" y="1040" width="430" height="560" fill="#161616" stroke="#d9d9d9" stroke-width="10"/>
<line x1="800" y1="650" x2="800" y2="1600" stroke="#d9d9d9" stroke-width="8"/>
<line x1="585" y1="825" x2="1015" y2="825" stroke="#d9d9d9" stroke-width="8"/>
<text x="800" y="300" text-anchor="middle" fill="#f5f5f5" font-family="serif" font-size="112" font-weight="700">THE RED BOOTH</text>
<text x="800" y="2210" text-anchor="middle" fill="#f5f5f5" font-family="sans-serif" font-size="66" letter-spacing="5">ASKER ISMAYILOV</text>
</svg>'''.encode("utf-8")
    files["cover.svg"] = cover_svg
    files["cover.xhtml"] = xhtml_doc("Cover", '<div class="cover"><img src="cover.svg" alt="The Red Booth cover"/></div>')
    files["title.xhtml"] = xhtml_doc(TITLE, f'<div class="titlepage"><h1>{TITLE}</h1><p>{AUTHOR}</p></div>')

    manifest, spine, nav_items, ncx = [], [], [], []
    for i, (key, title, blocks) in enumerate(secs, 1):
        body = [f"<h1>{esc(title)}</h1>"]
        first = True
        for typ, txt in blocks:
            if typ == "break":
                body.append('<div class="scene">⁂</div>')
                first = True
            else:
                cl = ' class="noindent"' if first else ""
                body.append(f"<p{cl}>{esc(txt)}</p>")
                first = False
        fn = f"sec{i:02d}.xhtml"
        files[fn] = xhtml_doc(title, "".join(body))
        manifest.append(f'<item id="s{i}" href="{fn}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="s{i}"/>')
        nav_items.append(f'<li><a href="{fn}">{esc(title)}</a></li>')
        ncx.append(
            f'<navPoint id="n{i}" playOrder="{i}"><navLabel><text>{esc(title)}</text></navLabel>'
            f'<content src="{fn}"/></navPoint>'
        )

    files["nav.xhtml"] = xhtml_doc(
        "Contents",
        '<nav xmlns:epub="http://www.idpf.org/2007/ops" epub:type="toc">'
        '<h1>Contents</h1><ol>' + "".join(nav_items) + "</ol></nav>"
    )
    files["toc.ncx"] = (
        f'<?xml version="1.0" encoding="UTF-8"?>'
        f'<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">'
        f'<head><meta name="dtb:uid" content="{book_id}"/></head>'
        f'<docTitle><text>{TITLE}</text></docTitle><navMap>{"".join(ncx)}</navMap></ncx>'
    ).encode("utf-8")

    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="en">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{book_id}</dc:identifier>
<dc:title>{TITLE}</dc:title>
<dc:creator>{AUTHOR}</dc:creator>
<dc:language>{LANG}</dc:language>
<dc:publisher>{AUTHOR}</dc:publisher>
<dc:description>{esc(DESCRIPTION)}</dc:description>
<dc:subject>Science Fiction</dc:subject>
<dc:subject>Hard SF</dc:subject>
<dc:subject>Time Travel</dc:subject>
<dc:subject>Time Paradoxes</dc:subject>
<dc:date>{YEAR}</dc:date>
<dc:source>v4-english {revision}</dc:source>
<meta property="dcterms:modified">{modified}</meta>
<meta name="cover" content="cover-image"/>
</metadata>
<manifest>
<item id="cover-image" href="cover.svg" media-type="image/svg+xml" properties="cover-image"/>
<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>
<item id="title" href="title.xhtml" media-type="application/xhtml+xml"/>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
<item id="css" href="styles.css" media-type="text/css"/>
{''.join(manifest)}
</manifest>
<spine toc="ncx">
<itemref idref="cover" linear="no"/>
<itemref idref="title"/>
{''.join(spine)}
</spine>
</package>'''
    files["content.opf"] = opf.encode("utf-8")

    container = b'''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>'''

    out = OUT / "The_Red_Booth_Asker_Ismayilov_V4_English.epub"
    with zipfile.ZipFile(out, "w") as z:
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
        for name, data in files.items():
            z.writestr("OEBPS/" + name, data, compress_type=zipfile.ZIP_DEFLATED)

    with zipfile.ZipFile(out) as z:
        if z.namelist()[0] != "mimetype":
            raise SystemExit("mimetype is not first")
        if z.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            raise SystemExit("mimetype is compressed")
        for name in z.namelist():
            if name.endswith((".xhtml", ".opf", ".xml", ".ncx", ".svg")):
                ET.fromstring(z.read(name))
        expected = {"OEBPS/" + f"sec{i:02d}.xhtml" for i in range(1, 36)}
        if not expected.issubset(set(z.namelist())):
            raise SystemExit("Missing literary sections")

    print(out)
    print(f"sections={len(secs)} revision={revision} size={out.stat().st_size}")

if __name__ == "__main__":
    build()
