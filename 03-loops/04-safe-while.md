<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 3.4 while a bezpečné ukončení cyklu.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 3 — Kdy opakování skončí?
@JSQ.world(3, Loops)
## BUG HUNT — Nekonečné počítání
@JSQ.bug
> **🐞 BUG HUNT** @JSQ.xp(2)
> Proč se `while` nikdy nezastaví?
```js
let i = 0;
while (i < 5) {
  console.log(i);
}
```
<details><summary>Řešení</summary>V těle chybí změna `i += 1`.</details>
## LEARN
`while` opakuje tělo, dokud je jeho otázka `true`. Proto musí existovat cesta, jak ji změnit na `false`.
## MISSION
@JSQ.mission
> **🎯 MISSION: BEZPEČNÝ ODPOČET** @JSQ.xp(3)
> Zobraz na canvasu hodnoty 5 až 1 pomocí bezpečně ukončeného `while`.
```js
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  let value = 5;
  // TODO: Opakuj, dokud je value kladné.
  // TODO: V každém průchodu value změň, aby cyklus skončil.
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Otázka může být o `value > 0`; změna musí být uvnitř těla.</details>
## QUICK QUIZ
@JSQ.quiz
> **⚡ QUICK QUIZ** @JSQ.xp(1)
> Co musí mít bezpečný `while`?
[(X)] změnu, která jednou ukončí podmínku
[( )] vždy canvas
[( )] dva vnořené cykly
[( )] pouze `else`
@JSQ.flag
> @JSQ.thinkflag
> Dokážu najít riziko nekonečné smyčky.
