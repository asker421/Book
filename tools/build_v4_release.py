#!/usr/bin/env python3
from __future__ import annotations
import base64, hashlib, html, io, json, math, os, re, textwrap, uuid, zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from docx import Document
from docx.shared import Mm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / "chapters_v4"
PREFACE = ROOT / "V4_PREFACE.md"
OUT = ROOT / "release_v4"
OUT.mkdir(exist_ok=True)

TITLE = "Красная будка"
AUTHOR = "Аскер Исмайлов"
YEAR = "2026"
LANG = "ru"
DESCRIPTION = ("После случайного входа в невозможную красную телефонную будку Асгар оказывается "
               "связан с аварийным возвратным контуром машины из далёкого будущего. Каждое новое окно "
               "уводит его всё дальше вперёд по истории Земли и Вселенной, а путь к источнику постепенно "
               "превращается из попытки вернуться домой в проверку того, что человек готов сохранить, "
               "когда прошлое наконец становится достижимым.")
SUBJECTS = ["Научная фантастика", "Hard SF", "Путешествия во времени", "Временные парадоксы", "Далёкое будущее"]

TRIM_W_MM, TRIM_H_MM = 145.0, 215.0
BLEED_MM = 3.0
SHEET_CALIPER_MM = 0.10  # adjustable printer assumption for perfect-bound cover

TITLES = {
"01":("Глава 1","Подальше от шума"),"02":("Глава 2","Пока тебя не было"),
"03":("Глава 3","Зерно изображения"),"04":("Глава 4","Чужое место"),
"04a":("Интерлюдия I","Отклонение"),"05":("Глава 5","За несколько секунд"),
"06":("Глава 6","Право на собственное имя"),"07":("Глава 7","Знакомые глаза"),
"08":("Глава 8","По обе стороны стекла"),"08a":("Интерлюдия II","За пределами допуска"),
"09":("Глава 9","Другая речь"),"10":("Глава 10","На краю погрешности"),
"11":("Глава 11","Вещи после стирки"),"12":("Глава 12","Трещина в порядке"),
"13":("Глава 13","Под открытым небом"),"14":("Глава 14","Короткой дороги нет"),
"15":("Глава 15","Память железа"),"15a":("Интерлюдия III","Незаконченный обед"),
"16":("Глава 16","Как вас называть"),"17":("Глава 17","Место за столом"),
"18":("Глава 18","Из уст в уста"),"19":("Глава 19","До вечера починится"),
"20":("Глава 20","Вода у порога"),"21":("Глава 21","Небо под ногами"),
"22":("Глава 22","Что именно"),"22a":("Интерлюдия IV","На полях записи"),
"23":("Глава 23","После сказанного"),"24":("Глава 24","Там, где был берег"),
"25":("Глава 25","Через столько рук"),"26":("Глава 26","Пока держится огонь"),
"27":("Глава 27","Право на воздух"),"28":("Глава 28","На ручном управлении"),
"29":("Глава 29","Крошки на столе"),"30":("Глава 30","На расстоянии руки"),
}
ORDER = ["01","02","03","04","04a","05","06","07","08","08a","09","10","11","12","13","14","15","15a","16","17","18","19","20","21","22","22a","23","24","25","26","27","28","29","30"]

def clean_md(s):
    s=s.replace("\ufeff","").replace("\r\n","\n").replace("\r","\n").strip()
    lines=s.splitlines()
    if lines and lines[0].lstrip().startswith("#"):
        lines=lines[1:]
    return "\n".join(lines).strip()

def blocks(md):
    md=clean_md(md)
    out=[]; buf=[]
    def flush():
        nonlocal buf
        if buf:
            t=" ".join(x.strip() for x in buf).strip()
            if t: out.append(("p",t))
            buf=[]
    for ln in md.splitlines():
        t=ln.strip()
        if not t:
            flush(); continue
        if t in {"***","* * *","---"}:
            flush(); out.append(("break","")); continue
        if t.startswith("#"):
            flush(); continue
        buf.append(ln)
    flush()
    return out

