<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 5.5 Boss pole dat.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 5 — Data Field
@JSQ.world(5, Arrays)
## BOSS
@JSQ.boss
> **🏆 BOSS: DATA FIELD** @JSQ.xp(10)
> Vytvoř datovou vizualizaci nebo pole částic. Použij pole, `length`, cyklus a alespoň jednu změnu či přidání hodnoty.
```js
const values = [40, 90, 65, 120, 75];
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  // TODO: Projdi data a převeď je na vizuální prvky.
  // TODO: Přidej nebo změň jednu hodnotu smysluplným pravidlem.
};
```
@P5.eval
<details><summary>Nápověda</summary>Začni jedním prvkem `values[i]`, pak použij celý cyklus.</details>
@JSQ.flag
> @JSQ.worldflag
> Dokážu řídit více hodnot pomocí pole a cyklu.
