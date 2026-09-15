# CANON SYNC MATRIX — «Красная будка» V3

## 0. Статус документа

Этот файл — обязательная контрольная матрица синхронизации:

**MANIFEST ↔ специализированные каноны ↔ ledgers ↔ персонажи ↔ главы V3 ↔ audit/release gates.**

Он не создаёт сюжет сам по себе. Он показывает, какие слои уже согласованы, где есть только покрытие правилами, а где художественный текст ещё обязан быть переписан/проверен.

### Легенда

- **PASS** — источник истины и зависимые документы согласованы.
- **PATCHED** — обнаруженный конкретный рассинхрон исправлен в текущем цикле.
- **COVERED** — правило/ledger существует и покрывает область, но это не означает, что каждая строка художественного текста уже прошла финальный audit.
- **REWRITE REQUIRED** — художественный файл ещё не является полноценным rewrite V3 с нуля по действующим канонам.
- **AUDIT REQUIRED** — после rewrite нужен полный chapter pass.
- **BLOCKED** — релиз/EPUB/печать запрещены до закрытия условия.

Главный принцип:

> **Наличие канона не равно соблюдению канона главой. Наличие файла в chapters_v3 не равно завершённому V3 rewrite.**

---

# 1. Источник истины и приоритет

| Область | Главный источник | Зависимые источники | Статус |
|---|---|---|---|
| Индекс проекта | `MANIFEST.md` | все canon/ledger/audit files | PASS |
| Финальная механика | `FINAL_CANON_OVERRIDE.md` | physics, terminology, reveal, chapters 34–35 | PATCHED / PASS |
| Структура 35+5 | `CHAPTER_BY_CHAPTER_CANON.md` + `V3_ARCHITECTURE_MAP.md` | chapter map, ledgers, chapters_v3 | PATCHED / PASS |
| Reveal | `REVEAL_ORDER_CANON.md` | knowledge, terminology, foreshadow | PASS |
| Знание персонажей | `KNOWLEDGE_LEDGER.md` | voices, motivation, chapters | PATCHED / PASS |
| Причина/следствие | `CAUSE_EFFECT_LEDGER.md` | decisions, conflict, foreshadow, chapters | PATCHED / PASS |
| Состояние Асгара | `ASGAR_STATE_LEDGER.md` | time, physics, continuity, chapters | PATCHED / PASS |
| Время | `TIME_CONTINUITY_CANON.md` | Asgar state, chapter contract | PATCHED / PASS |
| Физика | `PHYSICS_CANON.md` | hard scene, staging, final override | PASS at canon level |
| Геометрия/сцена | `LOCATION_STAGING_LEDGER.md` | physics, hard scene, chapters | PASS at canon level |
| Язык | `LANGUAGE_CANON.md` | hard scene, knowledge, epoch capability | PASS at canon level |
| Возможности эпох | `EPOCH_CAPABILITY_CANON.md` | physics, language, knowledge | PASS at canon level |
| Терминология | `TERMINOLOGY_CANON.md` | reveal, knowledge, final override | PASS |
| Мотивация решений | `DECISION_MOTIVATION_CANON.md` | anti-idiot, flaw, cause/effect | PASS |
| Мотивация персонажей | `CHARACTER_MOTIVATION_ANTI_IDIOT_CANON.md` | history, voice, knowledge, relationships | PASS |
| Биографии | `CHARACTER_HISTORY_CANON.md` | voice, motivation, relationship | PATCHED / PASS |
| Художественное раскрытие прошлого | `CHARACTER_REVEAL_MAP.md` | history, knowledge, chapter contract, foreshadow | PATCHED / PASS |
| Голоса | `CHARACTER_VOICE_CANON.md` | history, motivation, prose | PATCHED / PASS at canon level |
| Отношения | `RELATIONSHIP_CANON.md` | history, motivation, chapters | PATCHED / PASS |
| Конфликт/антагонизм | `CONFLICT_ANTAGONISM_CANON.md` | motivation, voice, knowledge, cause/effect | PATCHED / PASS |
| Недостатки Асгара | `ASGAR_FLAW_CANON.md` | decisions, relationships, cause/effect | PATCHED / PASS |
| POV/дистанция | `NARRATIVE_STYLE_CANON.md` | author style, prose, knowledge | PASS |
| Авторский ДНК | `CANON_AUTHOR_STYLE_V3.md` | narrative, prose, reader experience, tics | PASS at canon level |
| Проза/диалоги | `PROSE_DIALOGUE_CANON.md` | voices, author style, reader experience | PASS at canon level |
| Проживаемость | `READER_EXPERIENCE_CANON.md` | narrative, prose, chapter contract | PASS at canon level |
| Анти-тики | `CANON_WRITING_TICS.md` | prose, author style, conflict | PASS |
| Foreshadow/payoff | `FORESHADOWING_PAYOFF_LEDGER.md` | reveal, cause/effect, final override | PASS at ledger level |