def build_revision():
    """Короткая метка содержимого сборки.

    Считается по всем главам chapters_v4 и по утверждённой обложке. Если текст
    не менялся, метка та же; если менялся хоть один символ - другая. Через неё
    EPUB получает новый dc:identifier, иначе читалки считают пересобранный файл
    той же книгой, что уже стоит у них в библиотеке, и показывают старую копию.
    """
    h = hashlib.sha256()
    for path in sorted(CH.glob("*.md")):
        h.update(path.name.encode("utf-8"))
        h.update(path.read_bytes())
    h.update(approved_cover.APPROVED_BLOB_SHA1.encode("ascii"))
    return h.hexdigest()[:12]


def read_sections():
    if not PREFACE.exists(): raise SystemExit(f"Missing {PREFACE}")
    preface_bs=blocks(PREFACE.read_text(encoding="utf-8"))
    preface_wc=sum(len(re.findall(r"\b[\wЁёА-я-]+\b",t,re.UNICODE)) for k,t in preface_bs if k=="p")
    secs=[("preface","","Предисловие",preface_bs,preface_wc)]; total=preface_wc
    for key in ORDER:
        p=CH/(key+".md")
        if not p.exists(): raise SystemExit(f"Missing {p}")
        raw=p.read_text(encoding="utf-8")
        bs=blocks(raw)
        kicker,title=TITLES[key]
        if bs and bs[0][0]=="p" and title.lower() in bs[0][1].lower() and bs[0][1].strip().lower().startswith(("глава","интерлюдия")):
            bs=bs[1:]
        wc=sum(len(re.findall(r"\b[\wЁёА-я-]+\b",t,re.UNICODE)) for k,t in bs if k=="p")
        total += wc
        secs.append((key,kicker,title,bs,wc))
    if len(secs)!=35: raise SystemExit("Expected preface + 34 literary sections")
    return secs,total

def find_font(candidates):
    for p in candidates:
        if Path(p).exists(): return p
    raise SystemExit("Cyrillic font not found")

SERIF=find_font(["/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf","/usr/share/fonts/truetype/liberation2/LiberationSerif-Regular.ttf"])
SERIF_B=find_font(["/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf","/usr/share/fonts/truetype/liberation2/LiberationSerif-Bold.ttf"])
SANS=find_font(["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf","/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"])
SANS_B=find_font(["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf","/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"])
pdfmetrics.registerFont(TTFont("BookSerif",SERIF)); pdfmetrics.registerFont(TTFont("BookSerifB",SERIF_B))
pdfmetrics.registerFont(TTFont("BookSans",SANS)); pdfmetrics.registerFont(TTFont("BookSansB",SANS_B))

PAGE_W, PAGE_H = TRIM_W_MM*mm, TRIM_H_MM*mm
INNER, OUTER, TOP, BOTTOM = 19*mm, 15*mm, 17*mm, 18*mm
BODY_STYLE=ParagraphStyle("body",fontName="BookSerif",fontSize=10.2,leading=13.05,alignment=TA_JUSTIFY,
                          firstLineIndent=5.2*mm,spaceAfter=0,allowWidows=0,allowOrphans=0)
NOIND_STYLE=ParagraphStyle("noind",parent=BODY_STYLE,firstLineIndent=0)
TITLE_STYLE=ParagraphStyle("ct",fontName="BookSerifB",fontSize=18,leading=22,alignment=TA_CENTER)
KICK_STYLE=ParagraphStyle("kick",fontName="BookSans",fontSize=8.5,leading=11,alignment=TA_CENTER,textColor=colors.HexColor("#555555"))

def esc(s): return html.escape(s,quote=False).replace("—","&#8212;")

