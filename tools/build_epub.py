#!/usr/bin/env python3
from __future__ import annotations
import html, re, uuid, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"
ASSETS = ROOT / "assets"
DIST = ROOT / "dist"
TITLE = "Красная будка"
AUTHOR = "Аскер Исмайлов"
LANG = "ru"
OUT = DIST / "Krasnaya_budka_Asker_Ismayilov.epub"
COVER = ASSETS / "cover_epub.jpg"

def clean_text(s: str) -> str:
    s = s.replace("\ufeff", "").replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in s.split("\n")]
    return "\n".join(lines).strip() + "\n"

def inline_md(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", s)
    return s

def markdown_body(md: str):
    md = clean_text(md)
    lines = md.splitlines()
    title = None
    out = []
    para = []

    def flush():
        nonlocal para
        if para:
            text = " ".join(x.strip() for x in para).strip()
            if text:
                out.append(f"<p>{inline_md(text)}</p>")
            para = []

    for line in lines:
        if not line.strip():
            flush()
            continue
        if line.startswith("# "):
            flush()
            if title is None:
                title = line[2:].strip()
            else:
                out.append(f"<h2>{inline_md(line[2:].strip())}</h2>")
        elif line.startswith("## "):
            flush()
            out.append(f"<h2>{inline_md(line[3:].strip())}</h2>")
        elif line.strip() in {"***", "* * *", "---"}:
            flush()
            out.append('<div class="scene-break">⁂</div>')
        else:
            para.append(line)
    flush()
    return title or "Глава", "\n".join(out)

def xhtml_doc(title: str, body: str, extra_head: str = "") -> str:
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="{LANG}" lang="{LANG}">
<head>
<meta charset="utf-8"/>
<title>{html.escape(title)}</title>
<link rel="stylesheet" type="text/css" href="styles.css"/>
{extra_head}
</head>
<body>{body}</body>
</html>'''

def main():
    DIST.mkdir(exist_ok=True)
    if not COVER.exists():
        raise SystemExit(f"Cover missing: {COVER}")

    chapter_paths = sorted(CHAPTERS.glob("*.md"))
    if len(chapter_paths) != 40:
        raise SystemExit(f"Expected 40 chapters, found {len(chapter_paths)}")

    chapters = []
    total_words = 0
    for idx, p in enumerate(chapter_paths, 1):
        raw = clean_text(p.read_text(encoding="utf-8"))
        total_words += len(re.findall(r"\S+", raw))
        ch_title, body = markdown_body(raw)
        chapters.append((idx, p.name, ch_title, body))

    book_id = f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, 'asker421/Book:Красная будка:main')}"
    oebps = {}

    css = '''body { font-family: serif; line-height: 1.5; margin: 5%; }
h1 { text-align: center; font-size: 1.7em; margin: 2em 0 2.5em; page-break-after: avoid; }
h2 { font-size: 1.25em; margin-top: 1.5em; }
p { margin: 0; text-indent: 1.25em; text-align: justify; orphans: 2; widows: 2; }
h1 + p, h2 + p, .no-indent { text-indent: 0; }
.scene-break { text-align: center; margin: 1.4em 0; }
.cover { margin: 0; padding: 0; text-align: center; }
.cover img { max-width: 100%; max-height: 100%; }
.title-page { text-align: center; margin-top: 30%; }
.title-page h1 { margin: 0 0 1.5em; font-size: 2em; }
.title-page .author { font-size: 1.15em; }
nav ol { list-style: none; padding-left: 0; }
nav li { margin: .45em 0; }
'''
    oebps["styles.css"] = css.encode("utf-8")

    cover_body = '<div class="cover"><img src="cover.jpg" alt="Обложка книги Красная будка"/></div>'
    oebps["cover.xhtml"] = xhtml_doc("Обложка", cover_body).encode("utf-8")
    title_body = f'<div class="title-page"><h1>{TITLE}</h1><div class="author">{AUTHOR}</div></div>'
    oebps["title.xhtml"] = xhtml_doc(TITLE, title_body).encode("utf-8")

    nav_items = []
    ncx_items = []
    manifest_ch = []
    spine_ch = []
    for idx, _, ch_title, body in chapters:
        fn = f"chapter{idx:02d}.xhtml"
        ch_html = xhtml_doc(ch_title, f"<h1>{inline_md(ch_title)}</h1>\n{body}")
        oebps[fn] = ch_html.encode("utf-8")
        nav_items.append(f'<li><a href="{fn}">{html.escape(ch_title)}</a></li>')
        ncx_items.append(f'''<navPoint id="navPoint-{idx}" playOrder="{idx}">
<navLabel><text>{html.escape(ch_title)}</text></navLabel><content src="{fn}"/></navPoint>''')
        manifest_ch.append(f'<item id="ch{idx}" href="{fn}" media-type="application/xhtml+xml"/>')
        spine_ch.append(f'<itemref idref="ch{idx}"/>')

    nav = xhtml_doc("Оглавление", f'''<nav xmlns:epub="http://www.idpf.org/2007/ops" epub:type="toc" id="toc">
<h1>Оглавление</h1><ol>{''.join(nav_items)}</ol></nav>''')
    oebps["nav.xhtml"] = nav.encode("utf-8")

    ncx = f'''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{book_id}"/><meta name="dtb:depth" content="1"/></head>
<docTitle><text>{TITLE}</text></docTitle><docAuthor><text>{AUTHOR}</text></docAuthor>
<navMap>{''.join(ncx_items)}</navMap></ncx>'''
    oebps["toc.ncx"] = ncx.encode("utf-8")

    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="{LANG}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{book_id}</dc:identifier>
<dc:title>{TITLE}</dc:title>
<dc:creator>{AUTHOR}</dc:creator>
<dc:language>{LANG}</dc:language>
<dc:type>Text</dc:type>
<meta property="dcterms:modified">2026-09-01T00:00:00Z</meta>
<meta name="cover" content="cover-image"/>
</metadata>
<manifest>
<item id="cover-image" href="cover.jpg" media-type="image/jpeg" properties="cover-image"/>
<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>
<item id="title" href="title.xhtml" media-type="application/xhtml+xml"/>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
<item id="css" href="styles.css" media-type="text/css"/>
{''.join(manifest_ch)}
</manifest>
<spine toc="ncx">
<itemref idref="cover" linear="no"/>
<itemref idref="title"/>
{''.join(spine_ch)}
</spine>
<guide><reference type="cover" title="Обложка" href="cover.xhtml"/><reference type="toc" title="Оглавление" href="nav.xhtml"/></guide>
</package>'''
    oebps["content.opf"] = opf.encode("utf-8")

    container_xml = b'''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>'''

    with zipfile.ZipFile(OUT, "w") as z:
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container_xml, compress_type=zipfile.ZIP_DEFLATED)
        z.write(COVER, "OEBPS/cover.jpg", compress_type=zipfile.ZIP_DEFLATED)
        for name, data in oebps.items():
            z.writestr(f"OEBPS/{name}", data, compress_type=zipfile.ZIP_DEFLATED)

    # Structural validation
    with zipfile.ZipFile(OUT, "r") as z:
        names = z.namelist()
        assert names[0] == "mimetype"
        assert z.getinfo("mimetype").compress_type == zipfile.ZIP_STORED
        assert z.read("mimetype") == b"application/epub+zip"
        assert "META-INF/container.xml" in names
        assert "OEBPS/content.opf" in names
        assert "OEBPS/nav.xhtml" in names
        assert "OEBPS/cover.jpg" in names
        for i in range(1, 41):
            assert f"OEBPS/chapter{i:02d}.xhtml" in names
        for n in names:
            if n.endswith((".xhtml", ".opf", ".xml", ".ncx")):
                ET.fromstring(z.read(n))

    report = DIST / "epub_build_report.txt"
    report.write_text(
        f"Title: {TITLE}\nAuthor: {AUTHOR}\nChapters: {len(chapters)}\nWords (whitespace count): {total_words}\nEPUB: {OUT.name}\nValidation: PASS\n",
        encoding="utf-8",
    )
    print(report.read_text(encoding="utf-8"))

if __name__ == "__main__":
    main()
