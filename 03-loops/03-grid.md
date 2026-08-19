<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 3.3 vnořené cykly a mřížka.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 3 — Mřížka ze dvou opakování
@JSQ.world(3, Loops)
## ENTRY — Řady nestačí
Jedna smyčka nakreslí řadu. Jak nakreslíme několik řad pod sebe?
@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
> Kolik kruhů nakreslí dva cykly po třech průchodech?
[( )] 6
[(X)] 9
[( )] 3
[( )] 12
## EXPERIMENT
```js
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  for (let row = 0; row < 4; row += 1) {
    for (let column = 0; column < 8; column += 1) {
      p5.circle(45 + column * 70, 45 + row * 70, 24);
    }
  }
};
```
@P5.eval
## LEARN
Vnější cyklus vybírá řadu, vnitřní sloupec. Vnitřní cyklus se dokončí při každé nové řadě.
## COMPLETE CODE
@JSQ.complete
> **🔧 COMPLETE CODE** @JSQ.xp(2)
> Doplň druhý cyklus, aby se vedle sebe vykreslilo šest čtverců.
```js
for (let row = 0; row < 3; row += 1) {
  // TODO: Opakuj kreslení šesti sloupců.
}
```
## MISSION
@JSQ.mission
> **🎯 MISSION: PIXELOVÝ MOTIV** @JSQ.xp(4)
> Vytvoř mřížku 8 × 4 a podle kombinace řady a sloupce změň velikost nebo barvu některých prvků.
```js
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  // TODO: Vytvoř vnější cyklus pro řady.
  // TODO: Vytvoř vnitřní cyklus pro sloupce.
  // TODO: Propoj indexy s jednou vizuální vlastností.
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Začni stejnou mřížkou kruhů; potom změň pouze jednu vlastnost.</details>
@JSQ.flag
> @JSQ.buildflag
> Dokážu použít vnořené cykly pro pravidelnou mřížku.
