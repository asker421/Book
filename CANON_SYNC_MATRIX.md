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
| Структура 35+5 | `CHAPTER_BY_CHAPTER_CANON.md` | chapter map, ledgers, chapters_v3 | PASS |
| Reveal | `REVEAL_ORDER_CANON.md` | knowledge, terminology, foreshadow | PASS |
| Знание персонажей | `KNOWLEDGE_LEDGER.md` | voices, motivation, chapters | PASS |
| Причина/следствие | `CAUSE_EFFECT_LEDGER.md` | decisions, conflict, foreshadow, chapters | PATCHED / PASS |
| Состояние Асгара | `ASGAR_STATE_LEDGER.md` | time, physics, continuity, chapters | PASS |
| Время | `TIME_CONTINUITY_CANON.md` | Asgar state, chapter contract | PASS |
| Физика | `PHYSICS_CANON.md` | hard scene, staging, final override | PASS at canon level |
| Геометрия/сцена | `LOCATION_STAGING_LEDGER.md` | physics, hard scene, chapters | PASS at canon level |
| Язык | `LANGUAGE_CANON.md` | hard scene, knowledge, epoch capability | PASS at canon level |
| Возможности эпох | `EPOCH_CAPABILITY_CANON.md` | physics, language, knowledge | PASS at canon level |
| Терминология | `TERMINOLOGY_CANON.md` | reveal, knowledge, final override | PASS |
| Мотивация решений | `DECISION_MOTIVATION_CANON.md` | anti-idiot, flaw, cause/effect | PASS |
| Мотивация персонажей | `CHARACTER_MOTIVATION_ANTI_IDIOT_CANON.md` | history, voice, knowledge, relationships | PASS |
| Биографии | `CHARACTER_HISTORY_CANON.md` | voice, motivation, relationship | PATCHED / PASS |
| Голоса | `CHARACTER_VOICE_CANON.md` | history, motivation, prose | PASS at canon level |
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

**Статус структуры: PASS.**

---

# 3. Персонажная матрица

Для каждого ключевого именованного повторяющегося персонажа проверено наличие в шести обязательных слоях:

**history → voice → motivation/anti-idiot → relationship → knowledge → chapter contract.**

| Персонаж | History | Voice | Motivation | Relationship | Knowledge | Chapter contract |
|---|---:|---:|---:|---:|---:|---:|
| Асгар | PASS | PASS | PASS | PASS | PASS | PASS |
| Катя | PASS | PASS | PASS | PASS | PASS | PASS |
| Мара | PASS | PASS | PASS | PASS | PASS | PASS |
| Самир | PATCHED | PASS | PASS | PATCHED | PASS | PASS |
| Лейла | PATCHED | PASS | PASS | PATCHED | PASS | PASS |
| Нура | PASS | PASS | PASS | PATCHED | PASS | PASS |
| Эмил | PASS | PASS | PASS | PATCHED | PASS | PASS |
| Тар | PASS | PASS | PASS | PATCHED | PASS | PASS |
| Лиан | PASS | PASS | PASS | PASS | PASS | PASS |
| Рен | PASS | PASS | PASS | PASS | PASS | PASS |
| Йо | PASS | PASS | PASS | PASS | PASS | PASS |
| Эс | PATCHED | PASS | PASS | PATCHED | PASS | PASS |
| Энар | PASS | PASS | PASS | PASS | PASS | PASS |
| Тавия | PASS | PASS | PASS | PASS | PASS | PASS |
| Киран | PASS | PASS | PASS | PASS | PASS | PASS |
| Селин | PASS | PASS | PASS | PASS | PASS | PASS |
| Орт | PASS | PASS | PASS | PASS | PASS | PASS |
| Сей | PASS | PASS | PASS | PATCHED | PASS | PASS |
| Аэль | PASS | PASS | PASS | PASS | PASS | PASS |
| Сет | PASS | PASS | PASS | PASS | PASS | PASS |
| Сава | PASS | PASS | PASS | PASS | PASS | PASS |
| Рауф Керимов | PASS | PASS | PASS | PASS | PASS | PASS |
| Кей | PASS | PASS | PASS | PASS | PASS | PASS |
| Вар | PASS | PASS | PASS | PASS | PASS | PASS |

**Дыр после текущей синхронизации: 0.**

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

## Кей — интерлюдии I и III

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

## Вар — главы 17–20

Канон:
- внешний риск Ар;
- ограничение неизвестной технологии;
- социальное недоверие без карикатурного зла;
- после Ар не следует за Асгаром.

Художественный текст:
- гл.17 — причинный вход через неизвестного человека + аномалию;
- гл.19 — социальное голосование и след конфликта;
- гл.20 — формальное ограничение у окна;
- решение Асгара уйти не вызвано Варом.

