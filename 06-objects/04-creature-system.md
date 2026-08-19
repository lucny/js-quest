<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 6.4 Boss systém objektů.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 6 — Creature System
@JSQ.world(6, Objects)
## BOSS
@JSQ.boss
> **🏆 BOSS: CREATURE SYSTEM** @JSQ.xp(10)
> Vytvoř scénu alespoň se třemi entitami. Každá má polohu, rychlost a velikost; cyklus je pohybuje a vykreslí. Přidej jednoduchou reakci na hranici.
```js
const creatures = [
  { x: 80, y: 100, speed: 2, size: 30 },
  { x: 240, y: 170, speed: -2, size: 45 },
  { x: 440, y: 130, speed: 3, size: 25 }
];
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  // TODO: Projdi creatures a aktualizuj každou entitu.
  // TODO: Když entita opustí hranici, změň její rychlost.
};
```
@P5.eval
<details><summary>Nápověda</summary>Pracuj vždy s jednou entitou z pole a jejími properties.</details>
@JSQ.flag
> @JSQ.worldflag
> Dokážu modelovat více entit jako pole objektů.
