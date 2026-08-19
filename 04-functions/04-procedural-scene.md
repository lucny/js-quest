<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 4.4 Boss procedurální scéna.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 4 — Procedural Scene
@JSQ.world(4, Functions)
## BOSS
@JSQ.boss
> **🏆 BOSS: PROCEDURAL SCENE** @JSQ.xp(10)
> Navrhni scénu alespoň ze dvou vlastních funkcí. Jedna musí používat nejméně dva parametry a jedna může vracet výpočet pro další kreslení.
```js
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  // TODO: Navrhni pojmenované části své scény.
  // TODO: Použij parametry pro jejich různé varianty.
};
```
@P5.eval
<details><summary>Nápověda 1</summary>Rozděl scénu na opakující se části.</details>
<details><summary>Nápověda 2</summary>Parametry mohou určovat polohu, velikost nebo barvu.</details>
<details><summary>Řešení</summary>Existuje více správných scén; ověř, že funkce skutečně snižují opakování.</details>
## FLAGS
@JSQ.flag
> @JSQ.worldflag
> Dokážu rozdělit opakovaný program na pojmenované parametrické funkce.
