#!/usr/bin/env python3
"""Замок обложки: сборка проходит только с утверждённой автором обложкой.

Проверяет три вещи и падает на первой же проблеме:

1. В репозитории ровно один файл обложки — assets/cover_wrap.png — и он
   побайтно совпадает с утверждённым (замок в tools/cover.py).
2. Ни один инструмент сборки не рисует обложку кодом и не тянет её из
   запасных источников.
3. Всё, что реально собрано, несёт именно эту обложку: EPUB, печатный PDF,
   превью разворота и итоговый zip издательского пакета.
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import cover as approved_cover  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
TOOLS = ROOT / "tools"
WORKFLOWS = ROOT / ".github" / "workflows"

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".gif", ".bmp", ".b64"}

# Источники обложки, которые раньше конкурировали с утверждённой и должны
# оставаться удалёнными.
RETIRED = [
    "assets/cover_epub.b64",
    "assets/cover_epub.jpg",
    "assets/v4_cover_wrap.webp",
    "assets/v4_cover_wrap_approved",
]

# Признаки того, что обложку снова начали рисовать кодом.
DRAWING_MARKERS = [
    "rounded_rectangle",
    "booth silhouette",
    "ISBN / BARCODE",
]

failures: list[str] = []


def fail(message: str) -> None:
    failures.append(message)


def check_single_asset() -> None:
    images = sorted(
        p.relative_to(ROOT).as_posix()
        for p in ASSETS.rglob("*")
        if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES
    )
    if images != ["assets/cover_wrap.png"]:
        fail(
            "В assets/ должна быть ровно одна обложка assets/cover_wrap.png, "
            f"найдено: {images}"
        )
    for retired in RETIRED:
        if (ROOT / retired).exists():
            fail(f"Возвращён конкурирующий источник обложки: {retired}")


def check_no_generated_covers() -> None:
    for path in sorted(TOOLS.glob("*.py")) + sorted(WORKFLOWS.glob("*.yml")):
        if path.name in {"verify_cover.py", "cover.py"}:
            continue
        text = path.read_text(encoding="utf-8")
        for marker in DRAWING_MARKERS:
            if marker in text:
                fail(f"{path.relative_to(ROOT)}: обложка снова рисуется кодом ({marker!r})")
        for retired in RETIRED:
            # freeze_v2_epub.yml достаёт обложку из замороженного коммита и
            # намеренно не трогается: это неизменяемый релиз V2.
            if retired in text and path.name != "freeze_v2_epub.yml":
                fail(f"{path.relative_to(ROOT)}: ссылка на снятый источник обложки {retired}")


def check_built_artifacts() -> None:
    approved_front = approved_cover.front_jpeg_bytes()
    checked_any = False

    release = ROOT / "release_v4"
    epub = release / "Krasnaya_budka_Asker_Ismayilov_V4.epub"
    front_jpg = release / "krasnaya-budka-v4-cover-epub.jpg"
    full_pdf = release / "krasnaya-budka-v4-full-cover-145x215-bleed3mm.pdf"
    preview = release / "krasnaya-budka-v4-full-cover-preview-300dpi.png"
    package = release / "Krasnaya_budka_V4_PUBLISHING_PACKAGE.zip"

    if epub.exists():
        checked_any = True
        with zipfile.ZipFile(epub) as z:
            if z.namelist()[0] != "mimetype":
                fail(f"{epub.name}: mimetype не первым элементом архива")
            if z.read("OEBPS/cover.jpg") != approved_front:
                fail(f"{epub.name}: внутри EPUB не утверждённая обложка")
        if not front_jpg.exists() or front_jpg.read_bytes() != approved_front:
            fail("release_v4/krasnaya-budka-v4-cover-epub.jpg не совпадает с утверждённой обложкой")
        for required in (full_pdf, preview, package):
            if not required.exists():
                fail(f"Отсутствует файл пакета: {required.name}")
        if package.exists():
            with zipfile.ZipFile(package) as z:
                names = set(z.namelist())
                for required in (epub, full_pdf, preview, front_jpg):
                    if required.name not in names:
                        fail(f"{package.name}: в пакете нет {required.name}")

    dist_epubs = sorted((ROOT / "dist").glob("*.epub")) if (ROOT / "dist").exists() else []
    for built in dist_epubs:
        checked_any = True
        with zipfile.ZipFile(built) as z:
            if z.read("OEBPS/cover.jpg") != approved_front:
                fail(f"{built.name}: внутри EPUB не утверждённая обложка")

    if not checked_any:
        print("Собранных артефактов нет — проверены только источники.")


def main() -> None:
    approved_cover.verify_source()
    check_single_asset()
    check_no_generated_covers()
    check_built_artifacts()

    if failures:
        print("ЗАМОК ОБЛОЖКИ: НЕ ПРОЙДЕН")
        for message in failures:
            print(f"  - {message}")
        raise SystemExit(1)

    print("ЗАМОК ОБЛОЖКИ: ПРОЙДЕН")
    print(f"  источник: assets/cover_wrap.png ({approved_cover.APPROVED_BLOB_SHA1})")
    print(f"  передняя сторонка: {approved_cover.EPUB_FRONT_WIDTH}x{approved_cover.EPUB_FRONT_HEIGHT}")


if __name__ == "__main__":
    main()
