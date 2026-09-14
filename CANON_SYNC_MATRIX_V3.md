# CANON SYNC MATRIX V3 — «Красная будка»

Дата контрольного прохода: 14.09.2026  
Репозиторий: `asker421/Book`  
Ветка: `main`

## 0. Назначение

Этот файл — контрольная матрица герметичности проекта. Он **не создаёт новый сюжетный канон** и не переопределяет специализированные источники истины. Его задача — показать, синхронизированы ли:

**MANIFEST → специализированные canons/ledgers → authoring/audit слой → художественные главы v3 → PROJECT_MEMORY.**

При конфликте действует порядок приоритета из `MANIFEST.md`.

### Статусы

- **GREEN / PASS** — проверяемая синхронизация подтверждена.
- **YELLOW / PARTIAL** — канон и инфраструктура синхронизированы, но художественная реализация не сертифицирована полным v3 rewrite + chapter audit.
- **RED / REWRITE REQUIRED** — текущий файл главы всё ещё идентичен frozen v2, поэтому по определению не прошёл обязательный полный v3 rewrite.
- **BLOCKER** — противоречие источников истины или прямое нарушение канона. На момент создания этой матрицы известных незакрытых BLOCKER на уровне canon-stack нет.

---

# 1. SOURCE-OF-TRUTH MATRIX

| Слой | Source of truth | MANIFEST | Cross-sync | Chapters v3 | Статус |
|---|---|---:|---:|---:|---|
| Иерархия источников | `MANIFEST.md` | self | PASS | применена | **GREEN** |
| Финальная механика | `FINAL_CANON_OVERRIDE.md` | PASS | ссылки исправлены на `chapters_v3/31,34,35` | 34–35 согласованы по механике | **GREEN** |
| Структура 35+5 | `CHAPTER_BY_CHAPTER_CANON.md` | PASS | 35 глав + 5 интерлюдий, ровно 40 файлов | 40/40 файлов существуют | **GREEN** |
| Legacy → V3 | `MANIFEST.md` / `FROZEN_V2.md` | PASS | v2 frozen, v3 working corpus | 19 файлов всё ещё byte-identical v2 | **YELLOW** |
| Authoring rules | `AUTHORING_RULES.md` | PASS | FULL CANON STACK GATE добавлен | обязательность зафиксирована | **GREEN** |
| Chapter audit | `CHAPTER_AUDIT_PROMPT.md` | PASS | FULL CANON STACK GATE + causal echo pass | применять после каждого rewrite | **GREEN** |
| Master audit | `MASTER_ROMAN_AUDIT.md` | PASS | полный стек уже покрыт | финальная сертификация впереди | **GREEN infrastructure / YELLOW corpus** |
| Release audit | `NOVEL_FINAL_AUDIT_CHECKLIST.md` | PASS | FULL CANON STACK GATE добавлен | release пока заблокирован rewrite-статусом | **GREEN infrastructure / YELLOW corpus** |
| PROJECT_MEMORY | `PROJECT_MEMORY/*` | subordinate | handoff/style memory синхронизированы | current status обновляется этой матрицей | **GREEN after this pass** |

Контроль: все **36 root-level markdown-файлов** упоминаются в `MANIFEST.md`. Неиндексированных root markdown-файлов: **0**.

---

# 2. ПОЛНЫЙ КАНОНИЧЕСКИЙ СТЕК

## 2.1. Механика, физика, время, пространство

| Область | Главный источник | Связанные источники | Канон ↔ канон | Канон ↔ главы | Статус |
|---|---|---|---:|---:|---|
| Одна временная линия / финальная петля | `FINAL_CANON_OVERRIDE.md` | `PHYSICS_CANON.md`, `TIME_CONTINUITY_CANON.md` | PASS | финал структурно совпадает | **GREEN/YELLOW prose** |
| Физика RETRO-1 | `PHYSICS_CANON.md` | `HARD_SCENE_CANON.md`, `FINAL_CANON_OVERRIDE.md` | PASS | явных bench/seat внутри будки не найдено | **GREEN structural** |
| Пассажирская масса | `PHYSICS_CANON.md` | `CAUSE_EFFECT_LEDGER.md`, `FINAL_CANON_OVERRIDE.md` | PASS | закрытие двери → mass check сохранено | **GREEN structural** |
| Даты не выбираются | `PHYSICS_CANON.md` | `REVEAL_ORDER_CANON.md`, `KNOWLEDGE_LEDGER.md` | PASS | ранней «кнопки даты» не выявлено | **GREEN structural** |
| Возможности эпох | `EPOCH_CAPABILITY_CANON.md` | `KNOWLEDGE_LEDGER.md`, `LANGUAGE_CANON.md` | PASS | требует line-audit при rewrite | **YELLOW** |
| Hard scene realism | `HARD_SCENE_CANON.md` | physics/staging/state | PASS | обязательный rewrite ещё не везде сделан | **YELLOW** |
| Staging / дистанции / география | `LOCATION_STAGING_LEDGER.md` | `HARD_SCENE_CANON.md` | PASS | критические финальные расстояния согласованы; полный corpus audit впереди | **YELLOW** |
| Язык / перевод | `LANGUAGE_CANON.md` | knowledge/epoch | PASS | явной универсальной магии языка не обнаружено; полный rewrite gate остаётся | **YELLOW** |

