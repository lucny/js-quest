<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 7.1 pozice myši.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 7 — Program vnímá myš
@JSQ.world(7, Interaction)
## ENTRY
```js
p5.setup = function () {
  p5.createCanvas(600, 300);
};
p5.draw = function () {
  p5.background(245);
  p5.circle(p5.mouseX, p5.mouseY, 35);
};
```
@P5.eval
Kruh už nemá pevnou polohu. Jakou hodnotu používá?
## LEARN — Vstup místo pevné hodnoty
`p5.mouseX` a `p5.mouseY` jsou aktuální souřadnice ukazatele uvnitř canvasu. Program je při každém průchodu `draw()` znovu přečte, a proto kruh následuje myš bez vlastního pohybového cyklu.

```js
p5.circle(p5.mouseX, p5.mouseY, 35);
```

První argument určuje vodorovnou polohu, druhý svislou. Jsou to vstupy od člověka, podobně jako dříve byla `x` a `y` data objektu. Mimo canvas nemusí hodnoty odpovídat očekávané herní oblasti, proto budeme u složitějších úloh chránit stav podmínkami.
## PREDICT
@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
> Co určuje `p5.mouseX`?
[(X)] vodorovnou polohu myši v canvasu
[( )] rychlost myši
[( )] počet kliknutí
[( )] výšku canvasu
## MISSION
@JSQ.mission
> **🎯 MISSION: SVĚTLO MYŠI** @JSQ.xp(4)
> Vytvoř světlo, které následuje kurzor a mění velikost podle jeho svislé polohy.
```js
p5.setup = function () {
  p5.createCanvas(600, 300);
};
p5.draw = function () {
  p5.background(30);
  // TODO: Použij mouseX a mouseY pro polohu světla.
  // TODO: Odvoď velikost z jedné hodnoty myši.
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Myš poskytuje dvě číselné values, stejně jako x a y objektu.</details>
@JSQ.flag
> @JSQ.codeflag
> Umím použít polohu myši jako vstup programu.
