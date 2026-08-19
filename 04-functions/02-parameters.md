<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 4.2 parametry funkcí.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 4 — Funkce dostává údaje
@JSQ.world(4, Functions)
## EXPERIMENT
```js
function drawTarget(x, y, size) {
  p5.circle(x, y, size);
  p5.circle(x, y, size / 2);
}

p5.setup = function () {
  p5.createCanvas(600, 300);
};

p5.draw = function () {
  p5.background(245);
  drawTarget(120, 150, 90);
  drawTarget(400, 120, 50);
};
```
@P5.eval
## LEARN
Bez parametrů kreslí `drawTarget` stále stejný terč. Parametry dovolí stejnému návodu přijmout údaje pro konkrétní použití.

```js
function drawTarget(x, y, size) {
  p5.circle(x, y, size);
}

drawTarget(120, 150, 90);
```

`x`, `y` a `size` v definici jsou **parametry**: dočasná jména, se kterými funkce pracuje uvnitř svého těla. Čísla při volání jsou **argumenty**. Při tomto volání dostane `x` hodnotu 120, `y` hodnotu 150 a `size` hodnotu 90. Další volání může dodat jiné hodnoty, aniž bychom kopírovali funkci. Typická chyba je parametry napsat, ale uvnitř funkce dál používat pevná čísla.
## BUG HUNT
@JSQ.bug
> **🐞 BUG HUNT** @JSQ.xp(2)
> Proč se oba terče vykreslí na stejném místě?
```js
function drawTarget(x, y) {
  p5.circle(100, 100, 50);
}
```
<details><summary>Řešení</summary>Uvnitř funkce použij parametry `x` a `y`.</details>
## MISSION
@JSQ.mission
> **🎯 MISSION: KVĚTINOVÁ TOVÁRNA** @JSQ.xp(4)
> Doplň parametry tak, aby jedna funkce vykreslila květiny na různých místech a ve dvou velikostech.
```js
function drawFlower(x, y, size) {
  // TODO: Použij parametry pro polohu a velikost částí květiny.
}
p5.setup = function () {
  p5.createCanvas(600, 300);
};
p5.draw = function () {
  p5.background(245);
  drawFlower(140, 140, 70);
  drawFlower(420, 170, 45);
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Nejdřív nakresli střed, potom stejné parametry použij pro okvětní lístky.</details>
@JSQ.flag
> @JSQ.buildflag
> Dokážu použít parametry pro více variant stejného tvaru.