**Важно:** строки «PASS at canon level» не дают художественным главам автоматический PASS.

---

# 2. Структурная герметичность

Текущий `chapters_v3/` содержит:

- **35 основных глав**;
- **5 интерлюдий**;
- всего **40 художественных файлов**.

`CHAPTER_BY_CHAPTER_CANON.md` содержит явный контракт ровно для тех же 40 файлов.

Пропущенных chapter contracts: **0**.  
Лишних chapter contracts: **0**.

`PHYSICS_CANON.md`, `ASGAR_STATE_LEDGER.md`, `KNOWLEDGE_LEDGER.md` покрывают главы 1–35 и интерлюдии I–V.

**Статус структуры: PATCHED / PASS.**

---

# 3. Персонажная матрица

Для каждого ключевого именованного повторяющегося персонажа проверено наличие в шести обязательных слоях:

**history → voice → motivation/anti-idiot → relationship → knowledge → chapter contract.**

| Персонаж | History | Voice | Motivation | Relationship | Knowledge | Chapter contract |
|---|---:|---:|---:|---:|---:|---:|
| Асгар | PASS | PASS | PASS | PASS | PASS | PASS |
| Катя | PASS | PASS | PASS | PASS | PASS | PASS |
| Марен | PASS | PASS | PASS | PASS | PASS | PASS |
| Адриан | PATCHED | PASS | PASS | PATCHED | PASS | PASS |
| Элена | PATCHED | PASS | PASS | PATCHED | PASS | PASS |
| Нелия | PASS | PASS | PASS | PATCHED | PASS | PASS |
| Эмиан | PASS | PASS | PASS | PATCHED | PASS | PASS |
| Тавиан | PASS | PASS | PASS | PATCHED | PASS | PASS |
| Лорен | PASS | PASS | PASS | PASS | PASS | PASS |
| Ренел | PASS | PASS | PASS | PASS | PASS | PASS |
| Йорин | PASS | PASS | PASS | PASS | PASS | PASS |
| Ирия | PATCHED | PASS | PASS | PATCHED | PASS | PASS |
| Эриан | PASS | PASS | PASS | PASS | PASS | PASS |
| Тавена | PASS | PASS | PASS | PASS | PASS | PASS |
| Кирен | PASS | PASS | PASS | PASS | PASS | PASS |
| Селиан | PASS | PASS | PASS | PASS | PASS | PASS |
| Орлан | PASS | PASS | PASS | PASS | PASS | PASS |
| Сарен | PASS | PATCHED | PASS | PATCHED | PATCHED | PASS |
| Аурел | PASS | PASS | PASS | PASS | PASS | PASS |
| Северин | PASS | PASS | PASS | PASS | PASS | PASS |
| Авелина | PASS | PASS | PASS | PASS | PASS | PASS |
| Рауф Керимов | PASS | PASS | PASS | PASS | PASS | PASS |
| Дариан | PASS | PASS | PASS | PASS | PASS | PASS |
| Вален | PASS | PASS | PASS | PASS | PASS | PASS |

