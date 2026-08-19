<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 5.1 pole a index.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 5 — Mnoho hodnot pohromadě
@JSQ.world(5, Arrays)
## ENTRY
Máme uložit deset naměřených hodnot. Deset proměnných by bylo nepřehledných.
```js
const temperatures = [18, 21, 23, 20];
console.log(temperatures[0]);
```
## PREDICT
@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
> Jaká hodnota je na indexu 2 v `[5, 8, 12]`?
[( )] 5
[( )] 8
[(X)] 12
[( )] 2
## LEARN
Pole řeší situaci, kdy spolu souvisí více hodnot stejného druhu. Místo proměnných `temperature1`, `temperature2` a dalších uložíme hodnoty do jednoho uspořádaného celku.

```js
const temperatures = [18, 21, 23, 20];
const firstTemperature = temperatures[0];
```

Hranaté závorky vpravo od názvu pole vybírají jednu pozici. Index 0 znamená první položku, index 1 druhou. Program proto nečte „nultou teplotu“, ale první uloženou hodnotu. Když zkusíš index mimo pole, žádná hodnota na něm není — později se naučíme bezpečnou hranici `length`.
## EXPERIMENT
Změň jednu hodnotu v poli a přečti ji jiným indexem. Co se stane při indexu mimo pole?
## MISSION
@JSQ.mission
> **🎯 MISSION: PANEL MĚŘENÍ** @JSQ.xp(4)
> Ulož pět hodnot do pole a vypiš vybranou hodnotu i její index na canvas.
```js
const values = [12, 18, 9, 24, 16];
const selected = 0;
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  // TODO: Přečti hodnotu na selected.
  // TODO: Zobraz index a hodnotu jako text.
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Pro čtení použij hranaté závorky za názvem pole.</details>
@JSQ.flag
> @JSQ.codeflag
> Umím uložit hodnoty do pole a přečíst je indexem.