class BookPDF:
    def __init__(self,path):
        self.c=canvas.Canvas(str(path),pagesize=(PAGE_W,PAGE_H),pageCompression=1)
        self.c.setTitle(TITLE)
        self.c.setAuthor(AUTHOR)
        self.c.setSubject("Роман")
        self.c.setCreator("asker421/Book V4 publishing pipeline")
        self.page=0; self.started_body=False; self.first_page_of_section=False
    def margins(self):
        # odd = recto, binding edge left; even = verso, binding edge right
        return (INNER,OUTER) if self.page%2==1 else (OUTER,INNER)
    def header_footer(self):
        if self.page<=2 or self.first_page_of_section: return
        left,right=self.margins()
        self.c.setFillColor(colors.HexColor("#555555")); self.c.setFont("BookSans",7.2)
        header = TITLE if self.page%2==0 else AUTHOR
        self.c.drawCentredString(PAGE_W/2,PAGE_H-9.5*mm,header)
        self.c.setFont("BookSans",8)
        x = 10.5*mm if self.page%2==0 else PAGE_W-10.5*mm
        self.c.drawCentredString(x,9.5*mm,str(self.page-2))
    def new_page(self,first=False):
        if self.page:
            self.header_footer(); self.c.showPage()
        self.page += 1; self.first_page_of_section=first
    def title_page(self):
        self.new_page(first=True)
        self.c.setFont("BookSerifB",25); self.c.drawCentredString(PAGE_W/2,PAGE_H*0.64,TITLE)
        self.c.setFont("BookSerif",13); self.c.drawCentredString(PAGE_W/2,PAGE_H*0.56,AUTHOR)
        self.c.setFont("BookSans",8); self.c.setFillColor(colors.HexColor("#777777"))
        self.c.drawCentredString(PAGE_W/2,22*mm,"Баку · 2026")
    def copyright_page(self):
        self.new_page(first=True)
        self.c.setFont("BookSerif",8.8); self.c.setFillColor(colors.black)
        y=42*mm
        for line in ["© Аскер Исмайлов, 2026","Все права защищены.","ISBN: ______________________________",
                     "Издатель: ___________________________"]:
            self.c.drawString(22*mm,y,line); y+=5.2*mm
    def section(self,kicker,title,bs):
        self.new_page(first=True)
        left,right=self.margins(); width=PAGE_W-left-right
        y=PAGE_H-46*mm
        if kicker:
            p=Paragraph(esc(kicker.upper()),KICK_STYLE); w,h=p.wrap(width,20*mm); p.drawOn(self.c,left,y-h); y-=h+6*mm
        p=Paragraph(esc(title),TITLE_STYLE); w,h=p.wrap(width,30*mm); p.drawOn(self.c,left,y-h); y-=h+18*mm
        first=True
        for typ,txt in bs:
            if typ=="break":
                needed=8*mm
                if y-needed<BOTTOM:
                    self.new_page(); left,right=self.margins(); width=PAGE_W-left-right; y=PAGE_H-TOP
                self.c.setFont("BookSerif",10); self.c.drawCentredString(PAGE_W/2,y-2*mm,"⁂"); y-=8*mm; first=True
                continue
            style=NOIND_STYLE if first else BODY_STYLE
            para=Paragraph(esc(txt),style)
            while True:
                avail=max(0,y-BOTTOM)
                parts=para.split(width,avail)
                if parts:
                    part=parts[0]; w,h=part.wrap(width,avail); part.drawOn(self.c,left,y-h); y-=h
                    if len(parts)==1: break
                    para=parts[1]
                    self.new_page(); left,right=self.margins(); width=PAGE_W-left-right; y=PAGE_H-TOP
                else:
                    self.new_page(); left,right=self.margins(); width=PAGE_W-left-right; y=PAGE_H-TOP
            first=False
    def finish(self):
        self.header_footer(); self.c.save(); return self.page