---

# 3. KNOWLEDGE / REVEAL MATRIX

| Проверка | Каноническое правило | Фактический статус v3 | Статус |
|---|---|---|---|
| Мара не появляется как известный Асгару человек раньше положенного | интерлюдия III / глава 16 | до `15a` имя Мара в художественном корпусе не появляется; основная линия вводит её в гл.16 | **GREEN** |
| Термин «оператор» не известен Асгару до гл.16 | reveal/knowledge | в главах 1–15 художественного корпуса термин не найден | **GREEN** |
| RETRO-1 не называется до гл.31 | reveal/knowledge | в главах до 31 название не найдено; гл.31 содержит официальное раскрытие | **GREEN** |
| Мужчина 2014 не подтверждён как Асгар заранее | reveal/final override | фактическое подтверждение сохраняется в гл.35 | **GREEN structural** |
| Никакого «молодой/старший Асгар» как служебного ярлыка в прозе | narrative/prose | остаточные ярлыки в гл.35 удалены | **GREEN** |
| Мара не получает невозможный видеоканал | history/knowledge/staging | конструкции «Асгар увидел/посмотрел на Мару» не найдены | **GREEN** |
| Гипотеза ≠ факт | `KNOWLEDGE_LEDGER.md` | инфраструктура синхронизирована; полный line-by-line audit только после rewrite каждой главы | **YELLOW** |

---

# 4. CHARACTER MATRIX

Для основных и повторяющихся именованных персонажей проверено наличие в:
`CHARACTER_HISTORY_CANON.md` → `CHARACTER_VOICE_CANON.md` → `CHARACTER_MOTIVATION_ANTI_IDIOT_CANON.md` → `RELATIONSHIP_CANON.md` → `KNOWLEDGE_LEDGER.md`.

| Персонаж | History | Voice | Motivation | Relationship | Knowledge | Conflict role |
|---|---:|---:|---:|---:|---:|---:|
| Асгар | ✓ | ✓ | ✓ | ✓ | ✓ | flaw/conflict ✓ |
| Катя | ✓ | ✓ | ✓ | ✓ | ✓ | не антагонист |
| Мара | ✓ | ✓ | ✓ | ✓ | ✓ | институциональный конфликт возможен, не злодей |
| Самир | ✓ | ✓ | ✓ | ✓ | ✓ | нет |
| Лейла | ✓ | ✓ | ✓ | ✓ | ✓ | rational opposition ✓ |
| Нура | ✓ | ✓ | ✓ | ✓ | ✓ | нет |
| Эмил | ✓ | ✓ | ✓ | ✓ | ✓ | нет |
| Тар | ✓ | ✓ | ✓ | ✓ | ✓ | нет |
| Лиан | ✓ | ✓ | ✓ | ✓ | ✓ | нет |
| Рен | ✓ | ✓ | ✓ | ✓ | ✓ | локальные конфликты допустимы |
| Йо | ✓ | ✓ | ✓ | ✓ | ✓ | нет |
| Эс | ✓ | ✓ | ✓ | ✓ | ✓ | epistemic resistance |
| Энар | ✓ | ✓ | ✓ | ✓ | ✓ | нет |
| Тавия | ✓ | ✓ | ✓ | ✓ | ✓ | scientific opposition ✓ |
| Киран | ✓ | ✓ | ✓ | ✓ | ✓ | нет |
| Селин | ✓ | ✓ | ✓ | ✓ | ✓ | нет |
| Орт | ✓ | ✓ | ✓ | ✓ | ✓ | ethical/medical boundary |
| Сей | ✓ | ✓ | ✓ | ✓ | ✓ | нет |
| Аэль | ✓ | ✓ | ✓ | ✓ | ✓ | rational conflict ✓ |
| Сет | ✓ | ✓ | ✓ | ✓ | ✓ | rational conflict ✓ |
| Сава | ✓ | ✓ | ✓ | ✓ | ✓ | финальный forensic counterweight |
| Рауф Керимов | ✓ | ✓ | ✓ | ✓ | ✓ | antagonist arc ✓ |
| Кей | ✓ | ✓ | ✓ | ✓ | ✓ | antagonist arc ✓ |
| Вар | ✓ | ✓ | ✓ | ✓ | ✓ | antagonist arc ✓ |

