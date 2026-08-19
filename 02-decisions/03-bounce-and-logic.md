<!--
author:     JS Quest
version:    0.1.0
language:   cs
comment:    WORLD 2.3: odraz od hranic a logické operátory.

import: https://raw.githubusercontent.com/lucny/js-quest/experimental/world2/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->

@JSQ.styles

# WORLD 2 — Odraz a logické operátory

@JSQ.world(2, Decisions)

> Pravá hranice už umí otočit rychlost. Kulička ale po návratu odletí levou stranou.

---

## ENTRY — Dvě samostatné otázky

@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
>
> Je `x = -2`. Která otázka je nyní `true`?

[( )] `x > p5.width`
[(X)] `x < 0`
[( )] `x === 0`
[( )] `x > 0`

Nejdřív napišeme obě reakce zvlášť:

```js
if (x > p5.width) {
  speed = -speed;
}

if (x < 0) {
  speed = -speed;
}
```

---

## EXPERIMENT — Jedna nebo druhá

@JSQ.experiment
> **🧪 EXPERIMENT**
>
> Nahraď dvě podmínky jedinou. Sleduj, že `||` znamená „nebo“: stačí, aby platila jedna strana.

```js
if (x > p5.width || x < 0) {
  speed = -speed;
}
```

---

## LEARN — Logické spojení

Když se má stejná reakce stát na levé **nebo** pravé hranici, není nutné psát stejný příkaz dvakrát. Operátor `||` spojí dvě otázky do jedné:

```js
if (x > p5.width || x < 0) {
  speed = -speed;
}
```

Levá část testuje pravou hranici, pravá část levou. Celý výraz je `true`, když platí alespoň jedna část. Naproti tomu `&&` znamená „a současně“ — hodí se až tehdy, když musí platit více hranic najednou, například u obdélníkové zóny. Zápis `!A` obrátí odpověď otázky A. Typická chyba je zaměnit `||` a `&&`: objekt nemůže být současně napravo od canvasu a nalevo od nuly.

---

## COMPLETE CODE — Odraz ve dvou osách

@JSQ.complete
> **🔧 COMPLETE CODE** @JSQ.xp(2)
>
> Doplň dvě otázky pro svislý pohyb, aby se měnila i `ySpeed`.

```js
let x = 100;
let y = 80;
let xSpeed = 3;
let ySpeed = 2;

p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  p5.circle(x, y, 40);
  x += xSpeed;
  y += ySpeed;

  if (x > p5.width || x < 0) {
    xSpeed = -xSpeed;
  }
  // TODO: if pro y a p5.height
};
```
@P5.eval

<details><summary>Pomoc po vlastním pokusu</summary>

Pro osu y použij stejné uspořádání: horní hranice je 0, dolní je `p5.height`.

<details><summary>Řešení</summary>

```js
if (y > p5.height || y < 0) {
  ySpeed = -ySpeed;
}
```

</details></details>

---

## BUG HUNT — Správná podmínka, špatná rychlost

@JSQ.bug
> **🐞 BUG HUNT** @JSQ.xp(2)
>
> Kulička narazí nahoře a dole, ale změní vodorovný směr. Najdi jeden chybný název proměnné.

```js
if (y > p5.height || y < 0) {
  xSpeed = -xSpeed;
}
```

<details><summary>Řešení</summary>

V podmínce o ose y měníme `ySpeed`.

</details>

---

## MISSION — Kulička, která nezmizí

@JSQ.mission
> **🎯 MISSION: ČTYŘI HRANICE** @JSQ.xp(5)
>
> Vytvoř objekt s `x`, `y`, `xSpeed` a `ySpeed`, který se pohybuje a odráží od všech čtyř hranic canvasu. Použij alespoň jedno `||`.

```js
let x = 100;
let y = 80;
let xSpeed = 3;
let ySpeed = 2;

p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  x += xSpeed;
  y += ySpeed;
  p5.circle(x, y, 40);

  // TODO: Přidej rozhodování pro obě vodorovné hranice.
  // TODO: Přidej rozhodování pro obě svislé hranice.
};
```
@P5.eval

<details><summary>Pomoc po vlastním pokusu</summary>

Rozděl problém na vodorovný a svislý odraz. Každý potřebuje vlastní rychlost.

<details><summary>Konkrétnější nápověda</summary>

Pro osu x testuj `p5.width` a 0; pro osu y `p5.height` a 0.

<details><summary>Řešení</summary>

```js
if (x > p5.width || x < 0) {
  xSpeed = -xSpeed;
}
if (y > p5.height || y < 0) {
  ySpeed = -ySpeed;
}
```

</details>

</details></details>

---

## QUICK QUIZ — Kdy platí nebo?

@JSQ.quiz
> **⚡ QUICK QUIZ** @JSQ.xp(1)
>
> Kdy je `x > 600 || x < 0` pravda?

[(X)] když je x napravo od 600 nebo nalevo od 0
[( )] pouze když platí obě části současně
[( )] pouze když je x přesně 0
[( )] nikdy

---

## SIDE QUEST — Přesnější náraz

@JSQ.bonus
> **💎 SIDE QUEST** @JSQ.xp(3)
>
> Kruh má průměr 40. Uprav podmínky tak, aby se jeho okraj, ne až střed, nedostal za canvas. Jakou roli hraje poloměr 20?

---

## FLAGS — Objekt uvnitř prostoru

@JSQ.flag
> @JSQ.codeflag
>
> Umím spojit dvě hranice operátorem `||`.

@JSQ.flag
> @JSQ.thinkflag
>
> Dokážu vysvětlit rozdíl mezi `&&` a `||`.

@JSQ.flag
> @JSQ.buildflag
>
> Dokážu vytvořit objekt, který se neztratí z canvasu.

> **Další problém:** program už reaguje na hranice. Dokáže se rozhodovat i podle oblasti uvnitř canvasu?