def build_interior(secs):
    path=OUT/"krasnaya-budka-v4-print-interior-145x215.pdf"
    b=BookPDF(path); b.title_page(); b.copyright_page()
    for _,kicker,title,bs,_ in secs: b.section(kicker,title,bs)
    pages=b.finish()
    return path,pages

def font_pil(path,size):
    return ImageFont.truetype(path,size=size)

import cover as approved_cover

def cover_front(size=None):
    """Передняя сторонка утверждённой автором обложки.

    Обложка не рисуется кодом и не берётся ниоткуда, кроме
    assets/cover_wrap.png. Проверка источника — в tools/cover.py.
    """
    return approved_cover.front(size)

def build_epub(secs,front):
    path=OUT/"Krasnaya_budka_Asker_Ismayilov_V4.epub"
    cover=OUT/"krasnaya-budka-v4-cover-epub.jpg"; front.save(cover,"JPEG",quality=95,optimize=True)
    revision=build_revision()
    book_id=f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL,'asker421/Book:Красная будка:V4:'+revision)}"
    modified=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    files={}
    css="""body{font-family:serif;line-height:1.5;margin:5%}h1{text-align:center;font-size:1.6em;margin:2em 0 .3em}h2{text-align:center;font-size:1.15em;font-weight:normal;margin:.3em 0 2em}p{margin:0;text-indent:1.25em;text-align:justify;orphans:2;widows:2}h2+p,.noindent{text-indent:0}.scene{text-align:center;margin:1.2em 0}.cover{text-align:center;margin:0}.cover img{max-width:100%;height:auto}.title{text-align:center;margin-top:30%}nav ol{list-style:none;padding:0}nav li{margin:.45em 0}"""
    files["styles.css"]=css.encode()
    def xdoc(title,body):
        return f'<?xml version="1.0" encoding="utf-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" lang="ru"><head><meta charset="utf-8"/><title>{html.escape(title)}</title><link rel="stylesheet" href="styles.css" type="text/css"/></head><body>{body}</body></html>'
    files["cover.xhtml"]=xdoc("Обложка",'<div class="cover"><img src="cover.jpg" alt="Обложка"/></div>').encode()
    files["title.xhtml"]=xdoc(TITLE,f'<div class="title"><h1>{TITLE}</h1><p class="noindent">{AUTHOR}</p></div>').encode()
    nav=[]; mani=[]; spine=[]; ncx=[]
    for i,(key,kicker,title,bs,wc) in enumerate(secs,1):
        body=[]
        first=True
        for typ,txt in bs:
            if typ=="break": body.append('<div class="scene">⁂</div>'); first=True
            else:
                cl=' class="noindent"' if first else ''
                body.append(f'<p{cl}>{html.escape(txt)}</p>'); first=False
        fn=f"ch{i:02d}.xhtml"; label=title if not kicker else f"{kicker}. {title}"
        files[fn]=xdoc(label,f"<h1>{html.escape(kicker)}</h1><h2>{html.escape(title)}</h2>"+''.join(body)).encode()
        nav.append(f'<li><a href="{fn}">{html.escape(label)}</a></li>')
        mani.append(f'<item id="c{i}" href="{fn}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="c{i}"/>')
        ncx.append(f'<navPoint id="n{i}" playOrder="{i}"><navLabel><text>{html.escape(label)}</text></navLabel><content src="{fn}"/></navPoint>')
    files["nav.xhtml"]=xdoc("Оглавление",'<nav xmlns:epub="http://www.idpf.org/2007/ops" epub:type="toc"><h1>Оглавление</h1><ol>'+''.join(nav)+'</ol></nav>').encode()
    files["toc.ncx"]=f'<?xml version="1.0" encoding="UTF-8"?><ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1"><head><meta name="dtb:uid" content="{book_id}"/></head><docTitle><text>{TITLE}</text></docTitle><navMap>{"".join(ncx)}</navMap></ncx>'.encode()
    files["content.opf"]=f'''<?xml version="1.0" encoding="utf-8"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="ru"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="bookid">{book_id}</dc:identifier><dc:title>{TITLE}</dc:title><dc:creator>{AUTHOR}</dc:creator><dc:language>ru</dc:language><dc:publisher>{AUTHOR}</dc:publisher><dc:description>{html.escape(DESCRIPTION)}</dc:description>{''.join(f'<dc:subject>{s}</dc:subject>' for s in SUBJECTS)}<dc:date>{YEAR}</dc:date><dc:source>build {revision}</dc:source><meta property="dcterms:modified">{modified}</meta><meta name="cover" content="cover-image"/></metadata><manifest><item id="cover-image" href="cover.jpg" media-type="image/jpeg" properties="cover-image"/><item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/><item id="title" href="title.xhtml" media-type="application/xhtml+xml"/><item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/><item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/><item id="css" href="styles.css" media-type="text/css"/>{''.join(mani)}</manifest><spine toc="ncx"><itemref idref="title"/>{''.join(spine)}</spine></package>'''.encode()
    container=b'<?xml version="1.0" encoding="UTF-8"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>'
    with zipfile.ZipFile(path,"w") as z:
        z.writestr("mimetype","application/epub+zip",compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml",container,compress_type=zipfile.ZIP_DEFLATED)
        bio=io.BytesIO(); front.save(bio,"JPEG",quality=95,optimize=True)
        z.writestr("OEBPS/cover.jpg",bio.getvalue(),compress_type=zipfile.ZIP_DEFLATED)
        for n,b in files.items(): z.writestr("OEBPS/"+n,b,compress_type=zipfile.ZIP_DEFLATED)
    with zipfile.ZipFile(path) as z:
        assert z.namelist()[0]=="mimetype" and z.getinfo("mimetype").compress_type==zipfile.ZIP_STORED
        for n in z.namelist():
            if n.endswith((".xhtml",".opf",".xml",".ncx")): ET.fromstring(z.read(n))
    return path,cover

def set_cell_margins(cell,top=0,start=0,bottom=0,end=0):
    tc=cell._tc; tcPr=tc.get_or_add_tcPr(); mar=tcPr.first_child_found_in("w:tcMar")
    if mar is None:
        mar=OxmlElement("w:tcMar"); tcPr.append(mar)
    for m,v in (("top",top),("start",start),("bottom",bottom),("end",end)):
        node=mar.find(qn("w:"+m))
        if node is None: node=OxmlElement("w:"+m); mar.append(node)
        node.set(qn("w:w"),str(v)); node.set(qn("w:type"),"dxa")

def build_docx(secs):
    p=OUT/"krasnaya-budka-v4-manuscript.docx"; d=Document()
    sec=d.sections[0]; sec.page_width=Mm(TRIM_W_MM); sec.page_height=Mm(TRIM_H_MM)
    sec.top_margin=Mm(17); sec.bottom_margin=Mm(18); sec.left_margin=Mm(19); sec.right_margin=Mm(15)
    sectPr=sec._sectPr; mirror=OxmlElement("w:mirrorMargins"); sectPr.append(mirror)
    styles=d.styles
    n=styles["Normal"]; n.font.name="Georgia"; n.font.size=Pt(10.5); n.paragraph_format.line_spacing=1.18; n.paragraph_format.first_line_indent=Mm(5.2); n.paragraph_format.space_after=Pt(0)
    for st in ["Title","Subtitle","Heading 1","Heading 2"]:
        styles[st].font.name="Georgia"
    x=d.add_paragraph(); x.alignment=WD_ALIGN_PARAGRAPH.CENTER; x.paragraph_format.space_before=Mm(68)
    r=x.add_run(TITLE); r.bold=True; r.font.size=Pt(25)
    x=d.add_paragraph(); x.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=x.add_run(AUTHOR); r.font.size=Pt(13)
    for idx,line in enumerate(["© Аскер Исмайлов, 2026","Все права защищены.","ISBN: ______________________________","Издатель: ___________________________"]):
        q=d.add_paragraph(line); q.paragraph_format.first_line_indent=Mm(0)
        if idx==0: q.paragraph_format.page_break_before=True
    for key,kicker,title,bs,wc in secs:
        q=d.add_paragraph(); q.paragraph_format.page_break_before=True; q.alignment=WD_ALIGN_PARAGRAPH.CENTER; q.paragraph_format.space_before=Mm(28)
        if kicker:
            r=q.add_run(kicker.upper()); r.font.name="Arial"; r.font.size=Pt(8.5)
        q=d.add_paragraph(); q.alignment=WD_ALIGN_PARAGRAPH.CENTER
        r=q.add_run(title); r.bold=True; r.font.size=Pt(18)
        first=True
        for typ,txt in bs:
            if typ=="break":
                q=d.add_paragraph("⁂"); q.alignment=WD_ALIGN_PARAGRAPH.CENTER; q.paragraph_format.first_line_indent=Mm(0); first=True
            else:
                q=d.add_paragraph(txt); q.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY
                if first: q.paragraph_format.first_line_indent=Mm(0)
                first=False
    cp=d.core_properties; cp.title=TITLE; cp.author=AUTHOR; cp.subject="Роман"; cp.keywords=", ".join(SUBJECTS)
    build_dt=datetime.now(timezone.utc).replace(tzinfo=None)
    cp.created=build_dt; cp.modified=build_dt
    d.save(p); return p

def build_cover(pages):
    """Полная обложка = утверждённый разворот, без дорисовки.

    Геометрия жёстко задана утверждённым artwork (корешок 21.5 мм). Если
    типографии нужен другой корешок, переделывается сам artwork, а не
    растягивается готовая картинка.
    """
    spine = approved_cover.SPINE_MM
    total_w = approved_cover.TOTAL_W_MM
    total_h = approved_cover.TOTAL_H_MM

    computed = round((pages / 2.0) * SHEET_CALIPER_MM, 2)
    if abs(computed - spine) > 0.5:
        print(f"ПРЕДУПРЕЖДЕНИЕ: расчётный корешок {computed} мм при {pages} стр. "
              f"расходится с корешком утверждённой обложки {spine} мм. "
              f"Публикуется утверждённый artwork; при печати сверьте с типографией.")

    wrap_image = approved_cover.wrap()

    pdf = OUT / "krasnaya-budka-v4-full-cover-145x215-bleed3mm.pdf"
    temp = OUT / ".approved-cover-for-pdf.jpg"
    wrap_image.save(temp, "JPEG", quality=95, optimize=True)
    try:
        c = canvas.Canvas(str(pdf), pagesize=(total_w * mm, total_h * mm), pageCompression=1)
        c.setTitle(f"{TITLE} — полная обложка")
        c.setAuthor(AUTHOR)
        c.setSubject("Полная печатная обложка")
        c.setCreator("asker421/Book V4 publishing pipeline")
        c.drawImage(str(temp), 0, 0, width=total_w * mm, height=total_h * mm,
                    preserveAspectRatio=False, mask="auto")
        c.showPage()
        c.save()
    finally:
        temp.unlink(missing_ok=True)

    dpi = 300
    W = round(total_w / 25.4 * dpi)
    H = round(total_h / 25.4 * dpi)
    wrap_png = OUT / "krasnaya-budka-v4-full-cover-preview-300dpi.png"
    wrap_image.resize((W, H), Image.Resampling.LANCZOS).save(
        wrap_png, "PNG", optimize=True, dpi=(dpi, dpi))

    return pdf, wrap_png, spine, total_w, total_h

def combined_markdown(secs):
    p=OUT/"krasnaya-budka-v4-master.md"; parts=[f"# {TITLE}\n\n**{AUTHOR}**\n"]
    for key,kicker,title,bs,wc in secs:
        heading=title if not kicker else f"{kicker}. {title}"
        parts += [f"\n\n# {heading}\n"]
        for typ,txt in bs:
            parts.append("\n***\n" if typ=="break" else "\n"+txt+"\n")
    p.write_text("".join(parts),encoding="utf-8"); return p

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()

def main():
    secs,total_words=read_sections()
    interior,pages=build_interior(secs)
    front=cover_front(); epub,cover_jpg=build_epub(secs,front)
    docx=build_docx(secs)
    full_cover,wrap_png,spine,total_w,total_h=build_cover(pages)
    master=combined_markdown(secs)
    meta={
      "title":TITLE,"author":AUTHOR,"language":"ru","year":2026,"genre":"научная фантастика / hard SF",
      "trim_mm":[TRIM_W_MM,TRIM_H_MM],"bleed_mm":BLEED_MM,"sections":34,"main_chapters":30,"interludes":4,"preface":True,
      "word_count":total_words,"print_pages":pages,"isbn":None,"publisher":None,
      "cover_spine_mm":spine,"spine_assumption":"Утверждённый автором artwork использует корешок 21.5 мм. Если шаблон типографии требует другую ширину, переделывается artwork, а не масштабируется готовая обложка.",
      "cover_source":"assets/cover_wrap.png (единственный утверждённый источник)","cover_source_git_blob_sha1":approved_cover.APPROVED_BLOB_SHA1,
      "source":f"asker421/Book main, chapters_v4, final publishing build {datetime.now(timezone.utc).date().isoformat()}","build_revision":build_revision(),
      "description":DESCRIPTION,"subjects":SUBJECTS
    }
    meta_p=OUT/"publication_metadata.json"; meta_p.write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
    readme=OUT/"README_PUBLISHING_PACKAGE.txt"
    readme.write_text(
      f"""{TITLE} — издательский пакет V4\nАвтор: {AUTHOR}\n\nСостав:\n- {interior.name}: печатный блок, {TRIM_W_MM:.0f}x{TRIM_H_MM:.0f} мм, без вылетов, {pages} стр.\n- {full_cover.name}: полная обложка с вылетами 3 мм; корешок {spine:.2f} мм.\n- {wrap_png.name}: 300 dpi preview/растровый источник полной обложки.\n- {cover_jpg.name}: обложка для EPUB.\n- {epub.name}: EPUB 3.\n- {docx.name}: редактируемый издательский исходник.\n- {master.name}: единый мастер-текст Markdown.\n- {meta_p.name}: метаданные издания.\n\nВАЖНО ПО КОРЕШКУ: утверждённый автором artwork использует корешок {spine:.2f} мм. Если шаблон типографии требует другую ширину, нужно переделать сам artwork, а не растягивать готовую обложку. ISBN намеренно не выдуман: поле оставлено пустым.\n\nОБЛОЖКА: единственный источник — assets/cover_wrap.png. Сборка падает, если файл заменён без обновления замка в tools/cover.py.\n\nИсточник текста: актуальная V4, предисловие + 30 глав + 4 интерлюдии.\nСлов: {total_words}.\n""",
      encoding="utf-8")
    files=[interior,full_cover,wrap_png,cover_jpg,epub,docx,master,meta_p,readme]
    sums=OUT/"SHA256SUMS.txt"; sums.write_text("\n".join(f"{sha256(p)}  {p.name}" for p in files)+"\n",encoding="utf-8"); files.append(sums)
    zip_p=OUT/"Krasnaya_budka_V4_PUBLISHING_PACKAGE.zip"
    with zipfile.ZipFile(zip_p,"w",zipfile.ZIP_DEFLATED) as z:
        for p in files: z.write(p,p.name)
    print(json.dumps({"build_revision":build_revision(),"pages":pages,"words":total_words,"spine_mm":spine,"zip":zip_p.name,
                      "files":[p.name for p in files],"zip_sha256":sha256(zip_p)},ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