**Дыр после текущей синхронизации: 0.**

### Повторяющиеся неименованные роли

Для них emotional relationship layer не обязателен как отдельная сквозная связь, но обязательны **history/competence → motivation/entry causality → voice motor → knowledge firewall → chapter-local contract**.

| Роль | History / competence | Motivation | Voice | Knowledge | Scene/contract | Статус |
|---|---:|---:|---:|---:|---:|---:|
| Предыдущая женщина на линии | PASS | PASS | PASS | PASS | PASS | PASS |
| Куратор / сотрудники 2039 | PASS | PATCHED | PATCHED | PASS | PASS | PASS |
| Врач 2744 | PASS | PATCHED | PATCHED | PASS | PASS | PASS |
| Исследовательская группа Тавены | PASS | PATCHED | PATCHED | PASS by specialty | PASS | PASS |

Жёсткое правило: безымянность не разрешает универсальный «служебный голос» или коллективное всезнание.

Отдельно устранён **duplicate source-of-truth** в `CHARACTER_HISTORY_CANON.md`: ранние сокращённые дубли Адриан/Элена/Ирия удалены; для каждого оставлен один расширенный профиль.

---

## 3A. Герметичность раскрытия прошлого

`CHARACTER_REVEAL_MAP.md` включён в обязательный canon stack и audit gates.

Проверено разделение:
- `CHARACTER_HISTORY_CANON.md` хранит полную объективную биографию;
- `CHARACTER_REVEAL_MAP.md` определяет художественную доступность прошлого читателю;
- `KNOWLEDGE_LEDGER.md` ограничивает доступность знания персонажам;
- `CHAPTER_BY_CHAPTER_CANON.md` задаёт локальный контракт главы.

Исправленный конфликт:
- глава 33 больше не раскрывает Авелину как идентифицированного персонажа;
- разрешены только стук и неопознанный человеческий силуэт;
- имя, голос, профессия, бытовая конкретика и цепочка преемственности Авелины начинаются только в главе 34.

Audit coverage:
- `CHAPTER_AUDIT_PROMPT.md` — CHARACTER REVEAL GATE;
- `MASTER_ROMAN_AUDIT.md` — PASS 13A;
- `NOVEL_FINAL_AUDIT_CHECKLIST.md` — final character reveal continuity;
- `AUTHORING_RULES.md` — обязательный reveal gate до написания.

**Статус: PATCHED / PASS.**

---

# 4. Человеческий конфликт / антагонизм

## Рауф Керимов — главы 2–5

Канон:
- history — есть;
- voice — есть;
- motivation — есть;
- relationship — есть;
- knowledge firewall — есть;
- chapter contract — есть;
- continuity/cause-effect — есть.

Художественный текст:
- существующий следователь Алиев синхронизирован с каноном как **Рауф Керимов**;
- сохранена уже существовавшая причинность официального расследования;
- Рауф не заставляет Асгара войти;
- подтверждение аномалии не делает его автоматическим помощником.

**Статус: PATCHED / CANONICALLY PRESENT.**

## Дариан — интерлюдии I и III

Канон:
- отдельная этика операционного риска;
- не злодей;
- человек для него может исчезать внутри категории риска;
- не знает финальную механику;
- не управляет датами.

Художественный текст:
- Интерлюдия I: добавлена позиция «не расширять аварию повторными командами»;
- Интерлюдия III: добавлен конфликт вокруг вовлечённости оператора и границы между правом знать и сырой гипотезой.

**Статус: PATCHED / CANONICALLY PRESENT.**

## Вален — главы 17–20

Канон:
- внешний риск Ар;
- ограничение неизвестной технологии;
- социальное недоверие без карикатурного зла;
- после Ар не следует за Асгаром.

