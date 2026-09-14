# V3 PROMPT COVERAGE MATRIX

Для каждого из 40 individual prompts встроены:
- идентичность/путь/позиция в последовательности;
- source commit и source-change gate;
- обязательный canon stack;
- точные локальные sections;
- входное состояние и обязательный state/knowledge/staging receipt;
- цель, препятствие, выбор, цена и reader experience;
- конкретная цепочка событий/причинности;
- knowledge/reveal firewall;
- character/voice/motivation gate;
- physics/staging/language gate;
- reaction/lived-experience gate;
- prose/dialogue/tics gate;
- локальные запреты;
- выходное состояние;
- полный 7-stage protocol write→audit→fix→re-audit→Git/logs→full display→STOP.

| Эпизоды | Contract | Architecture | Knowledge | State | Physics/Staging | Reveal/Foreshadow | Characters/Voices | Full protocol | Auto-next forbidden |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1–35 + I–V | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

Наличие ✓ означает, что prompt требует конкретный локальный section + обязательный полный source; это НЕ означает автоматический prose PASS существующих файлов.
