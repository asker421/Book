#!/usr/bin/env python3
"""Замок релизной линии: публикуется только V4.

Автор закрыл линии V1 (chapters/), V2 (chapters_v2/) и V3 (chapters_v3/).
Их сборки удалены, и вернуться они не должны: любой новый workflow или
инструмент, который собирает книгу из старого корпуса, роняет проверку.

Сами корпуса остаются в репозитории как история текста — трогать их не нужно,
запрещено именно собирать из них релизы.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
TOOLS = ROOT / "tools"

CLOSED_CORPORA = ["chapters_v3", "chapters_v2", "chapters/"]

RETIRED_BUILDS = [
    ".github/workflows/build-epub-source.yml",
    ".github/workflows/freeze_v2_epub.yml",
    ".github/workflows/freeze_v2_epub_stdlib.yml",
    ".github/workflows/count_frozen_v2_words.yml",
    "tools/build_epub.py",
]

failures: list[str] = []


def main() -> None:
    for retired in RETIRED_BUILDS:
        if (ROOT / retired).exists():
            failures.append(f"Вернулась закрытая сборка: {retired}")

    scanned = sorted(WORKFLOWS.glob("*.yml")) + sorted(TOOLS.glob("*.py"))
    for path in scanned:
        if path.name == "verify_release_line.py":
            continue
        text = path.read_text(encoding="utf-8")
        for corpus in CLOSED_CORPORA:
            if corpus in text:
                failures.append(
                    f"{path.relative_to(ROOT)}: сборка из закрытого корпуса {corpus}"
                )

    if failures:
        print("ЗАМОК РЕЛИЗНОЙ ЛИНИИ: НЕ ПРОЙДЕН")
        for message in failures:
            print(f"  - {message}")
        raise SystemExit(1)

    print("ЗАМОК РЕЛИЗНОЙ ЛИНИИ: ПРОЙДЕН")
    print("  публикуется только chapters_v4; линии V1, V2 и V3 закрыты")


if __name__ == "__main__":
    main()