Художественный текст:
- гл.17 — причинный вход через неизвестного человека + аномалию;
- гл.19 — социальное голосование и след конфликта;
- гл.20 — формальное ограничение у окна;
- решение Асгара уйти не вызвано Валеном.

**Статус: PATCHED / CANONICALLY PRESENT.**

---

# 5. Теневая дуга Асгара

| Узел | Канон | Художественный V3 | Статус |
|---|---|---|---|
| гл.8 — полуправда Кате | `ASGAR_FLAW_CANON` | Катя ловит разницу между «могу передумать» и «ещё не решил» | PATCHED |
| гл.22 — удар по Марен | flaw + relationship + cause/effect | Асгар назначает Марен адресатом вины; Марен ставит границу | PATCHED |
| гл.23 — плохое извинение | flaw + relationship | сначала оправдывается, затем признаёт конкретную нечестность | PATCHED |
| гл.30 — чужой ресурс | flaw + motivation | пытается рационализировать расход чужого будущего | PATCHED |
| гл.33 — автономия | flaw + motivation | открывает процедуру пробуждения и останавливается до необратимого шага | PATCHED |
| гл.35 — смешанный мотив | final override + flaw | прямо признаёт, что защищал не только причинность, но и шанс на Катю | PATCHED |

**Статус теневой дуги: PASS по обязательным узлам; полный prose-pass после rewrite обязателен.**

---

# 6. Reveal / knowledge / terminology firewall

Проверены критические границы:

- `RETRO-1` — официальное раскрытие в основной линии с главы 31;
- «пустой модуль / незапланированный пассажир / пассажирская запись» — главный технический reveal главы 22;
- операторская структура — разрешённый блок Интерлюдия III / глава 16;
- историческая апертура — глава 34;
- мужчина 2014 = Асгар — окончательное физическое подтверждение глава 35;
- служебные ярлыки «молодой/Асгар после маршрута» запрещены в художественной прозе и удалены из финальной сцены, где были найдены;
- визуальные реакции Марен допустимы только в интерлюдиях с POV на стороне службы, не через телефон Асгара.

Статический critical-term scan не обнаружил подтверждённого раннего `RETRO-1`, пассажирской записи или исторической апертуры в основной линии.

**Статус: PASS на уровне критических reveal boundaries.**

---

# 7. Physics / staging / language

## Physics
`PHYSICS_CANON.md` фиксирует:
- физический интерьер;
- отсутствие мебели внутри будки;
- дверь и массовую сверку;
- отсутствие магического радиуса Асгара;
- стабильные/нестабильные окна;
- воздух/вакуум/воду/гравитацию/температуру;
- перенос предметов;
- физику всех 35 глав и 5 интерлюдий.

## Staging
`LOCATION_STAGING_LEDGER.md` отвечает за:
- слышимость;
- видимость;
- преграды;
- общий объём;
- дистанции;
- телефон/аудиомост;
- финальный 12-метровый участок.

## Language
`LANGUAGE_CANON.md` + `HARD_SCENE_CANON.md` отделяют:
- реальный язык;
- перевод;
- отсутствие автоматического взаимопонимания;
- доступность текста/надписей;
- операторский канал.

**Статус канонического слоя: PASS.**

**Статус художественного корпуса: AUDIT REQUIRED после полного rewrite каждой главы.**

Причина: старый текст V2 не может автоматически считаться прошедшим новые физические/staging/language gates только потому, что лежит в `chapters_v3/`.

---

# 8. Авторский стиль / проза / диалоги / голоса

Канонический стек:

`NARRATIVE_STYLE_CANON.md`
→ `CANON_AUTHOR_STYLE_V3.md` («Проза причинного эха»)
→ `PROSE_DIALOGUE_CANON.md`
→ `READER_EXPERIENCE_CANON.md`
→ `CANON_WRITING_TICS.md`
→ `CHARACTER_VOICE_CANON.md`.

