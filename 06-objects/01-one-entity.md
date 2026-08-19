<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 6.1 object literal a properties.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 6 — Vlastnosti patří k sobě
@JSQ.world(6, Objects)
## ENTRY
`playerX`, `playerY`, `playerSpeed`, `playerSize` a `playerColor` popisují jednoho hráče. Uložíme je jako jeden celek.
```js
const player = { x: 100, y: 150, speed: 3, size: 40, color: 'blue' };
```
## PREDICT
@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
> Jak přečteš vodorovnou polohu hráče?
[( )] `x.player`
[(X)] `player.x`
[( )] `player[x]`
[( )] `x.player()`
## LEARN
Objekt řeší problém dlouhého seznamu proměnných, které popisují jednu entitu. Object literal vytvoří celek v kudrnatých závorkách; každá property má jméno, dvojtečku a vlastní hodnotu.

```js
const player = {
  x: 100,
  y: 150,
  size: 40
};

const horizontalPosition = player.x;
```

Tečka čte jednu property z konkrétního objektu. `player.x` tedy znamená „vodorovná poloha tohoto hráče“, ne obecná proměnná `x`. Properties oddělujeme čárkami. Typická chyba je obrátit pořadí na `x.player` nebo zapomenout, že tečka patří za název objektu.
## MISSION
@JSQ.mission
> **🎯 MISSION: KARTA HRÁČE** @JSQ.xp(4)
> Vytvoř jeden objekt pro hráče a použij jeho properties pro kreslení kruhu.
```js
const player = { x: 100, y: 150, size: 40 };
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  // TODO: Přečti properties objektu při kreslení.
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Tečka spojuje název objektu a název vlastnosti.</details>
@JSQ.flag
> @JSQ.codeflag
> Umím vytvořit objekt a přečíst jeho property.
