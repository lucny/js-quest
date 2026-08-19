<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 5.4 push a rostoucí data.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 5 — Přidáváme nová data
@JSQ.world(5, Arrays)
## LEARN
`push` přidá jednu hodnotu na konec existujícího pole. Hodí se pro historii hodů, zpráv nebo naměřených hodnot, když data přibývají až během programu.

```js
const rolls = [2, 5];
rolls.push(4);
```

Po zavolání obsahuje pole tři hodnoty: `[2, 5, 4]`. Slovo `push` je metoda pole, proto za ním patří závorky s hodnotou, kterou chceme přidat. Samotné `rolls.push` nic neprovede. Když hodnoty přidáváme opakovaně, kontrolujeme také `rolls.length`, aby historie nerostla bez omezení.
## BUG HUNT
@JSQ.bug
> **🐞 BUG HUNT** @JSQ.xp(2)
> Proč tento kód nic nepřidá?
```js
const rolls = [2, 5];
rolls.push;
```
<details><summary>Řešení</summary>`push` je metoda a potřebuje závorky i hodnotu: `rolls.push(4)`.</details>
## MISSION
@JSQ.mission
> **🎯 MISSION: HISTORIE HODŮ** @JSQ.xp(4)
> V každém průchodu přidej do pole jednu hodnotu, ale udrž historii nejvýše deset položek a zobraz její délku.
```js
const rolls = [];
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  // TODO: Přidej do pole bezpečnou ukázkovou hodnotu.
  // TODO: Zobraz aktuální length; nenech historii nekonečně růst.
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Nejdřív vyzkoušej `push`; limit můžeš kontrolovat podmínkou.</details>
@JSQ.flag
> @JSQ.codeflag
> Umím přidat hodnotu na konec pole pomocí `push`.
