<!--
author:     JS Quest pilot
version:    0.1.0
language:   cs
comment:    Pilotní lekce WORLD 1: proměnné a stav programu pomocí pohybující se kuličky.

import: https://raw.githubusercontent.com/lucny/js-quest/experimental/pilot/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->

@JSQ.styles

# WORLD 1 — Pohybující se kulička

@JSQ.world(1, Variables)

> **Variables / stav programu / operátory**
>
> Cíl není naučit se nazpaměť několik zápisů. Cílem je pochopit, jak program uchovává hodnotu mezi jednotlivými okamžiky a jak ji můžeme měnit.

---

## ENTRY — Objekt, který si musí pamatovat polohu

Spusť následující sketch.

```js
p5.setup = function () {
  p5.createCanvas(600, 300);
};

p5.draw = function () {
  p5.background(240);
  p5.circle(80, 150, 40);
};
```
@P5.eval

Kruh se nehýbe.

Program při každém vykreslení používá stále stejné číslo `80`.

Potřebujeme tedy způsob, jak si program bude **pamatovat polohu**, kterou lze měnit.

---

## PREDICT — Co se změní?

@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
>
> Kód zatím nespouštěj.
>
> Co podle tebe udělá změna `80` na `200` v příkazu:
>
> ```js
> p5.circle(200, 150, 40);
> ```
>
> [( )] kruh bude větší
> [(X)] kruh se posune doprava
> [( )] kruh se posune dolů
> [( )] nic se nezmění

@JSQ.end
Číslo v prvním parametru určuje vodorovnou souřadnici středu kruhu.

Ale stále je to jen pevná hodnota.

---

## EXPERIMENT — Nahraď číslo proměnnou

@JSQ.experiment
> **🧪 EXPERIMENT**
>
> Spusť sketch a potom změň pouze počáteční hodnotu `x`.
>
> Vyzkoušej například `20`, `300` a `550`.
>
> Co zůstává stejné a co se mění?

@JSQ.end
```js
let x = 80;

p5.setup = function () {
  p5.createCanvas(600, 300);
};

p5.draw = function () {
  p5.background(240);
  p5.circle(x, 150, 40);
};
```
@P5.eval

Zápis:

```js
let x = 80;
```

říká:

1. vytvoř proměnnou `x`,
2. ulož do ní číslo `80`.

Příkaz:

```js
p5.circle(x, 150, 40);
```

už nepoužívá pevnou hodnotu polohy. Používá **aktuální hodnotu proměnné `x`**.

---

## LEARN — Proměnná jako stav programu

Proměnnou si můžeme pro začátek představit jako pojmenované místo pro hodnotu:

```text
x ─────► 80
```

Hodnotu můžeme později změnit:

```js
x = 120;
```

Potom platí:

```text
x ─────► 120
```

Znak `=` zde neznamená matematickou rovnici. Je to **přiřazení**.

Pravá strana se vyhodnotí a výsledek se uloží do proměnné vlevo.

---

## PREDICT — Zvláštní „rovnice“

@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
>
> Co znamená tento zápis?
>
> ```js
> x = x + 2;
> ```
>
> [( )] matematickou rovnici bez řešení
> [( )] vytvoření nové proměnné `x`
> [(X)] vezmi současné `x`, přičti 2 a výsledek znovu ulož do `x`
> [( )] nastav `x` vždy na 2

@JSQ.end
Příklad:

```text
před příkazem: x = 80
výpočet:        80 + 2
po příkazu:    x = 82
```

---

## COMPLETE CODE — Rozhýbej kuličku

@JSQ.complete
> **🔧 COMPLETE CODE** @JSQ.xp(2)
>
> Na místě `TODO` doplň jediný příkaz tak, aby se hodnota `x` při každém průchodu `draw()` zvětšila o 2.

@JSQ.end
```js
let x = 80;

p5.setup = function () {
  p5.createCanvas(600, 300);
};

p5.draw = function () {
  p5.background(240);
  p5.circle(x, 150, 40);

  // TODO: zvětši x o 2
};
```
@P5.eval

Nápověda:

```text
nové x = staré x + 2
```

Řešení si zobraz až po vlastním pokusu:

```js
x = x + 2;
```

---

## LEARN — Zkrácený zápis