**Статус: PATCHED / CANONICALLY PRESENT.**

---

# 5. Теневая дуга Асгара

| Узел | Канон | Художественный V3 | Статус |
|---|---|---|---|
| гл.8 — полуправда Кате | `ASGAR_FLAW_CANON` | Катя ловит разницу между «могу передумать» и «ещё не решил» | PATCHED |
| гл.22 — удар по Маре | flaw + relationship + cause/effect | Асгар назначает Мару адресатом вины; Мара ставит границу | PATCHED |
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
- служебные ярлыки «молодой/старший Асгар» запрещены в художественной прозе и удалены из финальной сцены, где были найдены;
- визуальные реакции Мары допустимы только в интерлюдиях с POV на стороне службы, не через телефон Асгара.

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

**Статус текущих глав: REWRITE REQUIRED.**

Нельзя присвоить существующей главе AUTHOR STYLE PASS только за локальную хирургическую правку.

---

# 9. Состояние V3-корпуса относительно V2

Актуальный snapshot после текущего цикла синхронизации:

- файлов V3: **40**;
- файлов, blob SHA которых отличается от V2: **21**;
- файлов, которые всё ещё побайтно равны V2: **19**.

Изменение SHA **не означает полный rewrite**: часть файлов получила только канонические хирургические исправления, необходимые для устранения уже найденных конфликтов.

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
| 01-16-avgusta.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 02-chetyre-dnya.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 03-sled.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 04-okno.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 04a-lishnyaya-massa.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 05-dvadtsat-pyat-let.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 06-mertvyy-chelovek.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 07-arhiv-16-08.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 08-vtoroe-okno.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 08a-raschet-ne-shoditsya.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 09-novaya-klimaticheskaya-epoha.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 10-krasnyy-koridor.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 11-ozhidanie.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 12-shturm.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 13-posle-voyny.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 14-mashiny-bez-hozyaev.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 15-protokol.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 15a-smena.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 16-mara.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 17-posle-vtorogo-padeniya.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 18-chelovek-iz-krasnoy-dveri.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 19-dolgoe-ozhidanie.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 20-vozrozhdenie.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 21-nepreryvnost.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 22-ne-domoy.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 22a-slepaya-zona.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 23-istochnik.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 24-milliony-let.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 25-posledniy-arhiv-zemli.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 26-odin.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 27-poslanie.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 28-smert-zemli.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 29-poslednie-zvezdy.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 30-temnaya-epoha.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 30a-do-poslednego-okna.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 31-retro-1.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 32-vy-pochti-doshli.md | COVERED | COVERED | byte-identical | REWRITE REQUIRED |
| 33-tishina.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 34-liniya-istochnika.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |
| 35-16-avgusta.md | COVERED | COVERED | patched/different SHA | REWRITE REQUIRED |

---

# 11. Исправления, выполненные при создании матрицы

1. `FINAL_CANON_OVERRIDE.md` переведён с устаревших художественных ссылок `chapters_v2/31,34,35` на `chapters_v3/`.
2. Алиев в главах 2–5 синхронизирован с каноническим Рауфом Керимовым.
3. Кей реально введён в Интерлюдии I и III.
4. Вар реально введён в главы 17, 19, 20.
5. Теневая дуга Асгара синхронизирована в главах 8, 22, 23, 30, 33, 35.
6. Удалены найденные служебные возрастные ярлыки из финальной художественной прозы.
7. Самир, Лейла и Эс получили недостающие history-профили.
8. Самир, Лейла, Эс, Нура/Эмил/Тар и Сей получили недостающие relationship-контракты.
9. Удалён дублированный блок human-conflict causal chains из `CAUSE_EFFECT_LEDGER.md`.
10. Персонажная матрица повторно проверена: 24/24 ключевых персонажа имеют шесть обязательных слоёв.

---

# 12. Что сейчас герметично, а что нет

## Герметично на уровне канонической архитектуры

- структура 35+5;
- приоритет источников;
- финальная механика;
- reveal-order;
- knowledge firewall;
- персонажные history/voice/motivation/relationship/knowledge/contracts;
- конфликтные дуги;
- теневая дуга Асгара;
- cause/effect;
- физический канон;
- staging;
- language;
- terminology;
- author-style stack;
- audit stack.

## Ещё НЕ герметично как готовый роман V3

**Художественный корпус.**

Причина не в отсутствии канонов, а в том, что полный rewrite V3 ещё не произведён для 40 глав/интерлюдий по новому авторскому ДНК.

Поэтому текущий глобальный статус:

# **CANON ARCHITECTURE: PASS**
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
