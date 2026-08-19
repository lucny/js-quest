<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 3.5 Boss generativní pattern.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 3 — Pattern Machine
@JSQ.world(3, Loops)
## BOSS — Generative Grid
@JSQ.boss
> **🏆 BOSS: PATTERN MACHINE** @JSQ.xp(10)
> Navrhni vlastní pravidelný ornament. Použij vnořené cykly, indexy řady i sloupce a alespoň jednu vlastnost závislou na indexu.
```js
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  // TODO: Navrhni počet řad a sloupců.
  // TODO: Opakuj kreslení tvaru ve dvou směrech.
  // TODO: Nech index ovlivnit barvu, velikost nebo tvar.
};
```
@P5.eval
<details><summary>Nápověda 1</summary>Nejdřív vytvoř pravidelnou mřížku.</details>
<details><summary>Nápověda 2</summary>Pro změnu vlastnosti můžeš použít součet nebo rozdíl indexů.</details>
<details><summary>Jedna varianta</summary>Neexistuje jediné správné řešení; zkontroluj, že obrazec používá oba cykly.</details>
## FLAGS
@JSQ.flag
> @JSQ.worldflag
> Dokážu pomocí cyklů vytvořit pravidelnou mřížku a předpovědět počet iterací.
