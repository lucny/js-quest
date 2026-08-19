<!--
author:     JS Quest
version:    0.1.0
language:   cs
comment:    WORLD 2.4: větve if/else a prostorové zóny canvasu.

import: https://raw.githubusercontent.com/lucny/js-quest/experimental/world2/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->

@JSQ.styles

# WORLD 2 — Zóny a if / else

@JSQ.world(2, Decisions)

> Kulička už umí reagovat na okraj. Teď se bude její chování měnit i uvnitř canvasu.

---

## ENTRY — Dvě poloviny, jedna volba

```js
let x = 80;
let speed = 3;

p5.setup = function () { p5.createCanvas(600, 300); };
p5.draw = function () {
  p5.background(245);
  if (x < p5.width / 2) {
    p5.fill(30, 90, 220);
  } else {
    p5.fill(230, 90, 40);
  }
  p5.circle(x, 150, 40);
  x += speed;
};
```
@P5.eval

---

## PREDICT — Která větev platí?

@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
>
> Canvas má šířku 600 a `x` je 420. Jakou barvu dostane kulička v ukázce?

[( )] modrou z větve `if`
[(X)] oranžovou z větve `else`
[( )] obě barvy současně
[( )] žádnou barvu

---

## LEARN — else není nová otázka

```js
if (x < p5.width / 2) {
  // levá polovina
} else {
  // všechno ostatní
}
```

`else` není druhé nezávislé `if`. Je to druhá větev stejného rozhodnutí: když podmínka neplatí, vykoná se `else`.

Program tedy nejdřív jednou vyhodnotí otázku `x < p5.width / 2`. Je-li odpověď `true`, provede se první blok. Je-li `false`, první blok se přeskočí a provede se blok po `else`. Nikdy se při jednom rozhodnutí neprovedou obě větve.

To je užitečné pro volbu jedné z možností: modrá **nebo** oranžová, aktivní zóna **nebo** běžný stav. Pokud bys napsal dva samostatné bloky `if`, musel bys sám hlídat, zda se jejich pravidla nepřekrývají.

---

## EXPERIMENT — Najdi střed

@JSQ.experiment
> **🧪 EXPERIMENT**
>
> Změň dělicí hodnotu `p5.width / 2` na `200` a potom na `450`. Kde přesně je hranice barevné zóny?

---

## COMPLETE CODE — Obdélník jako otázka

@JSQ.complete
> **🔧 COMPLETE CODE** @JSQ.xp(2)
>
> Doplň podmínku, která zjistí, zda je kulička uvnitř středové zóny: x je mezi 220 a 380 a y mezi 90 a 210.

```js
const jeVeZone = /* TODO */;
if (jeVeZone) {
  p5.fill(40, 180, 80);
} else {
  p5.fill(80);
}
```

<details><summary>Pomoc po vlastním pokusu</summary>

Každé „mezi“ potřebuje dvě porovnání. Všechna čtyři musí platit, proto je spoj `&&`.

<details><summary>Řešení</summary>

```js
x > 220 && x < 380 && y > 90 && y < 210
```

</details></details>

---

## BUG HUNT — else patří k if

@JSQ.bug
> **🐞 BUG HUNT** @JSQ.xp(2)
>
> Autor chtěl šedou barvu mimo zónu. Proč jeho druhý `if` přebarví kuličku hned po zelené?

```js
if (jeVeZone) {
  p5.fill(40, 180, 80);
}
if (!jeVeZone) {
  p5.fill(80);
}
```

<details><summary>Pomoc po vlastním pokusu</summary>

Tento zápis může fungovat, ale skrývá myšlenku „jinak“. Zapiš obě větve jednoho rozhodnutí vedle sebe.

<details><summary>Řešení</summary>

```js
if (jeVeZone) {
  p5.fill(40, 180, 80);
} else {
  p5.fill(80);
}
```

</details></details>

---

## MISSION — Aktivní zóna

