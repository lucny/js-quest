<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 9.4 Debugging Final Questu.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 9 — Debuguj jako autor
@JSQ.world(9, Final Quest)

## PROBLÉM

Chyba není důkaz, že projekt selhal. Je to informace: co jsem čekal, co se skutečně stalo a ve které části programu se liší?

## BUG HUNT
@JSQ.bug
> **BUG HUNT: PŘÍLIŠ RYCHLÉ SKÓRE** @JSQ.xp(5)
> Skóre roste rychle, i když uživatel jednou podrží tlačítko myši. Vysvětli proč a navrhni opravu podle toho, zda chceš reagovat na jeden klik, nebo na každý snímek.

```js
let score = 0;

p5.setup = function () {
  p5.createCanvas(520, 220);
};

p5.draw = function () {
  p5.background(254, 242, 242);
  if (p5.mouseIsPressed) {
    score = score + 1;
  }
  p5.textSize(24);
  p5.text(`Skóre: ${score}`, 30, 60);
};
```
@P5.eval

<details><summary>Nápověda 1</summary><code>draw</code> běží opakovaně, ne jednou za kliknutí.</details>
<details><summary>Nápověda 2</summary>Pro jediný klik lze použít událost <code>p5.mousePressed</code>.</details>
<details><summary>Možné řešení</summary>Přesuň změnu skóre do <code>p5.mousePressed = function () { ... };</code>, pokud chceš jeden bod za klik.</details>

## DEBUGOVACÍ POSTUP

- Popiš očekávané chování jednou větou.
- Zopakuj chybu co nejmenším počtem kroků.
- Zjisti, která proměnná nebo funkce se mění neočekávaně.
- Přidej dočasný `console.log` nebo jednoduchý výpis hodnoty.
- Oprav jednu hypotézu a znovu otestuj celý malý průchod.
- Teprve potom smaž dočasný výpis a pojmenuj, co bylo příčinou.

## QUICK QUIZ
@JSQ.quiz
> Co je nejlepší první reakce na chybu?

[( )] Přepsat celý program od začátku.
[(X)] Zmenšit situaci, popsat očekávání a ověřit jednu hypotézu.
[( )] Přidat více funkcí, aby chyba nebyla vidět.

@JSQ.flag
> @JSQ.thinkflag
> Dokážu formulovat hypotézu o chybě a ověřit ji malým experimentem.