Эти документы между собой синхронизированы по основным принципам:
- close third;
- жёсткая knowledge-фокализация;
- проживаемость вместо пересказа;
- анти-лесенка;
- собственные голоса;
- причинное эхо;
- неназванное неизвестное;
- эмоция как геометрия внимания;
- запрет превращать новый стиль в новый тик.

**Статус канонов: PASS.**

**Статус текущих глав: 1/40 FULL V3 PASS; 39/40 REWRITE REQUIRED.**

Нельзя присвоить существующей главе AUTHOR STYLE PASS только за локальную хирургическую правку.

---

# 9. Состояние V3-корпуса относительно V2

Актуальный snapshot после текущего цикла синхронизации:

- файлов V3: **40**;
- файлов с тем же техническим путём, blob SHA которых отличается от V2: **39**;
- файлов с тем же техническим путём, которые побайтно равны V2: **0**;
- отдельная переименованная пара пути: **1** — `chapters_v2/16-mara.md` → `chapters_v3/16-maren.md`.

Изменение SHA **не означает полный rewrite**: часть файлов получила только канонические хирургические исправления, необходимые для устранения уже найденных конфликтов.

Нормализация верхних заголовков до `Глава N` / `Интерлюдия I–V` сама по себе меняет SHA, поэтому после этого цикла SHA используется только как факт различия файлов, но не как оценка степени rewrite.

Следовательно:

> **Ни один файл не получает автоматический статус FULL V3 REWRITE только по факту отличия от V2 или нахождения в chapters_v3.**

Для перехода строки главы в FULL V3 PASS требуется:
1. прочитать v2 только как сюжетный материал;
2. загрузить весь релевантный canon stack;
3. заново построить сцену;
4. заново написать её по V3;
5. пройти `CHAPTER_AUDIT_PROMPT.md`;
6. пройти соответствующий слой `MASTER_ROMAN_AUDIT.md`;
7. обновить эту матрицу.

---

# 10. Chapter rewrite matrix

| Файл | Contract | Canon coverage | Current relation to V2 | Current V3 status |
|---|---|---|---|---|
| 01-16-avgusta.md | COVERED | SECOND COLD-START + LINE-BY-LINE PASS | 147 non-empty lines / 80 replica lines / 324 sentence-action units; restored canonical pre-threshold Ch1→2 boundary; 1↔35 continuity PASS; `WORD COUNT = 2415`; evidence in `worklogs_v3/01.md` | VERIFIED — FAIL COUNT 0 — AWAITING USER DECISION |
| 02-chetyre-dnya.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 03-sled.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 04-okno.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 04a-lishnyaya-massa.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 05-dvadtsat-pyat-let.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 06-mertvyy-chelovek.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 07-arhiv-16-08.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 08-vtoroe-okno.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 08a-raschet-ne-shoditsya.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 09-novaya-klimaticheskaya-epoha.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 10-krasnyy-koridor.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 11-ozhidanie.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 12-shturm.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 13-posle-voyny.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 14-mashiny-bez-hozyaev.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 15-protokol.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 15a-smena.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 16-maren.md | COVERED | COVERED | renamed path vs V2; not rewrite proof | REWRITE REQUIRED |
| 17-posle-vtorogo-padeniya.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 18-chelovek-iz-krasnoy-dveri.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 19-dolgoe-ozhidanie.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 20-vozrozhdenie.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 21-nepreryvnost.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 22-ne-domoy.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 22a-slepaya-zona.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 23-istochnik.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 24-milliony-let.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 25-posledniy-arhiv-zemli.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 26-odin.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 27-poslanie.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 28-smert-zemli.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 29-poslednie-zvezdy.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 30-temnaya-epoha.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 30a-do-poslednego-okna.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 31-retro-1.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 32-vy-pochti-doshli.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 33-tishina.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 34-liniya-istochnika.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |
| 35-16-avgusta.md | COVERED | COVERED | different SHA; not rewrite proof | REWRITE REQUIRED |

