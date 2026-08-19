<!--
author:     JS Quest
version:    0.1.0
language:   cs
comment:    WORLD 2.1: porovnání a booleanové výrazy před podmínkou if.

import: https://raw.githubusercontent.com/lucny/js-quest/experimental/world2/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->

@JSQ.styles

# WORLD 2 — Otázky s odpovědí true / false

@JSQ.world(2, Decisions)

> **Navazujeme na WORLD 1:** kulička se umí pohybovat, ale jednou odletí z canvasu. Jak může program poznat, že se dostala k okraji?

---

## ENTRY — Otázka o poloze

Spusť sketch a sleduj text pod kuličkou. Až kulička opustí pravou stranu, hodnota se změní.

```js
let x = 80;
let speed = 3;

p5.setup = function () {
  p5.createCanvas(600, 300);
};

p5.draw = function () {
  p5.background(245);
  p5.circle(x, 150, 40);
  p5.textSize(20);
  p5.text(`x > width: ${x > p5.width}`, 20, 35);
  x += speed;
};
```
@P5.eval

---

## PREDICT — Kdy se odpověď změní?

@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
>
> Je `x = 580`. Jakou hodnotu má výraz `x > p5.width`, když canvas má šířku 600?

[( )] `true`
[(X)] `false`
[( )] číslo 580
[( )] program spadne

<details>
<summary>Nápověda</summary>

Porovnáváme 580 a 600. Otázka zní: je 580 větší než 600?

</details>

---

## EXPERIMENT — Změň otázku, ne pohyb

@JSQ.experiment
> **🧪 EXPERIMENT**
>
> Ve výpisu postupně vyzkoušej `x > p5.width`, `x < p5.width` a `x >= p5.width`. Popiš, kdy je odpověď `true`.

Nemusíme ještě říkat programu, co má udělat. Nejdřív jen umíme položit otázku.

---

## LEARN — Booleanový výraz

Výraz `x > p5.width` má vždy jednu ze dvou hodnot: `true` nebo `false`. Říkáme mu **booleanový výraz**.

Pro začátek stačí tyto otázky:

- `>` je větší než,
- `<` je menší než,
- `>=` je větší nebo rovno,
- `<=` je menší nebo rovno,
- `===` je přesně stejné,
- `!==` není stejné.

Pozor na rozdíl:

```js
x = 300;    // ulož hodnotu
x === 300;  // polož otázku
```

---

## COMPLETE CODE — Zobraz správnou otázku

@JSQ.complete
> **🔧 COMPLETE CODE** @JSQ.xp(2)
>
> Doplň na místo `TODO` výraz, který zjistí, zda je kulička napravo od středu canvasu.

```js
let x = 420;

p5.setup = function () {
  p5.createCanvas(600, 300);
};

p5.draw = function () {
  p5.background(245);
  p5.circle(x, 150, 40);
  p5.textSize(20);
  const napravoOdStredu = /* TODO */;
  p5.text(napravoOdStredu, 20, 35);
};
```
@P5.eval

<details>
<summary>Pomoc po vlastním pokusu</summary>

**Nápověda 1.** Střed šířky canvasu je `p5.width / 2`.

<details>
<summary>Konkrétnější nápověda</summary>

**Nápověda 2.** Potřebuješ otázku začínající `x >`.

<details>
<summary>Jedno možné řešení</summary>

```js
x > p5.width / 2
```

</details>
</details>
</details>

---

## BUG HUNT — Jedno rovná se nestačí

@JSQ.bug
> **🐞 BUG HUNT** @JSQ.xp(2)
>
> Autor chtěl zjistit, zda je `x` přesně 300. Proč jeho program místo otázky mění hodnotu `x`?

```js
let x = 280;
const jeUprostred = x = 300;
```

<details>
<summary>Pomoc po vlastním pokusu</summary>

Přiřazení `=` uloží hodnotu. Pro porovnání stejnosti potřebujeme tři rovnítka.

<details>
<summary>Řešení</summary>

```js
const jeUprostred = x === 300;
```

</details>
</details>

---

## MISSION — Otázka pro odletující kuličku

@JSQ.mission
> **🎯 MISSION: HRANIČNÍ DETEKTOR** @JSQ.xp(4)
>
> Vytvoř pohybující se kuličku a pod ní zobraz booleanovou hodnotu otázky „je kulička za pravým okrajem?“. Kulička se zatím nemá vracet.

```js
let x = 80;
let speed = 3;

p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  p5.circle(x, 150, 40);
  x += speed;

  // TODO: Vytvoř booleanovou otázku o pravém okraji.
  // TODO: Zobraz její aktuální hodnotu jako text.
};
```
@P5.eval

<details>
<summary>Pomoc po vlastním pokusu</summary>

Začni se známým `x += speed` a přidej výraz `x > p5.width` do proměnné.

<details><summary>Konkrétnější nápověda</summary>

Použij `const zaHranou = ...` a potom `p5.text(zaHranou, 20, 35)`.

<details><summary>Jedno možné řešení</summary>

```js
const zaHranou = x > p5.width;
p5.text(zaHranou, 20, 35);
```

</details></details>

</details>

---

## QUICK QUIZ — Přiřazení nebo otázka?

@JSQ.quiz
> **⚡ QUICK QUIZ** @JSQ.xp(1)
>
> Který zápis se ptá, zda má `speed` hodnotu `-3`?

[( )] `speed = -3`
[(X)] `speed === -3`
[( )] `speed > -3`
[( )] `speed += -3`

---

## SIDE QUEST — Přesná hranice

@JSQ.bonus
> **💎 SIDE QUEST** @JSQ.xp(2)
>
> Kdy je vhodnější otázka `x >= p5.width` než `x > p5.width`? Vyzkoušej obě a najdi rozdíl při přesné hodnotě 600.

---

## FLAGS — Co už umím zjistit

@JSQ.flag
> @JSQ.codeflag
>
> Umím zapsat porovnání pomocí `>`, `<` nebo `===`.

@JSQ.flag
> @JSQ.thinkflag
>
> Dokážu předpovědět, kdy booleanový výraz vrátí `true` nebo `false`.

@JSQ.flag
> @JSQ.buildflag
>
> Umím vytvořit výraz, který odpoví `true` nebo `false`.

> **Další problém:** program už umí odpovědět. Jak mu ale řekneme, co má udělat, když odpověď zní `true`?
