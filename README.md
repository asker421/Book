# Красная будка

Рабочий репозиторий романа «Красная будка».

## Активная версия

Текущий художественный source of truth — **`chapters_v4/`**.

Активная структура:
- **30 основных глав**;
- **4 интерлюдии**;
- финальный блок: **28 → 29 → 30**.

`chapters_v2/` и `chapters_v3/` — исторические версии. Они могут использоваться только как редакционная история и не переопределяют V4.

Перед любой работой сначала читать **`MANIFEST.md`**.

## Ключевые активные документы

- `V4_AUTHORING_RULES.md` — рабочие правила V4.
- `V4_NAMING_CANON.md` — утверждённые названия и имена.
- `FINAL_CANON_OVERRIDE.md` — абсолютный source of truth финальной механики.
- `CHAPTER_BY_CHAPTER_CANON.md` — активные chapter contracts.
- `PHYSICS_CANON.md` — физика RETRO-1, двери, массы, материализации и исторического доступа.
- `TIME_CONTINUITY_CANON.md` — календарное и субъективное время.
- `REVEAL_ORDER_CANON.md` — порядок раскрытий.
- `KNOWLEDGE_LEDGER.md` — кто что знает и когда.
- `ASGAR_STATE_LEDGER.md` — тело, инвентарь, язык, навыки и психологическое состояние Асгара.
- `CAUSE_EFFECT_LEDGER.md` — причинно-следственные цепочки.
- `FORESHADOWING_PAYOFF_LEDGER.md` — seeds/reframes/payoffs.
- `LOCATION_STAGING_LEDGER.md` + `MICRO_STAGING_CANON.md` — геометрия и покадровая наблюдаемость.
- `EPOCH_CAPABILITY_CANON.md` — технологические возможности эпох.
- `LANGUAGE_CANON.md` — язык и каналы понимания.
- `DECISION_MOTIVATION_CANON.md` + `CHARACTER_MOTIVATION_ANTI_IDIOT_CANON.md` — мотивация и очевидные альтернативы.
- `CHARACTER_HISTORY_CANON.md`, `CHARACTER_REVEAL_MAP.md`, `CHARACTER_VOICE_CANON.md`, `RELATIONSHIP_CANON.md` — персонажи.
- `ASGAR_FLAW_CANON.md` — теневая дуга Асгара.
- `NARRATIVE_STYLE_CANON.md`, `CANON_AUTHOR_STYLE_V3.md`, `PROSE_DIALOGUE_CANON.md`, `READER_EXPERIENCE_CANON.md`, `CANON_WRITING_TICS.md` — стиль и проза. Имя `CANON_AUTHOR_STYLE_V3.md` историческое; сам стилевой метод продолжает применяться к V4.

## Аудит

Активный audit stack:
- `MASTER_ROMAN_AUDIT.md`;
- `CHAPTER_AUDIT_PROMPT.md`;
- `MAXIMUM_CAUTION_AUDIT_PROTOCOL.md`;
- `NOVEL_FINAL_AUDIT_CHECKLIST.md`;
- `CANON_SYNC_MATRIX.md`.

Любой новый аудит начинается с **NOT VERIFIED**. Старый PASS/READY не переносится на изменённый художественный blob.

Обязательные финальные pair-check:
- **глава 1 ↔ глава 30 (2014)**;
- **глава 8 ↔ глава 30 (2039)**.

## Исторические каталоги

- `chapters/` — ранняя версия;
- `chapters_v2/` — замороженный V2;
- `chapters_v3/` — предыдущая 35+5 архитектура;
- `V3_ARCHITECTURE_MAP.md`, `V3_AUDIT_PROTOCOL.md`, `V3_PROGRESS.md` — исторические V3-служебные материалы.

Исторические материалы не являются release-gate V4.

## Project memory / handoff

Новый чат начинает с:
1. `MANIFEST.md`;
2. `V4_AUTHORING_RULES.md`;
3. `V4_NAMING_CANON.md`;
4. релевантных специализированных канонов;
5. только затем — `PROJECT_MEMORY/` и старых worklogs при необходимости.

При конфликте памяти/handoff со свежим `main` действует актуальный canon stack V4.
