<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 3.2 index a grafika.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 3 — Počítadlo jako souřadnice
@JSQ.world(3, Loops)
## PREDICT
@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
> Jaká je poslední hodnota `i` uvnitř `i < 4`?
[( )] 4
[(X)] 3
[( )] 5
[( )] -1
## EXPERIMENT
```js
p5.setup = function () {
  p5.createCanvas(600, 300);
};

p5.draw = function () {
  p5.background(245);
  for (let i = 0; i < 12; i += 1) {
    p5.rect(i * 50, 100, 35, i * 8);
  }
};
```
@P5.eval
## LEARN — Index jako vstup pro kreslení
Počítadlo `i` není jen počet opakování. V každém průchodu má jinou hodnotu, a proto může řídit vlastnost právě kresleného prvku.

```js
for (let i = 0; i < 12; i += 1) {
  const x = i * 50;
  const height = i * 8;
  p5.rect(x, 100, 35, height);
}
```

Když je `i` nula, první obdélník začíná na x = 0 a má výšku 0. S každým dalším průchodem se obě hodnoty zvětší. Tento vztah mezi indexem a grafikou je důvod, proč cyklus neumí jen kopírovat stejný tvar, ale vytvářet schody, graf nebo ornament.
## MISSION
@JSQ.mission
> **🎯 MISSION: SCHODIŠTĚ** @JSQ.xp(4)
> Vytvoř deset schodů, jejichž výška roste s pořadím.
```js
p5.setup = function () {
  p5.createCanvas(600, 300);
};

p5.draw = function () {
  p5.background(245);
  // TODO: Opakuj kreslení schodu.
  // TODO: Spoj index s výškou.
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Index může určovat x i výšku.</details>
## QUICK QUIZ
@JSQ.quiz
> **⚡ QUICK QUIZ** @JSQ.xp(1)
> Co je výhodou indexu?
[(X)] dovolí každému průchodu jinou hodnotu
[( )] zastaví draw
[( )] nahradí canvas
[( )] vždy je nulový
@JSQ.flag
> @JSQ.thinkflag
> Dokážu předpovědět hodnotu počítadla.
