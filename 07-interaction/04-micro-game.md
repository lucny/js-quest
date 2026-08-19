<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 7.4 Boss micro game.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 7 — Micro Game
@JSQ.world(7, Interaction)
## BOSS
@JSQ.boss
> **🏆 BOSS: SBĚRAČ SIGNÁLŮ** @JSQ.xp(10)
> Vytvoř malou hru: hráč se ovládá šipkami, sbírá cíl, skóre se mění a hra má stav start/play/game over nebo dokončeno.
```js
const player = { x: 80, y: 150, speed: 4, size: 30 };
const target = { x: 450, y: 150, size: 25 };
let score = 0;
let playing = true;
p5.setup = function () {
  p5.createCanvas(600, 300);
};
p5.draw = function () {
  p5.background(245);
  // TODO: Ovládej player a zachovej hranice.
  // TODO: Rozhodni, zda hráč dosáhl target, a změň score/stav.
  p5.circle(player.x, player.y, player.size);
  p5.circle(target.x, target.y, target.size);
  p5.text(`Skóre: ${score}`, 20, 30);
};
```
@P5.eval
<details><summary>Nápověda 1</summary>Nejdřív zprovozni pohyb hráče.</details>
<details><summary>Nápověda 2</summary>Pro zásah porovnej vzdálenost x a y s velikostmi objektů.</details>
@JSQ.flag
> @JSQ.worldflag
> Dokážu spojit stav, událost a pravidla do malé interaktivní hry.
