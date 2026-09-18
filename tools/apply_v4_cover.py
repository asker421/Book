#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import io
import json
import subprocess
import zipfile
from pathlib import Path

from PIL import Image, ImageFile
from reportlab.lib.pagesizes import mm
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "release_v4"
SOURCE = ROOT / "assets" / "v4_cover_wrap.webp"
FALLBACK_PARTS = [
    (ROOT / "assets" / "v4_cover_wrap_approved" / "part001.b64", "c931e692c4b5745aa5f1bca6e19bf02598252337"),
    (ROOT / "assets" / "v4_cover_wrap_approved" / "part002.b64", "2e7587c28cb60d4c9644d9e7ca4c047b5b66ce5f"),
    (ROOT / "assets" / "v4_cover_wrap_approved" / "part003.b64", "04b58dcc268a728eb1db2b445320ea767c5616b3"),
]
APPROVED_ARCHIVE_B64_CHARS = 38821
APPROVED_ARCHIVE_DANGLING_CHARS = 1

# This is the author-approved full flat wrap. Do not silently substitute another
# cover. If the author approves a new cover, replace the asset intentionally and
# update this lock in the same commit.
APPROVED_SOURCE_GIT_BLOB_SHA1 = "ddb54d6e89eeb7a54723de93771374d7f97c808f"
APPROVED_SOURCE_PIXELS = (1503, 1046)

TOTAL_W_MM = 317.5
TOTAL_H_MM = 221.0
BLEED_MM = 3.0
BACK_MM = 145.0
SPINE_MM = 21.5
FRONT_MM = 145.0
TRIM_H_MM = 215.0

EPUB = OUT / "Krasnaya_budka_Asker_Ismayilov_V4.epub"
EPUB_COVER = OUT / "krasnaya-budka-v4-cover-epub.jpg"
FULL_PDF = OUT / "krasnaya-budka-v4-full-cover-145x215-bleed3mm.pdf"
FULL_PREVIEW = OUT / "krasnaya-budka-v4-full-cover-preview-300dpi.png"
META = OUT / "publication_metadata.json"
README = OUT / "README_PUBLISHING_PACKAGE.txt"
SUMS = OUT / "SHA256SUMS.txt"
PACKAGE = OUT / "Krasnaya_budka_V4_PUBLISHING_PACKAGE.zip"


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def verify_approved_source_bytes() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Missing author-approved cover source: {SOURCE}")

    actual_blob = git_blob_sha1(SOURCE)
    if actual_blob != APPROVED_SOURCE_GIT_BLOB_SHA1:
        raise SystemExit(
            "Author-approved cover lock failed: "
            f"expected git blob {APPROVED_SOURCE_GIT_BLOB_SHA1}, got {actual_blob}. "
            "Do not publish until the cover change is explicitly approved and the lock is updated."
        )


def load_archived_approved_source() -> Image.Image:
    """Reconstruct the author-approved wrap from locked base64 archive parts.

    This is a fail-closed recovery path for CI environments that cannot decode the
    locked WebP. Every text part is pinned by its Git blob SHA before decoding.
    """
    chunks = []
    for path, expected_blob in FALLBACK_PARTS:
        if not path.exists():
            raise SystemExit(f"Missing approved cover archive part: {path}")
        actual_blob = git_blob_sha1(path)
        if actual_blob != expected_blob:
            raise SystemExit(
                "Approved cover archive lock failed: "
                f"{path.name}: expected git blob {expected_blob}, got {actual_blob}"
            )
        chunks.append("".join(path.read_text(encoding="ascii").split()))

    encoded = "".join(chunks)
    if len(encoded) != APPROVED_ARCHIVE_B64_CHARS:
        raise SystemExit(
            "Approved cover archive encoded length changed: "
            f"expected {APPROVED_ARCHIVE_B64_CHARS}, got {len(encoded)}"
        )

    # The locked archive predates this build guard and contains one known dangling
    # base64 character plus a JPEG without the optional EOI marker. Both quirks
    # are accepted ONLY for the exact SHA-pinned archive parts above.
    encoded = encoded[:-APPROVED_ARCHIVE_DANGLING_CHARS]
    try:
        data = base64.b64decode(encoded, validate=True)
        old_truncated = ImageFile.LOAD_TRUNCATED_IMAGES
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        try:
            with Image.open(io.BytesIO(data)) as probe:
                source = probe.convert("RGB")
        finally:
            ImageFile.LOAD_TRUNCATED_IMAGES = old_truncated
    except Exception as exc:
        raise SystemExit(f"Unable to reconstruct LOCKED approved cover archive: {exc!r}") from exc

    return source