**Character canon coverage: 24/24 проверенных персонажей имеют полный базовый профиль history + voice + motivation + relationship + knowledge.**

Важно: наличие voice profile не означает автоматический PASS каждой реплики. Реплики в главе получают GREEN только после chapter-level voice audit.

---

# 5. HUMAN CONFLICT / ANTAGONISM MATRIX

| Дуга | Канон | Требуемое появление | Реализация v3 после sync-pass | Статус |
|---|---|---|---|---|
| Рауф Керимов | `CONFLICT_ANTAGONISM_CANON.md` | главы 2–5 | существующий следователь Алиев синхронизирован в Рауфа Керимова; архивный след в гл.7 также исправлен | **GREEN structural / YELLOW voice-cert** |
| Кей | там же | интерлюдии I и III | добавлен как операционный risk counterweight; не злодей, спорит о цене вмешательства и вовлечённости оператора | **GREEN structural / YELLOW voice-cert** |
| Вар | там же | 17, 19, 20 | введён как координатор внешнего риска Ар; социальный/процедурный конфликт; не выталкивает Асгара в маршрут | **GREEN structural / YELLOW voice-cert** |
| Лейла | rational opponent | 9–12 при необходимости | существующая дуга не превращена в злодейскую | **GREEN canon / YELLOW chapter audit** |
| Тавия | scientific opponent | 21–23 | сохраняется научным оппонентом | **GREEN canon / YELLOW chapter audit** |
| Аэль / Сет | rational conflict | 30 | спор о цене знания сохранён | **GREEN structural** |
| Зоны без искусственного нового злодея | conflict canon | 1; 6–8; 13–16 main; 21–29; 31–35 | новые персональные антагонисты туда не добавлены | **GREEN** |

Главный anti-pattern **«новая эпоха → новый злодей → преодоление → прыжок»** после sync-pass не создаётся.

---

# 6. ASGAR FLAW MATRIX

| Узел | Требование `ASGAR_FLAW_CANON.md` | v3 после исправления | Статус |
|---|---|---|---|
| Глава 8 | полуправда Кате: «ещё не решил», хотя путь уже default | добавлен прямой конфликт; Катя ловит подмену | **GREEN structural** |
| Глава 22 | несправедливый удар по Маре | добавлен; Мара ставит границу; мгновенного прощения нет | **GREEN structural** |
| Глава 23 | плохое конкретное извинение | добавлено без терапевтической идеальности | **GREEN structural** |
| Глава 30 | эгоистичная рационализация чужого ресурса | добавлена попытка назвать будущую жизнь «неиспользованным резервом» | **GREEN structural** |
| Глава 33 | почти нарушенная автономия | Асгар доходит до необратимого шага пробуждения и останавливается | **GREEN structural** |
| Глава 35 | смешанный мотив молчания | прямо признаёт: защищал не только причинность, но и шанс снова получить Катю | **GREEN structural** |

Полный психологический PASS всё равно требует prose/voice audit соответствующих глав.

---

# 7. CAUSE → EFFECT / STATE / PAYOFF MATRIX

| Слой | Source | Cross-sync | Глава-реализация | Статус |
|---|---|---:|---:|---|
| Причинные цепи | `CAUSE_EFFECT_LEDGER.md` | связан с physics/chapter canon | ключевые цепи присутствуют, но ledger не является построчным индексом всех 40 разделов | **GREEN canon / YELLOW corpus** |
| Состояние Асгара | `ASGAR_STATE_LEDGER.md` | 1–35 + I–V покрыты | полный chapter pass нужен после rewrite | **GREEN coverage / YELLOW implementation** |
| Foreshadow/payoff | `FORESHADOWING_PAYOFF_LEDGER.md` | reveal/final canon согласованы | финальная петля и мужчина 2014 совместимы | **GREEN structural / YELLOW prose** |
| Decision logic | `DECISION_MOTIVATION_CANON.md` | motivation/flaw/chapter canon согласованы | ключевые решения получили человеческую цену | **GREEN structural / YELLOW corpus** |
| Relationship persistence | `RELATIONSHIP_CANON.md` | history/voice/motivation согласованы | Ар/Мара/Катя имеют след в поздних главах | **GREEN canon / YELLOW full audit** |

