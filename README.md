# Красная будка

Рабочий репозиторий романа «Красная будка».

Здесь хранятся канон, сюжетная карта, правила континьюти, визуальные законы и финальные версии глав. Черновики, признанные логически неверными, в главы не попадают.

## Структура
- `MANIFEST.md` — замысел, жанр, тон и обязательные принципы.
- `STORY_BIBLE.md` — механика будки, временные правила, мотивации и раскрытия.
- `CHAPTER_MAP.md` — карта 35 основных глав и 5 параллельных интерлюдий.
- `CONTINUITY.md` — факты, которые нельзя нарушать.
- `HARD_SCENE_CANON.md` — жёсткий канон связи, языка, физического staging, знания персонажей, среды, психологии и состояния Асгара.
- `CHARACTER_VOICE_CANON.md` — канонические голоса, эмоциональные реакции и поведенческие границы персонажей.
- `EPOCH_CAPABILITY_CANON.md` — технологический потолок и запреты каждой крупной эпохи.
- `TIME_CONTINUITY_CANON.md` — календарное и субъективное время Асгара, известные длительности и правила старения/обучения.
- `REVEAL_ORDER_CANON.md` — жёсткий порядок раскрытий по главам и запрет ретроактивного знания.
- `DECISION_MOTIVATION_CANON.md` — каноническая мотивация каждого крупного добровольного решения Асгара.
- `RELATIONSHIP_CANON.md` — динамика и границы ключевых отношений без случайной романтизации и эмоциональных скачков.
- `chapters/` — предыдущая редакция v1, сохраняется только как исторический/reference-корпус.
- `chapters_v2/` — актуальная чистовая редакция романа: 35 основных глав + 5 интерлюдий. Для чтения, аудита и будущей сборки использовать именно её.


## Project memory / передача между чатами

Для продолжения редакционной работы в новом чате сначала читать:

1. `PROJECT_MEMORY/00_READ_ME_FIRST.md`
2. `PROJECT_MEMORY/01_CURRENT_STATUS.md`
3. `PROJECT_MEMORY/02_CANON_AND_RULES.md`
4. `PROJECT_MEMORY/03_EDITORIAL_HISTORY.md`
5. `PROJECT_MEMORY/04_HANDOFF_PROMPT.md`
6. `PROJECT_MEMORY/05_RECENT_COMMIT_INDEX.md`
7. `PROJECT_MEMORY/06_V2_REWRITE.md`

Эти файлы — долговременная редакционная память проекта. После них читать актуальные `FINAL_CANON_OVERRIDE.md`, `HARD_SCENE_CANON.md`, `CHARACTER_VOICE_CANON.md`, `EPOCH_CAPABILITY_CANON.md`, `TIME_CONTINUITY_CANON.md`, `REVEAL_ORDER_CANON.md`, `DECISION_MOTIVATION_CANON.md`, `RELATIONSHIP_CANON.md`, `AUTHORING_RULES.md`, `STORY_BIBLE.md`, `CONTINUITY.md`, `CHAPTER_MAP.md`, `MANIFEST.md` и `NOVEL_FINAL_AUDIT_CHECKLIST.md`.

При конфликте память-файлов с более свежим содержимым ветки `main` источником истины остаётся актуальный `main`; затем memory-файлы нужно синхронизировать.
