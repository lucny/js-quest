# JS Quest

JS Quest je interaktivní kurz základů JavaScriptu pro začínající středoškoláky. Vede od proměnných k samostatnému programu skrze předpovědi, malé experimenty, debugging a editovatelný kód. XP a vlajky jsou motivace a kompetenční orientace — nejsou známka.

## Pro studenta

Začni v [COURSE-MAP.md](COURSE-MAP.md) a otevři první lekci WORLD 1. Postupuj po WORLD ech; Bonus a [Arena aktivity](ARENAS.md) jsou dobrovolné. Final Quest ve WORLD 9 je příležitost vytvořit vlastní malý program.

## Technologie a spuštění

Kurz používá [LiaScript](https://liascript.github.io/), [p5.js](https://p5js.org/) pro vizualizace a oficiální LiaScript WebDev template pro WORLD 8. Po publikování větve otevři lekci v LiaScript Preview:

```text
https://liascript.github.io/course/?https://raw.githubusercontent.com/lucny/js-quest/experimental/course-polish/01-variables/01-moving-ball.md
```

P5 lekce běží v instance mode s prefixem `p5.`. Web/DOM lekce používají `@WebDev.HTML_JS`; jejich HTML a JavaScript se vykreslují společně v oficiálním template.

## Struktura

- WORLD 1 — Variables
- WORLD 2 — Decisions
- WORLD 3 — Loops
- WORLD 4 — Functions
- WORLD 5 — Arrays
- WORLD 6 — Objects
- WORLD 7 — Interaction
- WORLD 8 — Web / DOM
- WORLD 9 — Final Quest

Úplný seznam lekcí je v [COURSE-MAP.md](COURSE-MAP.md). Didaktická pravidla a společná makra jsou v [GAME-DESIGN.md](GAME-DESIGN.md) a [GAME-MACROS.md](GAME-MACROS.md).

## Validace

Vyžaduje Python 3.11+ bez dalších závislostí:

```powershell
python tools/validate_course.py
python tools/course_metrics.py
git diff --check
```

Pro upravenou lekci spusť i oficiální LiaScript Exporter:

```powershell
npx --yes @liascript/exporter -i 08-web/01-html-dom.md -p . -f json -o .tmp/lesson
```

Automatické kontroly nenahrazují manuální Preview; použij [COURSE-TEST.md](COURSE-TEST.md).

## Pro autora

Začni v [AUTHORING-GUIDE.md](AUTHORING-GUIDE.md), zachovej globální makra a nevkládej CSS ani `font-family` do lekce. Mission musí mít editor, funkční výchozí scaffold a 1–3 TODO. Používej pouze single-choice kvízy `[( )]` / `[(X)]`, pomoc ve `details` a nikdy syntax `[[...]]` ani LiaScript Task listy.

Před commitem proveď validaci, Exporter, regresní search a `git diff --check`. Učitelský postup shrnuje [TEACHER-GUIDE.md](TEACHER-GUIDE.md); odpovědi pro učitele jsou v [ANSWER-GUIDE.md](ANSWER-GUIDE.md).
