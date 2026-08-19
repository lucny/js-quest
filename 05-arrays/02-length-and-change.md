<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 5.2 length a změna prvku.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 5 — Kolik hodnot máme?
@JSQ.world(5, Arrays)
## PREDICT
@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
> Jakou hodnotu má `[4, 7, 9].length`?
[( )] 2
[(X)] 3
[( )] 9
[( )] undefined
## LEARN — Počet a poslední pozice
`length` říká, kolik položek pole obsahuje. Neříká ale číslo poslední pozice, protože indexy začínají nulou.

```js
const scores = [10, 12, 18];
const count = scores.length;
const lastIndex = scores.length - 1;
```

Zde je `count` 3, ale poslední platný index je 2. Zápis `scores[1] = 25` změní druhou položku: nejdřív vybereme pozici v hranatých závorkách, potom do ní přiřadíme novou hodnotu. Zaměnění `length` za poslední index je častá chyba off-by-one.
## COMPLETE CODE
@JSQ.complete
> **🔧 COMPLETE CODE** @JSQ.xp(2)
> Změň druhou hodnotu pole na 25.
```js
const scores = [10, 12, 18];
// TODO: změň prvek na druhé pozici.
```
## BUG HUNT
@JSQ.bug
> **🐞 BUG HUNT** @JSQ.xp(2)
> Proč poslední platný index není `scores.length`?
```js
console.log(scores[scores.length]);
```
<details><summary>Řešení</summary>Indexy začínají nulou; poslední je `scores.length - 1`.</details>
## MISSION
@JSQ.mission
> **🎯 MISSION: OPRAVA DAT** @JSQ.xp(4)
> Připrav panel hodnot, změň jeden vybraný prvek a zobraz, kolik hodnot pole obsahuje.
```js
const scores = [10, 12, 18, 7];
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  // TODO: Změň jeden konkrétní prvek pole.
  // TODO: Zobraz počet prvků pomocí length.
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Pro změnu použij přiřazení do `scores[index]`.</details>
@JSQ.flag
> @JSQ.thinkflag
> Dokážu určit platný index a počet prvků pole.
