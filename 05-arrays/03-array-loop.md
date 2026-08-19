<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 5.3 cyklus přes pole.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 5 — Data řídí kreslení
@JSQ.world(5, Arrays)
## EXPERIMENT
```js
const heights = [40, 90, 60, 130, 75];
p5.setup = function () {
  p5.createCanvas(600, 300);
};
p5.draw = function () {
  p5.background(245);
  for (let i = 0; i < heights.length; i += 1) {
    p5.rect(40 + i * 100, 260 - heights[i], 60, heights[i]);
  }
};
```
@P5.eval
## LEARN
Cyklus přes pole propojuje dvě známé myšlenky: `i` určuje pořadí průchodu a zároveň vybírá hodnotu na stejné pozici v poli.

```js
for (let i = 0; i < heights.length; i += 1) {
  const height = heights[i];
  p5.rect(40 + i * 100, 260 - height, 60, height);
}
```

Hranice `i < heights.length` se přizpůsobí počtu dat, takže nečteme neexistující položku. V prvním průchodu je `i` 0 a `height` je 40, v dalším je `i` 1 a vybere se 90. Kdybychom napsali `i <= heights.length`, poslední průchod by hledal položku za koncem pole.
## QUICK QUIZ
@JSQ.quiz
> **⚡ QUICK QUIZ** @JSQ.xp(1)
> Která hranice projde všemi prvky `values`?
[(X)] `i < values.length`
[( )] `i <= values.length`
[( )] `i < 0`
[( )] `values < i`
## MISSION
@JSQ.mission
> **🎯 MISSION: DATOVÝ GRAF** @JSQ.xp(4)
> Zobraz všechna data jako sloupce. Změň pole a sleduj, že se graf automaticky přizpůsobí.
```js
const data = [30, 120, 80, 160, 60];
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  // TODO: Projdi celé pole pomocí for a length.
  // TODO: Použij data[i] jako výšku sloupce.
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Index začíná na 0 a končí před `data.length`.</details>
@JSQ.flag
> @JSQ.buildflag
> Dokážu propojit cyklus s polem a vytvořit datový graf.