---

# 8. AUTHORIAL STYLE MATRIX

| Слой | Source | Canon sync | Chapter sync | Статус |
|---|---|---:|---:|---|
| Narrative mode | `NARRATIVE_STYLE_CANON.md` | PASS | не все главы переписаны | **YELLOW** |
| Уникальный метод «Проза причинного эха» | `CANON_AUTHOR_STYLE_V3.md` | зарегистрирован в manifest, authoring, audit, memory | создан после исходного v2 корпуса | **YELLOW until rewrite** |
| Prose/dialogue | `PROSE_DIALOGUE_CANON.md` | PASS | не все главы rebuilt from scene logic | **YELLOW** |
| Reader experience | `READER_EXPERIENCE_CANON.md` | PASS | требует line-level experience pass | **YELLOW** |
| Writing tics | `CANON_WRITING_TICS.md` | causal-echo anti-tics добавлены | corpus-wide final scan ещё нужен | **YELLOW** |
| Terminology | `TERMINOLOGY_CANON.md` | reveal/knowledge согласованы | основные эмбарго проходят структурные тесты | **GREEN structural / YELLOW full scan** |

Главный вывод: **авторский ДНК уже герметично закреплён в системе, но ещё не может считаться герметично реализованным в романе, пока остаются v2-identical главы.**

---

# 9. CHAPTER CORPUS MATRIX

Правило сертификации:
- byte-identical с `chapters_v2/` → **RED / REWRITE REQUIRED**;
- отличается от v2 → **YELLOW / CHANGED OR PATCHED**, пока нет доказанного полного rewrite + chapter audit;
- GREEN выдаётся только после полного v3 rewrite и чистого chapter audit по FULL CANON STACK.

## 9.1. RED — точно не прошли полный V3 rewrite

1. `01-16-avgusta.md`
2. `06-mertvyy-chelovek.md`
3. `09-novaya-klimaticheskaya-epoha.md`
4. `10-krasnyy-koridor.md`
5. `11-ozhidanie.md`
6. `14-mashiny-bez-hozyaev.md`
7. `15-protokol.md`
8. `16-mara.md`
9. `21-nepreryvnost.md`
10. `22a-slepaya-zona.md`
11. `24-milliony-let.md`
12. `25-posledniy-arhiv-zemli.md`
13. `26-odin.md`
14. `27-poslanie.md`
15. `28-smert-zemli.md`
16. `29-poslednie-zvezdy.md`
17. `30a-do-poslednego-okna.md`
18. `31-retro-1.md`
19. `32-vy-pochti-doshli.md`

**19/40 = RED / REWRITE REQUIRED.**

## 9.2. YELLOW — отличаются от v2, но full-rewrite certification не доказан

1. `02-chetyre-dnya.md`
2. `03-sled.md`
3. `04-okno.md`
4. `04a-lishnyaya-massa.md`
5. `05-dvadtsat-pyat-let.md`
6. `07-arhiv-16-08.md`
7. `08-vtoroe-okno.md`
8. `08a-raschet-ne-shoditsya.md`
9. `12-shturm.md`
10. `13-posle-voyny.md`
11. `15a-smena.md`
12. `17-posle-vtorogo-padeniya.md`
13. `18-chelovek-iz-krasnoy-dveri.md`
14. `19-dolgoe-ozhidanie.md`
15. `20-vozrozhdenie.md`
16. `22-ne-domoy.md`
17. `23-istochnik.md`
18. `30-temnaya-epoha.md`
19. `33-tishina.md`
20. `34-liniya-istochnika.md`
21. `35-16-avgusta.md`

**21/40 = YELLOW / CHANGED OR PATCHED.**

## 9.3. GREEN

**0/40 пока не сертифицированы как полный V3 rewrite + clean full-stack audit.**

Это не означает, что 0 глав хороши. Это означает, что матрица запрещает выдавать отсутствие доказательства за PASS.

---

# 10. АВТОМАТИЧЕСКИЕ / СТРУКТУРНЫЕ ПРОВЕРКИ ПО ГЛАВАМ

После sync-pass подтверждено:

