<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 6.3 metoda a pole objektů.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 6 — Co entita umí
@JSQ.world(6, Objects)
## LEARN
Funkce uložená v objektu je metoda. Může měnit vlastní properties přes `this`.
```js
const bot = { x: 50, speed: 2, move() { this.x += this.speed; } };
```
## PREDICT
@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
> Co změní `bot.move()`?
[(X)] property `bot.x`
[( )] název objektu
[( )] všechny objekty automaticky
[( )] délku pole
## COMPLETE CODE
@JSQ.complete
> **🔧 COMPLETE CODE** @JSQ.xp(2)
> Doplň volání metody v cyklu.
```js
for (let i = 0; i < bots.length; i += 1) { // TODO: nech aktuálního bota vykonat move. }
```
## MISSION
@JSQ.mission
> **🎯 MISSION: MALÁ FLOTILA** @JSQ.xp(4)
> Vytvoř pole dvou objektů. Každý se má pohybovat vlastní rychlostí.
```js
const bots = [
  { x: 80, y: 100, speed: 2, size: 30 },
  { x: 500, y: 200, speed: -3, size: 45 }
];
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  // TODO: Projdi pole objektů.
  // TODO: Změň a vykresli properties každého objektu.
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Cyklus dá každému průchodu jeden objekt: `const bot = bots[i]`.</details>
@JSQ.flag
> @JSQ.thinkflag
> Dokážu rozlišit data entity, její metodu a pole entit.