---

# 11. Исправления, выполненные при создании матрицы

1. `FINAL_CANON_OVERRIDE.md` переведён с устаревших художественных ссылок `chapters_v2/31,34,35` на `chapters_v3/`.
2. Алиев в главах 2–5 синхронизирован с каноническим Рауфом Керимовым.
3. Дариан реально введён в Интерлюдии I и III.
4. Вален реально введён в главы 17, 19, 20.
5. Теневая дуга Асгара синхронизирована в главах 8, 22, 23, 30, 33, 35.
6. Удалены найденные служебные возрастные ярлыки из финальной художественной прозы.
7. Адриан, Элена и Ирия получили недостающие history-профили.
8. Адриан, Элена, Ирия, Нелия/Эмиан/Тавиан и Сарен получили недостающие relationship-контракты.
9. Удалён дублированный блок human-conflict causal chains из `CAUSE_EFFECT_LEDGER.md`.
10. Персонажная матрица повторно проверена: 24/24 ключевых именованных персонажа имеют шесть обязательных слоёв.
11. Удалён duplicate source-of-truth для Адриан/Элена/Ирия в `CHARACTER_HISTORY_CANON.md`.
12. Для повторяющихся безымянных ролей добавлены отдельные motivation/voice gates.
13. Активная терминология возрастных состояний Асгара нормализована: внутренний canon stack использует «Асгар после маршрута» / «Асгар в 2014», без модели двух версий персонажа.
14. Канон Кати синхронизирован между `CHARACTER_HISTORY_CANON.md` и `RELATIONSHIP_CANON.md`: после исчезновения Асгара у неё нет новых романтических отношений; Катя закреплена как эмоциональная святыня романа, без нового партнёра, любовного треугольника или позднего «другого большого романа».
15. Добавлен 9+ execution gate: каждая глава обязана иметь необратимый delta; сложная физика подаётся через опыт до терминологии; главы 1/7/20/22/26/35 закреплены как разные landmark-сцены.
16. Финальный блок 31–35 переведён в режим обязательного драматургического сжатия: после 31-й запрещено расширять роман новыми крупными концепциями.
17. Разрыв доверия Асгар–Марен после главы 22 получил долговременное последствие; извинение главы 23 не обнуляет отношения.
18. Глава 26 получила обязательный психологический/голосовой delta за 22 месяца одиночества; глава 35 — запрет на лекционное исполнение финального payoff.
19. Создан `V3_ARCHITECTURE_MAP.md`: все 35 глав и 5 интерлюдий получили отдельный драматический двигатель, reader experience, необратимый delta и exit vector; отдельно зафиксированы зоны потенциального провисания и финальное сжатие.
20. Проведён cold-reader structural surgery: усилена причинность ухода из 2039 без превращения его в вынужденный побег; глава 16 вводит Марен через практический consent-test; архив «Человека из Красной двери» перенесён из главы 17 в причинно мотивированную главу 18; три точки «остаться/уйти» разведены по разным мотивациям; главы 24–25 закреплены как одна человеческая остановка, 29–30 — как одна поздняя ресурсная цивилизационная линия; правило однозначности оплачивается в 31 до финального применения; глава 35 получила конкретный человеческий payoff дуги контроля без нового mission hook.
21. Сквозной бытовой мотив дома закреплён как ситуация «кто-то ждёт Асгара домой/завтра» с максимум четырьмя структурными использованиями (1/7/20/35), без буквального рефрена.
22. Удалён остаток отменённого финала из `CONTINUITY.md`: краткое появление Асгара после маршрута в 2039 больше не превращается в длительное присутствие, обычную биометрию или новую биографию.
23. Главы 8 и 22 разведены по знанию и эмоции: глава 8 убирает гарантию дома, но оставляет человеческую надежду на отдельное решение источника; глава 22 раскрывает более глубокий факт — пассажир вообще не является штатным адресатом возвратной задачи.
24. Субъективная хронология пересчитана накопительно: итог ≈2,4 года, каноническая человеческая формулировка — «примерно два с половиной года»; «около года» к главе 23 исправлено на ≈5 месяцев; скрытое добирание месяцев запрещено.
25. Сарен получила полный voice profile, collision gate и отдельные knowledge boundaries.
26. Активный слой дочищен от всех legacy-имён персонажей; художественный V3 дополнительно проверен, единственный найденный остаток старого имени в Интерлюдии I исправлен.
27. `AUTHORING_RULES.md` разделён на AUDIT ONLY / AUDIT + SURGICAL REPAIR / CONTINUOUS WRITING; автоматический переход к следующей главе теперь разрешён только при явном включении непрерывного режима.
28. SHA-сравнение V2/V3 пересчитано по Git: 0 byte-identical среди 39 одинаковых путей; глава 16 имеет отдельный переименованный путь. SHA явно не используется как доказательство полного rewrite.
29. Рабочие названия глав сняты: художественный и служебный V3 использует только `Глава N` / `Интерлюдия I–V`; slug-имена файлов остаются техническими до финального именования после прозы.

