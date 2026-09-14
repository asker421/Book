# FROZEN_V2 — статус литературного корпуса

**Status: SUPERSEDED RELEASE / EPUB STALE AFTER STRUCTURAL COMPRESSION**

- Source corpus: `chapters_v2/`
- Current literary source commit at this audit point: `80fd051667a1606188794facfac5cf8edbc748fd`
- Sections: `40` (35 основных глав + 5 интерлюдий)
- Words: `79034`
- Previous frozen EPUB: `release/krasnaya-budka-v2-FROZEN.epub`
- Previous EPUB status: **STALE — собран до удаления промежуточных миров и не соответствует текущему `main`**

Текущая литературная структура после хирургического сокращения не должна собираться или распространяться из прежнего frozen EPUB без новой сборки.

Удалены как самостоятельные эпохи: 12870, 312406 и Нэр / 91 208 004 000 000. Эпоха 703 118 402 объединена в одну главу. Финальная нумерация основной линии: 1–35.

Новый freeze допустим только после отдельной сборки EPUB из актуального `chapters_v2/` и проверки TOC, порядка 35 глав + 5 интерлюдий и соответствия текущему commit SHA.
