<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 7.3 klávesnice a ovládání.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 7 — Hráč volí směr
@JSQ.world(7, Interaction)
## EXPERIMENT
```js
let x = 300;
p5.setup = function () {
  p5.createCanvas(600, 300);
};
p5.draw = function () {
  p5.background(245);
  if (p5.keyIsDown(p5.LEFT_ARROW)) {
    x -= 4;
  }
  if (p5.keyIsDown(p5.RIGHT_ARROW)) {
    x += 4;
  }
  p5.circle(x, 150, 40);
};
```
@P5.eval
## LEARN — Klávesa jako průběžný vstup
`p5.keyIsDown(...)` odpovídá na otázku, zda je konkrétní klávesa právě stisknutá. Proto se ptáme uvnitř `draw()`: při držení klávesy se odpověď kontroluje v každém snímku a hráč se pohybuje plynule.

```js
if (p5.keyIsDown(p5.LEFT_ARROW)) {
  x -= 4;
}
```

Podmínka chrání změnu `x`. Když levá šipka není stisknutá, poloha se v tomto snímku nezmění. Pro druhý směr použijeme samostatnou otázku, protože hráč může případně držet více kláves. Předchozí `if` a objektový stav se tu přirozeně spojují s novým vstupem z klávesnice.
## QUICK QUIZ
@JSQ.quiz
> **⚡ QUICK QUIZ** @JSQ.xp(1)
> Kdy se pohne hráč doleva?
[(X)] když je stisknutá levá šipka
[( )] při každém kliknutí
[( )] když je mouseX nula
[( )] nikdy
## MISSION
@JSQ.mission
> **🎯 MISSION: OVLÁDANÝ PRŮZKUMNÍK** @JSQ.xp(4)
> Doplň ovládání oběma osami a udrž hráče uvnitř canvasu.
```js
const player = { x: 300, y: 150, speed: 4, size: 35 };
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  // TODO: Reaguj na šipky a změň x/y hráče.
  // TODO: Použij známé podmínky pro hranice canvasu.
  p5.circle(player.x, player.y, player.size);
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Každá šipka mění jednu property o `player.speed`.</details>
@JSQ.flag
> @JSQ.buildflag
> Dokážu ovládat objekt klávesnicí a chránit ho hranicemi.