---

# 11A. Build / release pipeline

Проверена не только рукопись, но и путь сборки.

| Контур | Состояние | Статус |
|---|---|---|
| `tools/build_epub.py` | читает `chapters_v3/`, не `chapters_v2/` | PATCHED / PASS |
| `.github/workflows/build-epub-source.yml` | следит за `chapters_v3/**` и `CANON_SYNC_MATRIX.md` | PATCHED / PASS |
| Working EPUB при RED/YELLOW матрице | имя `Krasnaya_budka_V3_WORKING_NOT_RELEASE.epub` | PASS |
| Финальный EPUB | допускается только когда матрица больше не содержит `REWRITE REQUIRED` / release block | BLOCKED сейчас |
| Frozen V2 workflows | остаются архивными и не являются текущей V3-сборкой | PASS / LEGACY |

Это закрывает опасный прежний рассинхрон: до исправления текущий EPUB workflow продолжал собирать `chapters_v2/`, хотя рабочим корпусом уже был объявлен V3.

---

# 12. Что сейчас герметично, а что нет

## Герметично на уровне канонической архитектуры

- структура 35+5;
- полный structural skeleton 40/40 в `V3_ARCHITECTURE_MAP.md`: двигатель / reader experience / irreversible delta / resistance / reveal-payoff / exit vector;
- cold-reader structure pass: глава 17 без раннего Red Door reveal; 18 получает причинный архивный двигатель; 24–25 и 29–30 не перезапускают новые социальные миры; 31 заранее оплачивает финальный инвариант; 35 закрывает дугу контроля человеческим решением;
- приоритет источников;
- финальная механика;
- reveal-order;
- knowledge firewall;
- персонажные history/voice/motivation/relationship/knowledge/contracts;
- character reveal architecture: след → давление → причина → payoff, с отдельной картой раскрытия прошлого;
- 9+ execution architecture: irreversible chapter delta, mass-market hard-SF accessibility, landmark scenes, secondary-character hierarchy и final contraction 31–35;
- конфликтные дуги;
- теневая дуга Асгара;
- cause/effect;
- физический канон;
- staging;
- language;
- terminology;
- author-style stack;
- audit stack.
- накопительная шкала субъективного времени без скрытых месяцев;
- различие reveal главы 8 и технического overturn главы 22;
- полные voice/knowledge boundaries Сарен;
- единый режим рабочих инструкций без конфликта auto-continue / stop-for-approval;
- временная политика названий: только номера до завершения prose rewrite.

## Ещё НЕ герметично как готовый роман V3

**Художественный корпус.**

Причина не в отсутствии канонов, а в том, что полный rewrite V3 ещё не произведён для 40 глав/интерлюдий по новому авторскому ДНК.

Поэтому текущий глобальный статус:

