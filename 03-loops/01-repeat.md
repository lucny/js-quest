<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 3.1 opakování a první for.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 3 — Opakování bez kopírování
@JSQ.world(3, Loops)
## ENTRY — Třicet kruhů
Jak nakreslit 30 objektů bez třiceti příkazů?
@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
> Kolikrát se provede tělo cyklu `for (let i = 0; i < 5; i += 1)`?
[( )] 4
[(X)] 5
[( )] 6
[( )] nekonečně
## EXPERIMENT — Počítadlo kreslí řadu
```js
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  for (let i = 0; i < 10; i += 1) {
    p5.circle(40 + i * 55, 150, 30);
  }
};
```
@P5.eval
## LEARN — for
Cyklus `for` řeší opakovaný krok, který by bylo únavné psát třicetkrát. Jeho hlavičku čti po částech:

```js
for (let i = 0; i < 10; i += 1) {
  p5.circle(40 + i * 55, 150, 30);
}
```

- `let i = 0` vytvoří počítadlo a nastaví první průchod.
- `i < 10` je otázka: dokud platí, vykoná se tělo cyklu.
- `i += 1` změní počítadlo po každém průchodu.
- Odsazený příkaz je to, co se opakuje.

Hodnoty `i` jsou postupně 0 až 9, takže tělo proběhne desetkrát. Když zapomeneš počítadlo měnit nebo dáš špatnou hranici, cyklus může běžet příliš dlouho či vůbec neskončit.
## COMPLETE CODE
@JSQ.complete
> **🔧 COMPLETE CODE** @JSQ.xp(2)
> Doplň hranici tak, aby vzniklo 12 kruhů.
```js
for (let i = 0; i < /* TODO */; i += 1) {
  p5.circle(30 + i * 45, 150, 25);
}
```
## BUG HUNT
@JSQ.bug
> **🐞 BUG HUNT** @JSQ.xp(2)
> Proč tento cyklus nikdy nekončí?
```js
for (let i = 0; i < 10; i -= 1) {
}
```
<details><summary>Řešení</summary>Počítadlo se musí zvětšovat: `i += 1`.</details>
## MISSION
@JSQ.mission
> **🎯 MISSION: ŘADA SIGNÁLŮ** @JSQ.xp(4)
> Vytvoř řadu 15 značek s pravidelným rozestupem.
```js
p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  // TODO: Opakuj kreslení značky 15×.
  // TODO: Použij počítadlo pro její vodorovnou polohu.
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>V každém průchodu se mění jen poloha.</details>
## FLAGS
@JSQ.flag
> @JSQ.buildflag
> Dokážu nahradit opakovaný kód jednoduchým cyklem `for`.
