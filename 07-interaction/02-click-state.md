<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 7.2 kliknutí a stav.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 7 — Kliknutí mění stav
@JSQ.world(7, Interaction)
## EXPERIMENT
```js
let active = false;
p5.setup = function () { p5.createCanvas(600, 300); };
p5.mousePressed = function () { active = !active; };
p5.draw = function () { p5.background(245); if (active) { p5.fill(40, 180, 80); } else { p5.fill(90); } p5.circle(300, 150, 90); };
```
@P5.eval
## LEARN
Událost `mousePressed` se spustí při kliknutí. Proměnná `active` uchovává stav mezi událostmi.
## BUG HUNT
@JSQ.bug
> **🐞 BUG HUNT** @JSQ.xp(2)
> Proč se stav nikdy nezmění?
```js
p5.mousePressed = function () { active = active; };
```
<details><summary>Řešení</summary>Pro přepnutí booleanu použij `active = !active`.</details>
## MISSION
@JSQ.mission
> **🎯 MISSION: PŘEPÍNAČ BARVY** @JSQ.xp(4)
> Kliknutím přepínej dvě barvy a zobraz aktuální stav jako text.
```js
let active = false;
p5.setup = function () { p5.createCanvas(600, 300); };
p5.mousePressed = function () { /* TODO: změň stav. */ };
p5.draw = function () { p5.background(245); p5.fill(90); p5.circle(300, 150, 90); // TODO: Reaguj na stav při kreslení. };
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Boolean lze obrátit vykřičníkem.</details>
@JSQ.flag
> @JSQ.thinkflag
> Dokážu vysvětlit, jak událost mění stav programu.