# **CANON ARCHITECTURE: PATCHED / PASS**
# **V3 ARTISTIC CORPUS: REWRITE REQUIRED**
# **RELEASE: BLOCKED**

---

# 13. Обязательное обновление матрицы

После любого изменения:
- нового канона;
- нового ledger;
- новой конфликтной дуги;
- изменения мотивации;
- изменения голоса;
- изменения знания;
- изменения физики;
- полного rewrite главы;
- финального chapter audit

редактор обязан обновить соответствующую строку/секцию этого файла в том же цикле.

Запрещено ставить `PASS` по памяти или по факту старого аудита.

PASS означает только состояние, подтверждённое актуальным корпусом и актуальными канонами.


# 14. Дополнительная герметизация audit/memory

- `AUTHORING_RULES.md`, `CHAPTER_AUDIT_PROMPT.md` и `NOVEL_FINAL_AUDIT_CHECKLIST.md` содержат явный FULL CANON STACK GATE.
- `PROJECT_MEMORY/04_HANDOFF_PROMPT.md` синхронизирован с author style, motivation, antagonism и Asgar flaw canons.
- `PROJECT_MEMORY/07_V3_NARRATIVE_STYLE.md` синхронизирован с `CANON_AUTHOR_STYLE_V3.md` и методом «Проза причинного эха».
- Любой root-level обязательный markdown обязан быть индексирован `MANIFEST.md`; MANIFEST DRIFT блокирует PASS.

---

# 14. Машинные проверки целостности

Последний sync-pass подтверждает:

- root-level markdown-файлов: **38**;
- root-level markdown-файлов, отсутствующих в `MANIFEST.md`: **0**;
- активных root `*_CANON.md` + `*_LEDGER.md`: **23**;
- активных canon/ledger, отсутствующих в `MANIFEST.md`: **0**;
- битых markdown-ссылок между активными canon/ledger/authoring/audit документами: **0** (шаблонные `*_CANON.md` / `*_LEDGER.md` не считаются файлами);
- chapter contracts: **40/40**;
- файлов `chapters_v3/`: **40/40**;
- byte-identical V2 среди 39 файлов с тем же техническим путём: **0/39**;
- отличающихся SHA среди тех же путей: **39/39**;
- отдельная переименованная пара пути: **1/40** (`16-mara.md` → `16-maren.md`);
- подтверждённых fail-closed full rewrite + exhaustive canon-register audit: **1/40** — Глава 1; `FAIL count = 0`, пользовательское одобрение ещё не получено.
- автоматических FULL V3 PASS по факту SHA: **0/40** — автоматическое присвоение запрещено.

### Reveal firewall

Критические границы согласованы:
- `RETRO-1` — основная линия с главы 31;
- пассажирская модель — раскрывается с главы 22;
- operator terminology в основном POV — с главы 16;
- исторический якорь / общий физический объём — поздний блок главы 34;
- физическое подтверждение личности мужчины 2014 — глава 35.

Проверенные ранние интерлюдии используют до reveal нейтральные категории вроде **внешней нагрузки / живой массы**, а не преждевременную пассажирскую модель.

### Physical / POV false-positive discipline

Автоматический поиск не считается доказательством нарушения без контекста:
- «скамейка» допустима снаружи будки;
- визуальное действие Марен допустимо в интерлюдии с POV службы;
- сравнительная конструкция «выглядел старше Асгара» не является служебным ярлыком «Асгар после маршрута»;
- слова «версия/копия» допустимы только там, где текст явно отвергает такую модель и не объясняет через неё финальную физику.

### Итог machine integrity gate

**MANIFEST INDEX: PASS**  
**ACTIVE CROSS-REFERENCES: PASS**  
**STRUCTURE 35+5: PASS**  
**CANON ARCHITECTURE: PATCHED / PASS**  
**ARTISTIC V3 COMPLETION: BLOCKED / REWRITE REQUIRED**

---
