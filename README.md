# JS Quest

JS Quest je pilotní interaktivní kurz základů JavaScriptu pro začínající středoškolské studenty. Staví na krátkých programátorských problémech: předpověď, experiment, vysvětlení, úprava kódu a samostatné použití principu.

Technologie: [LiaScript](https://liascript.github.io/) pro interaktivní Markdown, kvízy a editovatelný kód; [p5.js](https://p5js.org/) pro přirozené vizualizace programového stavu. XP a vlajky jsou v pilotu pouze didaktická metadata, ne známky ani persistentní skóre.

## Struktura

- [COURSE-MAP.md](COURSE-MAP.md) — přehled WORLD 1 — Variables a WORLD 2 — Decisions.
- [01-variables/01-moving-ball.md](01-variables/01-moving-ball.md) — WORLD 1: proměnné, přiřazení, rychlost a pohyb.
- [02-decisions/01-boolean-questions.md](02-decisions/01-boolean-questions.md) — WORLD 2: booleanové výrazy, `if`, logické operátory, odrazy a zóny.
- [GAME-DESIGN.md](GAME-DESIGN.md) — didaktický a herní návrh.
- [GAME-MACROS.md](GAME-MACROS.md) — společná LiaScript makra a vzhled aktivit.
- [AUTHORING-GUIDE.md](AUTHORING-GUIDE.md) — pravidla pro nové lekce.
- [AGENTS.md](AGENTS.md) — trvalé pokyny pro automatizovanou práci na projektu.

## Otevření pilotu

Po pushi větve `experimental/pilot` otevři tento odkaz v prohlížeči:

```text
https://liascript.github.io/course/?https://raw.githubusercontent.com/lucny/js-quest/experimental/pilot/01-variables/01-moving-ball.md
```

LiaScript načte p5js template i společná makra přes importy z hlavní hlavičky lekce. Pro rychlé úpravy lze použít také [LiaScript Live Editor](https://liascript.github.io/LiveEditor/).

## Validace

Vyžaduje Python 3.11+ a nepřidává žádné závislosti:

```powershell
python tools/validate_course.py
git diff --check
```

Validátor kontroluje povinné soubory, UTF-8, code fences, hlavičky a importy, sadu `@JSQ` maker, párování karet, označení WORLD, zakázané task/quiz konstrukce a lokální odkazy. Nenahrazuje render LiaScriptu ani manuální ověření interakce p5.js.

## Nová lekce

Začni v [AUTHORING-GUIDE.md](AUTHORING-GUIDE.md), používej makra z [GAME-MACROS.md](GAME-MACROS.md) a před předáním spusť validaci. Společný CSS/HTML kód nepatří do jednotlivých lekcí.
