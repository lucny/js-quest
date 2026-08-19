<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 4.3 return a lokální proměnná.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 4 — Funkce může vrátit výsledek
@JSQ.world(4, Functions)
## PREDICT
@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
> Jakou hodnotu vrátí `double(6)`?
[( )] 6
[(X)] 12
[( )] undefined
[( )] 36
```js
function double(number) {
  return number * 2;
}
```
## LEARN
Některé funkce nekreslí ani nemění stav — spočítají hodnotu, kterou chceme použít jinde. `return` předá takový výsledek zpět na místo volání.

```js
function double(number) {
  const result = number * 2;
  return result;
}

const size = double(6);
```

Nejprve parametr `number` dostane 6, funkce vytvoří `result` s hodnotou 12 a `return` tuto hodnotu vrátí. Teprve potom se 12 uloží do `size`. Proměnná `result` patří jen do těla funkce; mimo něj ji JavaScript nezná. Proto venku nepíšeme `result`, ale použijeme návratovou hodnotu.
## COMPLETE CODE
@JSQ.complete
> **🔧 COMPLETE CODE** @JSQ.xp(2)
> Vrať z funkce velikost o polovinu větší.
```js
function bigger(size) {
  // TODO: Vrať vypočtenou hodnotu.
}
```
## BUG HUNT
@JSQ.bug
> **🐞 BUG HUNT** @JSQ.xp(2)
> Proč nelze po volání použít proměnnou `result`?
```js
function sum(a, b) {
  const result = a + b;
  return result;
}
console.log(result);
```
<details><summary>Řešení</summary>`result` je lokální. Ulož návratovou hodnotu: `const total = sum(2, 3)`.</details>
## MISSION
@JSQ.mission
> **🎯 MISSION: VÝPOČET VELIKOSTI** @JSQ.xp(4)
> Vytvoř funkci, která z hodnoty energie vrátí velikost kruhu, a výsledek použij při kreslení.
```js
function sizeFromEnergy(energy) {
  // TODO: Vypočti a vrať velikost mezi 20 a 100.
}
p5.setup = function () {
  p5.createCanvas(600, 300);
};
p5.draw = function () {
  p5.background(245);
  const size = sizeFromEnergy(6);
  // TODO: Použij size jako třetí parametr kruhu.
  p5.circle(300, 150, 40);
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Vrať výraz, který energii násobí; návratovou hodnotu použij jako třetí parametr kruhu.</details>
@JSQ.flag
> @JSQ.thinkflag
> Dokážu rozlišit lokální proměnnou a návratovou hodnotu.
