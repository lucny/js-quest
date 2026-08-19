<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 9.3 Minimum viable program.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 9 — Nejmenší funkční verze
@JSQ.world(9, Final Quest)

## PROBLÉM

Nejdřív vytvoř jeden malý funkční průchod: vstup nebo automatická změna → pravidlo → viditelný výsledek. Teprve pak rozšiřuj.

## PREDICT
@JSQ.predict
> Které dvě věci musí MVP sběratelské hry ukázat jako první: dekorace, nebo hráče a cíl?

## MISSION
@JSQ.mission
> **MISSION: MVP SBĚRU** @JSQ.xp(7)
> Výchozí hra ukáže hráče, cíl a skóre. Doplň pohyb šipkami a pravidlo pro získání bodu. Neřeš ještě vzhled, menu ani více úrovní.

```js
const player = { x: 80, y: 150, speed: 4, size: 28 };
const target = { x: 500, y: 150, size: 24 };
let score = 0;

function movePlayer() {
  // TODO: Změň player.x nebo player.y podle stisknutých šipek.
}

function collectTarget() {
  // TODO: Rozhodni, zda se hráč dostal k cíli, a změň score.
}

p5.setup = function () {
  p5.createCanvas(620, 300);
};

p5.draw = function () {
  p5.background(240, 253, 250);
  movePlayer();
  collectTarget();
  p5.fill(20, 83, 45);
  p5.circle(player.x, player.y, player.size);
  p5.fill(220, 38, 38);
  p5.circle(target.x, target.y, target.size);
  p5.fill(17, 24, 39);
  p5.textSize(20);
  p5.text(`Skóre: ${score}`, 20, 30);
};
```
@P5.eval

<details><summary>Nápověda 1</summary>Vyber nejdřív jeden směr pohybu a ověř jej před přidáním ostatních.</details>
<details><summary>Nápověda 2</summary>Pro jednoduchý sběr stačí porovnat rozdíly x a y s malým prahem.</details>
<details><summary>Možné řešení</summary>Existuje více variant pohybu i zásahu. MVP je hotové, když hráč umí změnit stav a vidí důsledek.</details>

## BONUS
@JSQ.bonus
> Teprve po funkčním MVP přidej jednu drobnost: nový cíl po získání bodu, limit času nebo změnu barvy.

@JSQ.flag
> @JSQ.buildflag
> Dokážu oddělit nezbytné jádro programu od pozdějších rozšíření.