- `chapters_v3/`: **40/40** файлов;
- `CHAPTER_BY_CHAPTER_CANON.md`: ссылки ровно на те же **40/40** разделов;
- `PHYSICS_CANON.md`: покрытие глав 1–35 + интерлюдий I–V;
- `ASGAR_STATE_LEDGER.md`: покрытие 1–35 + I–V;
- `KNOWLEDGE_LEDGER.md`: покрытие 1–35 + I–V;
- `RETRO-1` отсутствует в художественных главах до официальной гл.31;
- термин `оператор` отсутствует в основной линии до гл.16;
- Мара не названа в художественной линии до `15a/16`;
- визуального канала Асгар↔Мара не обнаружено;
- служебные ярлыки «молодой/старший Асгар» в финальной художественной прозе удалены;
- старое имя следователя Алиев удалено из актуального конфликтного контура и архивного упоминания;
- Рауф присутствует в 2–5; Кей — I/III; Вар — 17/19/20;
- найденные слова «скамейка» относятся к внешней среде, не к интерьеру RETRO-1.

---

# 11. ЧТО БЫЛО ИСПРАВЛЕНО ЭТИМ SYNC-PASS

1. `FINAL_CANON_OVERRIDE.md`: художественные источники истины переведены с frozen `chapters_v2/` на актуальные `chapters_v3/`.
2. Ранний полицейский Алиев синхронизирован с каноническим Рауфом Керимовым в главах 2–5 и архивном следе главы 7.
3. Кей встроен в интерлюдии I и III как реальный носитель операционного риска.
4. Вар встроен в главы 17, 19, 20 как причинно возникающий социально-процедурный оппонент.
5. Глава 8: восстановлена обязательная полуправда Кате.
6. Глава 22: восстановлен несправедливый удар по Маре и граница Мары.
7. Глава 23: восстановлено неидеальное конкретное извинение.
8. Глава 30: восстановлена эгоистичная рационализация чужого будущего ресурса.
9. Глава 33: восстановлена почти нарушенная автономия сохранённого человека.
10. Глава 35: усилен смешанный мотив молчания и удалены служебные age-labels.
11. `AUTHORING_RULES.md`, `CHAPTER_AUDIT_PROMPT.md`, `NOVEL_FINAL_AUDIT_CHECKLIST.md`: добавлен FULL CANON STACK GATE.
12. `PROJECT_MEMORY/04_HANDOFF_PROMPT.md`: добавлены causal-echo, motivation, antagonism и Asgar flaw canons.
13. `PROJECT_MEMORY/07_V3_NARRATIVE_STYLE.md`: добавлен `CANON_AUTHOR_STYLE_V3.md` и «Проза причинного эха».

---

# 12. ГЕРМЕТИЧНОСТЬ — ФИНАЛЬНЫЙ ВЕРДИКТ

## Canon architecture
**PASS.**

На текущем main не найден активный root-level канон/ledger/служебный markdown, который существует вне индекса `MANIFEST.md`.

Персонажные базовые слои для 24 проверенных повторяющихся фигур замкнуты:
**history → voice → motivation → relationship → knowledge.**

Ключевые конфликтные дуги замкнуты:
**history → motivation → voice → relationship → knowledge → chapter contract → prose presence.**

Ключевые финальные правила замкнуты:
**physics → final override → reveal → knowledge → staging → chapter 34/35.**

## Artistic corpus
**NOT YET PASS.**

Причина одна, но фундаментальная: V3 по собственному манифесту обязан быть полным rewrite, а:
- **19/40** файлов всё ещё идентичны v2;
- **21/40** отличаются от v2, но не имеют формального доказательства полного rewrite + clean full-stack audit.

Следовательно, роман **нельзя честно объявить полностью герметичным или release-ready**, пока все 40 разделов не получат chapter-level GREEN.

---

# 13. УСЛОВИЕ GREEN ДЛЯ КАЖДОЙ ГЛАВЫ

Глава получает GREEN только если одновременно:

1. переписана как v3, а не просто пропатчена;
2. выполняет `CHAPTER_BY_CHAPTER_CANON.md`;
3. knowledge/reveal чисты;
4. physics/hard-scene/epoch capability чисты;
5. staging и язык физически объяснимы;
6. состояние Асгара совпадает с ledger;
7. решения имеют причинную мотивацию;
8. flaw arc не потерян;
9. каждый значимый персонаж действует из собственной мотивации;
10. voice соответствует профилю;
11. relationship state не сброшен;
12. conflict/antagonism не сценарный;
13. cause→effect оплачены;
14. foreshadow/payoff честны;
15. `CANON_AUTHOR_STYLE_V3.md` реализован без STYLE TIC;
16. проза/диалоги/POV/проживаемость проходят;
17. запрещённые тики отсутствуют;
18. выход главы герметично совпадает со входом следующей.

До выполнения всех 18 пунктов статус не GREEN.