def load_approved_source() -> Image.Image:
    """Load the locked wrap without ever substituting unapproved artwork.

    Pillow is attempted first, then dwebp. If this particular locked WebP cannot
    be decoded by the runner, reconstruct the same author-approved artwork from
    separately locked base64 archive parts committed to the repository.
    """
    try:
        with Image.open(SOURCE) as probe:
            source = probe.convert("RGB")
    except OSError as pillow_error:
        decoded = OUT / ".approved-v4-cover-decoded.png"
        try:
            subprocess.run(
                ["dwebp", str(SOURCE), "-o", str(decoded)],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            with Image.open(decoded) as probe:
                source = probe.convert("RGB")
        except (FileNotFoundError, subprocess.CalledProcessError, OSError):
            source = load_archived_approved_source()
            print(
                "Locked WebP decoder unavailable; used locked approved cover archive "
                f"(Pillow error: {pillow_error!r})."
            )
        finally:
            decoded.unlink(missing_ok=True)

    if source.size != APPROVED_SOURCE_PIXELS:
        raise SystemExit(
            f"Approved cover dimensions changed: expected {APPROVED_SOURCE_PIXELS}, got {source.size}"
        )
    return source


def mm_to_px_x(mm_value: float, width: int) -> int:
    return round(mm_value / TOTAL_W_MM * width)


def mm_to_px_y(mm_value: float, height: int) -> int:
    return round(mm_value / TOTAL_H_MM * height)


def make_front(source: Image.Image) -> Image.Image:
    x0 = mm_to_px_x(BLEED_MM + BACK_MM + SPINE_MM, source.width)
    x1 = mm_to_px_x(BLEED_MM + BACK_MM + SPINE_MM + FRONT_MM, source.width)
    y0 = mm_to_px_y(BLEED_MM, source.height)
    y1 = mm_to_px_y(BLEED_MM + TRIM_H_MM, source.height)
    front = source.crop((x0, y0, x1, y1)).convert("RGB")
    target_w = 1600
    target_h = round(target_w * TRIM_H_MM / FRONT_MM)
    return front.resize((target_w, target_h), Image.Resampling.LANCZOS)


def patch_epub_cover(epub_path: Path, cover_bytes: bytes) -> None:
    tmp = epub_path.with_suffix(".epub.tmp")
    with zipfile.ZipFile(epub_path, "r") as zin, zipfile.ZipFile(tmp, "w") as zout:
        for info in zin.infolist():
            data = cover_bytes if info.filename == "OEBPS/cover.jpg" else zin.read(info.filename)
            out = zipfile.ZipInfo(info.filename, info.date_time)
            out.compress_type = zipfile.ZIP_STORED if info.filename == "mimetype" else info.compress_type
            out.comment = info.comment
            out.extra = info.extra
            out.internal_attr = info.internal_attr
            out.external_attr = info.external_attr
            out.create_system = info.create_system
            out.flag_bits = info.flag_bits
            zout.writestr(out, data)
    tmp.replace(epub_path)
    with zipfile.ZipFile(epub_path, "r") as z:
        assert z.namelist()[0] == "mimetype"
        assert z.getinfo("mimetype").compress_type == zipfile.ZIP_STORED
        assert z.read("OEBPS/cover.jpg") == cover_bytes


def write_full_cover_pdf(source: Image.Image) -> None:
    temp = OUT / ".approved-v4-cover.jpg"
    source.convert("RGB").save(temp, "JPEG", quality=95, optimize=True)
    try:
        c = canvas.Canvas(str(FULL_PDF), pagesize=(TOTAL_W_MM * mm, TOTAL_H_MM * mm), pageCompression=1)
        c.drawImage(str(temp), 0, 0, width=TOTAL_W_MM * mm, height=TOTAL_H_MM * mm, preserveAspectRatio=False, mask="auto")
        c.showPage()
        c.save()
    finally:
        temp.unlink(missing_ok=True)


def write_preview(source: Image.Image) -> None:
    dpi = 300
    w = round(TOTAL_W_MM / 25.4 * dpi)
    h = round(TOTAL_H_MM / 25.4 * dpi)
    source.resize((w, h), Image.Resampling.LANCZOS).save(FULL_PREVIEW, "PNG", optimize=True, dpi=(dpi, dpi))


def update_metadata() -> None:
    if META.exists():
        data = json.loads(META.read_text(encoding="utf-8"))
        data["cover_spine_mm"] = SPINE_MM
        data["cover_source"] = "assets/v4_cover_wrap.webp (author-approved source of truth)"
        data["cover_source_git_blob_sha1"] = APPROVED_SOURCE_GIT_BLOB_SHA1
        data["cover_source_pixels"] = list(APPROVED_SOURCE_PIXELS)
        data["cover_total_mm"] = [TOTAL_W_MM, TOTAL_H_MM]
        data["spine_assumption"] = "Author-approved fixed cover artwork uses a 21.5 mm spine. Rebuild the artwork if printer stock requires a different spine."
        META.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_readme() -> None:
    if not README.exists():
        return
    text = README.read_text(encoding="utf-8")
    text = text.replace("корешок 21.25 мм", "корешок 21.5 мм")
    text = text.replace(
        "ВАЖНО ПО КОРЕШКУ: ширина 21.25 мм рассчитана из условной толщины листа 0.10 мм. Перед отправкой конкретной типографии подставьте её фактический paper caliper/шаблон.",
        "ВАЖНО ПО КОРЕШКУ: утверждённый автором artwork использует корешок 21.5 мм. Если шаблон конкретной типографии требует другую ширину, нужно адаптировать сам artwork, а не растягивать его автоматически."
    )
    lock_line = f"Approved cover git blob: {APPROVED_SOURCE_GIT_BLOB_SHA1}\n"
    if lock_line not in text:
        text += "\n" + lock_line
    README.write_text(text, encoding="utf-8")


def rebuild_checksums_and_package() -> None:
    files = sorted(
        p for p in OUT.iterdir()
        if p.is_file() and p.name not in {SUMS.name, PACKAGE.name}
    )
    lines = [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}" for p in files]
    SUMS.write_text("\n".join(lines) + "\n", encoding="utf-8")
    with zipfile.ZipFile(PACKAGE, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for p in files + [SUMS]:
            z.write(p, arcname=p.name)


def main() -> None:
    verify_approved_source_bytes()
    if not EPUB.exists():
        raise SystemExit(f"Build V4 release first; missing {EPUB}")

    source = load_approved_source()
    ratio = source.width / source.height
    expected = TOTAL_W_MM / TOTAL_H_MM
    if abs(ratio - expected) > 0.003:
        raise SystemExit(f"Cover source ratio {ratio:.6f} does not match {expected:.6f}")

    front = make_front(source)
    front.save(EPUB_COVER, "JPEG", quality=95, optimize=True)
    patch_epub_cover(EPUB, EPUB_COVER.read_bytes())
    write_full_cover_pdf(source)
    write_preview(source)
    update_metadata()
    update_readme()
    rebuild_checksums_and_package()

    print(f"Applied LOCKED author-approved V4 cover: {SOURCE}")
    print(f"Approved git blob: {APPROVED_SOURCE_GIT_BLOB_SHA1}")
    print(f"Approved source pixels: {source.width}x{source.height}")
    print(f"EPUB cover: {EPUB_COVER} ({front.width}x{front.height})")
    print(f"Full cover: {TOTAL_W_MM} x {TOTAL_H_MM} mm; spine {SPINE_MM} mm")


if __name__ == "__main__":
    main()
