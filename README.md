# JS Quest

> Interaktivní výprava do základů JavaScriptu.

JS Quest je experimentální výukový kurz JavaScriptu postavený na krátkých programátorských úkolech. Student nejprve předpovídá chování programu, potom experimentuje, vysvětluje pozorování, upravuje kód a hledá chyby.

Kurz používá [LiaScript](https://liascript.github.io/) a tam, kde je to užitečné, [p5.js](https://p5js.org/) pro okamžitou vizualizaci výsledků.

## Obsah repozitáře

- `01-variables/01-moving-ball.md` — pilotní lekce WORLD 1 o proměnných, stavu programu a operátorech; výsledkem je pohybující se kulička v p5.js.
- `GAME-DESIGN.md` — herní a didaktický návrh kurzu.
- `GAME-MACROS.md` — společná makra a vizuální komponenty pro lekce.
- `AUTHORING-GUIDE.md` — pravidla a doporučení pro tvorbu dalších lekcí.

## Náhled lekce

Lekci lze otevřít v [LiaScript Live Editoru](https://liascript.github.io/LiveEditor/):

1. otevři soubor `01-variables/01-moving-ball.md`,
2. zkopíruj jeho obsah do editoru,
3. spusť náhled a vyzkoušej interaktivní bloky i p5.js ukázky.

Pro publikování lekce stačí zpřístupnit Markdown soubor přes veřejnou URL. Import p5.js šablony je uveden přímo v hlavičce lekce.

## Stav projektu

Projekt je ve fázi pilotu (`v0.1`). XP a vlajky jsou zatím motivační a didaktická metadata; persistentní ukládání výsledků není součástí této verze.

## Tvorba dalších lekcí

Při rozšiřování projektu postupuj podle `AUTHORING-GUIDE.md` a používej makra z `GAME-MACROS.md`. Doporučený průběh lekce je:

`ENTRY` → `PREDICT` → `EXPERIMENT` → `LEARN` → `TRAINING` → `BUG HUNT` → `MISSION` → `PROOF OF UNDERSTANDING` → `FLAGS`

Každá lekce by měla obsahovat editovatelný kód, alespoň jeden debuggingový moment a jasné oddělení povinné části od dobrovolného `SIDE QUEST`.

## Licence

Licence projektu zatím nebyla určena.