Tento zápis:

```js
x = x + 2;
```

lze zkrátit:

```js
x += 2;
```

Oba příkazy v tomto případě znamenají totéž.

Ještě užitečnější je oddělit **polohu** od **rychlosti**:

```js
let x = 80;
let speed = 2;
```

a potom:

```js
x += speed;
```

Tím získáme dvě samostatně měnitelné části stavu.

---

## EXPERIMENT — Rychlost je také hodnota

@JSQ.experiment
> **🧪 EXPERIMENT**
>
> Vyzkoušej postupně:
>
> ```js
> let speed = 1;
> let speed = 5;
> let speed = 15;
> let speed = -3;
> ```
>
> Před spuštěním poslední varianty nejprve odhadni, co udělá záporná rychlost.

@JSQ.end
```js
let x = 80;
let speed = 3;

p5.setup = function () {
  p5.createCanvas(600, 300);
};

p5.draw = function () {
  p5.background(240);
  p5.circle(x, 150, 40);

  x += speed;
};
```
@P5.eval

---

## QUICK QUIZ — Čteme stav programu

@JSQ.quiz
> **⚡ QUICK QUIZ** @JSQ.xp(1)
>
> Začínáme:
>
> ```js
> let x = 10;
> let speed = 3;
> ```
>
> Třikrát provedeme:
>
> ```js
> x += speed;
> ```
>
> Jaká bude hodnota `x`?
>
> [( )] 13
> [( )] 16
> [(X)] 19
> [( )] 30

@JSQ.end
---

## BUG HUNT — Dva znaky, jiný význam

@JSQ.bug
> **🐞 BUG HUNT** @JSQ.xp(2)
>
> Autor chtěl, aby se kruh posouval doprava.
>
> Program se ale nechová správně.
>
> Najdi chybu a oprav ji.

@JSQ.end
```js
let x = 80;
let speed = 3;

p5.setup = function () {
  p5.createCanvas(600, 300);
};

p5.draw = function () {
  p5.background(240);
  p5.circle(x, 150, 40);

  x =+ speed;
};
```
@P5.eval

### Co je špatně?

```js
x += speed;
```

znamená:

```js
x = x + speed;
```

Ale:

```js
x =+ speed;
```

se interpretuje jako přiřazení kladné hodnoty `speed` do `x`.

To je typická chyba, která může být syntakticky platná, ale logicky chybná.

---

## PROOF OF UNDERSTANDING — Dokážeš chybu vysvětlit?

@JSQ.quiz
> **⚡ CHECK** @JSQ.xp(1)
>
> Je-li `speed = 3`, co po příkazu `x =+ speed` platí?
>
> [( )] `x` se zvětší o 3
> [(X)] `x` dostane hodnotu 3
> [( )] JavaScript vždy vyhodí syntax error
> [( )] `x` dostane hodnotu -3

@JSQ.end
---

## MISSION — Pohyb ve dvou osách

@JSQ.mission
> **🎯 MISSION: DIAGONÁLNÍ LET** @JSQ.xp(4)
>
> Uprav program tak, aby:
>
> 1. vodorovná poloha byla uložena v `x`,
> 2. svislá poloha byla uložena v `y`,
> 3. existovala samostatná `speedX`,
> 4. existovala samostatná `speedY`,
> 5. kruh se pohyboval diagonálně.
>
> Nepřidávej zatím `if`, pole ani objekty.

@JSQ.end
Starter:

```js
let x = 80;
let y = 80;

let speedX = 3;
let speedY = 2;

p5.setup = function () {
  p5.createCanvas(600, 300);
};

p5.draw = function () {
  p5.background(240);

  p5.circle(x, y, 40);

  // TODO: změň x
  // TODO: změň y
};
```
@P5.eval

Po dokončení si zodpověz:

- Která proměnná určuje vodorovný pohyb?
- Která proměnná určuje svislý pohyb?
- Co se stane, když `speedY` změníš na záporné číslo?

---

## PROOF OF UNDERSTANDING — Bez spuštění

