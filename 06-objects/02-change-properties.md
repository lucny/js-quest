<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 6.2 změna property.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 6 — Entita mění stav
@JSQ.world(6, Objects)
## EXPERIMENT
```js
const ship = { x: 80, y: 150, speed: 3, size: 40 };
p5.setup = function () {
  p5.createCanvas(600, 300);
};
p5.draw = function () {
  p5.background(245);
  ship.x += ship.speed;
  p5.circle(ship.x, ship.y, ship.size);
};
```
@P5.eval
## LEARN — Property je část stavu entity
Objekt není neměnná kartička s údaji. Jednotlivé properties můžeme číst i měnit, takže objekt drží aktuální stav jedné entity.

```js
ship.x += ship.speed;
```

Pravá strana nejdřív přečte současné `ship.x` a `ship.speed`. Výsledek se pak uloží zpět do property `ship.x`. Zápis `ship.x + ship.speed` by hodnotu jen spočítal a zahodil. Tečka proto patří na obou stranách: čteme i měníme údaje stejné lodi.
## BUG HUNT
@JSQ.bug
> **🐞 BUG HUNT** @JSQ.xp(2)
> Proč se loď neposouvá?
```js
ship.x + ship.speed;
```
<details><summary>Řešení</summary>Změna property potřebuje `ship.x += ship.speed`.</details>
## MISSION
@JSQ.mission
> **🎯 MISSION: POHYBUJÍCÍ SE ENTITA** @JSQ.xp(4)
> Rozšiř objekt o rychlost a změň jeho polohu v každém snímku.
```js
const ship = { x: 80, y: 150, speed: 3, size: 40 };
p5.setup = function () {
  p5.createCanvas(600, 300);
};
p5.draw = function () {
  p5.background(245);
  // TODO: Změň property polohy podle property rychlosti.
  p5.circle(ship.x, ship.y, ship.size);
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Obě hodnoty patří objektu `ship`.</details>
@JSQ.flag
> @JSQ.buildflag
> Dokážu měnit stav entity přes její properties.