@JSQ.mission
> **🎯 MISSION: ZELENÝ SEKTOR** @JSQ.xp(5)
>
> Vytvoř pohybující se kuličku, která se odráží od čtyř hranic. Když vstoupí do obdélníkové oblasti uprostřed, změň jí barvu nebo velikost. Mimo oblast vrať původní vlastnost pomocí `else`.

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
  if (x > p5.width || x < 0) {
    xSpeed = -xSpeed;
  }
  if (y > p5.height || y < 0) {
    ySpeed = -ySpeed;
  }

  p5.fill(70);
  // TODO: Rozhodni, zda je kulička uvnitř středové obdélníkové oblasti.
  // TODO: V oblasti změň vlastnost kuličky, mimo ni ji vrať pomocí else.
  p5.circle(x, y, 40);
};
```
@P5.eval

<details><summary>Pomoc po vlastním pokusu</summary>

Rozděl program na pohyb, odrazy a až potom otázku pro zónu.

<details><summary>Konkrétnější nápověda</summary>

Zóna potřebuje porovnání x zleva i zprava a y shora i zdola spojená `&&`.

<details><summary>Řešení</summary>

```js
const veZone = x > 220 && x < 380 && y > 90 && y < 210;
if (veZone) {
  p5.fill(40, 180, 80);
} else {
  p5.fill(70);
}
```

</details>

</details></details>

---

## QUICK QUIZ — Kdy je zóna aktivní?

@JSQ.quiz
> **⚡ QUICK QUIZ** @JSQ.xp(1)
>
> Proč spojujeme hranice obdélníkové zóny operátorem `&&`?

[(X)] kulička musí současně splnit všechny hranice zóny
[( )] stačí splnit libovolnou hranici
[( )] `&&` mění rychlost
[( )] `&&` znamená „jinak“

---

## SIDE QUEST — Vlastní pravidlo

@JSQ.bonus
> **💎 SIDE QUEST** @JSQ.xp(3)
>
> Přidej druhou zónu s jinou barvou. Zachovej jednu jasnou větev `if`/`else` pro každé rozhodnutí.

---

## BOSS — Smart Ball

@JSQ.boss
> **🏆 BOSS: SMART BALL** @JSQ.xp(10)
>
> Vytvoř autonomní objekt. Musí mít vlastní `x`, `y`, `xSpeed` a `ySpeed`, pohybovat se, reagovat na všechny čtyři hranice, použít alespoň jedno `if`, jedno spojení `&&` nebo `||` a obdélníkovou zónu. Po vstupu do zóny změň jeho barvu, velikost nebo rychlost.

<details><summary>Nápověda 1</summary>

Rozděl problém na pohyb, hranice a zónu.

<details><summary>Nápověda 2</summary>

Pro hranice testuj x a y samostatně. Obdélníková zóna obsahuje několik porovnání spojených `&&`.

<details><summary>Jedna úplná varianta</summary>

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
  if (x > p5.width || x < 0) {
    xSpeed = -xSpeed;
  }
  if (y > p5.height || y < 0) {
    ySpeed = -ySpeed;
  }
  const zone = x > 220 && x < 380 && y > 90 && y < 210;
  if (zone) {
    p5.fill(40, 180, 80);
  } else {
    p5.fill(70);
  }
  p5.circle(x, y, 40);
};
```

</details></details></details>

---

## FLAGS — Autonomní rozhodování

@JSQ.flag
> @JSQ.codeflag
>
> Umím zapsat větev pomocí `if` a `else`.

@JSQ.flag
> @JSQ.thinkflag
>
> Dokážu určit, kdy musí platit všechna porovnání spojená `&&`.

@JSQ.flag
> @JSQ.buildflag
>
> Dokážu vytvořit objekt reagující na hranice i prostorovou zónu.

@JSQ.flag
> @JSQ.worldflag
>
> Umím navrhnout program, který podle podmínek autonomně mění své chování.