@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
>
> Máme:
>
> ```js
> let x = 100;
> let y = 50;
> let speedX = 4;
> let speedY = -2;
>
> x += speedX;
> y += speedY;
> ```
>
> Jaké budou nové hodnoty?
>
> [( )] `x = 96`, `y = 52`
> [(X)] `x = 104`, `y = 48`
> [( )] `x = 104`, `y = 52`
> [( )] `x = 400`, `y = -100`

@JSQ.end
---

## SIDE QUEST — Dva objekty, dva různé stavy

@JSQ.bonus
> **💎 SIDE QUEST: PROTISMĚR** @JSQ.xp(3)
>
> Přidej druhý kruh.
>
> První se má pohybovat doprava a druhý doleva.
>
> Nepoužívej zatím pole ani objekty.
>
> Cílem je zjistit, proč se nám při větším počtu entit začnou hodit složitější datové struktury.

@JSQ.end
Možná výchozí sada proměnných:

```js
let x1 = 80;
let speed1 = 2;

let x2 = 520;
let speed2 = -3;
```

Zbytek navrhni sám.

---

## BOSS — Signal Runners

@JSQ.boss
> **🏆 BOSS: SIGNAL RUNNERS** @JSQ.xp(10)
>
> Vytvoř scénu se dvěma kruhy.
>
> Povinné požadavky:
>
> - každý kruh má vlastní `x` a `y`,
> - každý má vlastní vodorovnou rychlost,
> - alespoň jeden má nenulovou svislou rychlost,
> - rychlosti jsou uložené v proměnných,
> - v `draw()` nejsou souřadnice pohybujících se kruhů zapsány jako pevná čísla,
> - řešení používá pouze principy, které už byly v této lekci vysvětleny.
>
> **Záměrně zatím neřeš odraz od okraje.** To je problém pro WORLD 2 — Decisions.

@JSQ.end
Po dokončení porovnej své řešení se spolužákem:

1. Kolik proměnných jste potřebovali?
2. Které názvy jsou čitelnější?
3. Kde se začíná objevovat opakování?
4. Jaký problém podle vás budeme řešit pomocí objektů nebo polí?

Kruhy dříve nebo později odletí z canvasu. Zatím to neopravuj: příště budeme potřebovat rozhodnutí podle podmínky, tedy `if`.

---

## FLAGS — Co máš skutečně umět

@JSQ.flag
> @JSQ.codeflag
>
> Umím vytvořit proměnnou pomocí `let` a změnit její hodnotu.

@JSQ.end
@JSQ.flag
> @JSQ.thinkflag
>
> Dokážu vysvětlit rozdíl mezi:
>
> ```js
> x += speed;
> ```
>
> a
>
> ```js
> x =+ speed;
> ```

@JSQ.end
@JSQ.flag
> @JSQ.buildflag
>
> Dokážu pomocí proměnných a operátorů vytvořit objekt, který se v p5.js pohybuje ve dvou osách.

@JSQ.end
---

## EXIT CHECK

Bez spuštění programu určete výsledek:

```js
let x = 5;
let speed = 4;

x += speed;
x += speed;
speed = -2;
x += speed;
```

Jaká je výsledná hodnota `x`?

[( )] 7
[(X)] 11
[( )] 15
[( )] -2

---

## Technická poznámka: proč je všude `p5.`?

V běžném p5.js často uvidíš:

```js
function setup() {
  createCanvas(600, 300);
}

function draw() {
  background(240);
  circle(80, 150, 40);
}
```

Oficiální p5js šablona pro LiaScript používá tzv. **instance mode**, a proto v této učebnici zapisujeme:

```js
p5.setup = function () {
  p5.createCanvas(600, 300);
};

p5.draw = function () {
  p5.background(240);
  p5.circle(80, 150, 40);
};
```

JavaScriptové principy `let`, přiřazení, operátory a funkce jsou stejné. Liší se způsob, jakým je p5.js připojeno k prostředí LiaScriptu.

---

## Skóre pilotní lekce

XP v této verzi slouží jako motivační orientace, nikoli jako automaticky ověřené hodnocení.

```text
Predict + Quick Checks     5 XP
Complete Code              2 XP
Bug Hunt                   2 XP
Mission                    4 XP
Side Quest                 3 XP
Boss                      10 XP
──────────────────────────────
maximum                    26 XP
```

Pro skutečné hodnocení jsou důležitější tři vlajky výše než samotný součet XP.
