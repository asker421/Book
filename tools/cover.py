#!/usr/bin/env python3
"""Единственный источник обложки для всех сборок.

В репозитории есть ровно один файл обложки: assets/cover_wrap.png — утверждённый
автором плоский разворот (задняя сторонка + корешок + передняя сторонка).

Любая сборка (EPUB, печатный PDF, издательский пакет) обязана брать обложку
только отсюда. Рисовать обложку кодом, держать запасные копии в base64 или
подставлять другой файл запрещено: сборка падает, а не публикует чужую картинку.

Если автор утверждает новую обложку — заменить assets/cover_wrap.png и в том же
коммите обновить APPROVED_BLOB_SHA1 и APPROVED_PIXELS.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "cover_wrap.png"

APPROVED_BLOB_SHA1 = "361d1d1b20a2438ce0f9fa961629abd761056139"
APPROVED_PIXELS = (1503, 1046)

# Геометрия утверждённого разворота, мм.
BLEED_MM = 3.0
BACK_MM = 145.0
SPINE_MM = 21.5
FRONT_MM = 145.0
TRIM_H_MM = 215.0
TOTAL_W_MM = BLEED_MM + BACK_MM + SPINE_MM + FRONT_MM + BLEED_MM   # 317.5
TOTAL_H_MM = BLEED_MM + TRIM_H_MM + BLEED_MM                       # 221.0

# Передняя сторонка для EPUB: истинные пропорции обреза 145 x 215 мм.
EPUB_FRONT_WIDTH = 1600
EPUB_FRONT_HEIGHT = round(EPUB_FRONT_WIDTH * TRIM_H_MM / FRONT_MM)  # 2372


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def verify_source() -> None:
    if not SOURCE.exists():
        raise SystemExit(
            f"Нет утверждённой обложки: {SOURCE}. Сборка остановлена — "
            "публиковать книгу без утверждённой автором обложки нельзя."
        )
    actual = git_blob_sha1(SOURCE)
    if actual != APPROVED_BLOB_SHA1:
        raise SystemExit(
            "Обложка не совпадает с утверждённой: ожидался git blob "
            f"{APPROVED_BLOB_SHA1}, получен {actual}. Если обложку меняли осознанно, "
            "обновите APPROVED_BLOB_SHA1 в tools/cover.py тем же коммитом."
        )


def wrap() -> Image.Image:
    """Полный утверждённый разворот."""
    verify_source()
    with Image.open(SOURCE) as probe:
        image = probe.convert("RGB")
    if image.size != APPROVED_PIXELS:
        raise SystemExit(
            f"Размер обложки изменился: ожидалось {APPROVED_PIXELS}, получено {image.size}"
        )
    ratio = image.width / image.height
    expected = TOTAL_W_MM / TOTAL_H_MM
    if abs(ratio - expected) > 0.003:
        raise SystemExit(
            f"Пропорции обложки {ratio:.6f} не совпадают с разворотом {expected:.6f}"
        )
    return image


def front(size: tuple[int, int] | None = None) -> Image.Image:
    """Передняя сторонка, вырезанная из утверждённого разворота."""
    source = wrap()

    def mm_x(value: float) -> int:
        return round(value / TOTAL_W_MM * source.width)

    def mm_y(value: float) -> int:
        return round(value / TOTAL_H_MM * source.height)

    box = (
        mm_x(BLEED_MM + BACK_MM + SPINE_MM),
        mm_y(BLEED_MM),
        mm_x(BLEED_MM + BACK_MM + SPINE_MM + FRONT_MM),
        mm_y(BLEED_MM + TRIM_H_MM),
    )
    cropped = source.crop(box)
    target = size or (EPUB_FRONT_WIDTH, EPUB_FRONT_HEIGHT)
    return cropped.resize(target, Image.Resampling.LANCZOS)


def front_jpeg_bytes(size: tuple[int, int] | None = None, quality: int = 95) -> bytes:
    import io

    buffer = io.BytesIO()
    front(size).save(buffer, "JPEG", quality=quality, optimize=True)
    return buffer.getvalue()


if __name__ == "__main__":
    image = wrap()
    print(f"Утверждённая обложка: {SOURCE}")
    print(f"git blob: {APPROVED_BLOB_SHA1}")
    print(f"разворот: {image.width}x{image.height} ({TOTAL_W_MM} x {TOTAL_H_MM} мм)")
    print(f"передняя сторонка для EPUB: {EPUB_FRONT_WIDTH}x{EPUB_FRONT_HEIGHT}")
