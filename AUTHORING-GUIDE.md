# JS Quest — AUTHORING-GUIDE

**Verze:** 1.0
**Určeno pro:** autora lekcí, Codex/AI asistenta i učitele, který bude materiály později upravovat.

---

## 1. Povinné principy

Každá lekce musí:

1. začít problémem nebo pozorovatelným jevem,
2. obsahovat aktivitu před delším vysvětlením,
3. vést studenta k předpovědi alespoň jednou,
4. obsahovat editovatelný kód,
5. obsahovat nejméně jeden debuggingový moment,
6. mít jasně oddělené povinné minimum a Side Quest,
7. zakončit sebereflexí nebo ověřením kompetence,
8. nepoužívat body jako náhradu hodnocení znalostí.

---

## 2. Doporučená hlavička lekce

```text
<!--
author:     ...
version:    0.1.0
language:   cs
comment:    Krátký popis lekce.

import: https://RAW-URL/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
```

Po importu společných maker:

```text
@JSQ.styles
```

Pro lekce `08-web/` místo p5js importu použijte ověřený WebDev template:

```text
import: https://raw.githubusercontent.com/liaTemplates/WebDev/master/README.md
```

Ostatní studentské lekce používají p5js template. Vždy importujte pouze jeden z těchto runtime template.

---

## 3. Struktura souboru

Doporučená kostra:

```text
# Název lekce

@JSQ.world(1, Variables)

## ENTRY
## PREDICT
## EXPERIMENT
## LEARN
## TRAINING 1
## TRAINING 2
## BUG HUNT
## MISSION
## PROOF OF UNDERSTANDING
## SIDE QUEST
## BOSS
## FLAGS
```

Krátká lekce může některé sekce sloučit. Pořadí „aktivita před vysvětlením“ však zachovejte.

---

## 4. LEARN BLOCK STANDARD

LEARN blok nevkládejte před první pokus, ale po problému, předpovědi nebo experimentu, který dal konstrukci důvod existovat. Při zavádění významného konceptu má LEARN zpravidla obsahovat:

1. problém, který konstrukce řeší;
2. krátký, víceřádkový příklad;
3. rozklad významu syntaxe nebo jednotlivých řádků;
4. krokový mentální model běhu programu;
5. typickou chybu či nedorozumění;
6. vazbu na předchozí znalost a další aktivitu.

Nejde o povinnost psát dlouhé odstavce. Jedna přesná věta může stačit pro opakování; první výklad `for`, `while`, `if`, funkce, parametrů, `return`, pole, indexu, objektu, metody, selectoru nebo event listeneru však musí studentovi vysvětlit nejen název, ale i důvod a chování zápisu.

Používejte podle potřeby čtyři lehké varianty: **concept** (proč konstrukce existuje), **syntax** (jak číst její části), **mental model** (co se děje krok po kroku) a **pitfall** (jak rozpoznat běžnou chybu). Didakticky významnou konstrukci nikdy neschovávejte do dlouhého jednořádkového příkladu.

---

## 5. Predict before run

Předpověď musí být skutečná. Student nesmí současně vidět výsledek.

Příklad:

```text
@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
>
> Kód zatím nespouštěj.
>
> Jaká bude hodnota `x`?
>
> ```js
> let x = 10;
> x += 5;
> x *= 2;
> ```
>
> [( )] 15
> [(X)] 30
> [( )] 25
```

Potom může následovat experiment nebo vysvětlení.

Makro typu aktivity vždy stojí samostatně před blockquotem. Vloží atributový komentář pro tento jediný blok; nikdy nepoužívejte dvojici maker, která otevírá a zavírá HTML element přes více Markdown bloků.

Pokud je karta zároveň kvízem, blockquote ukončete před první volbou. Možnosti `[( )]` a `[(X)]` musí tvořit jeden souvislý LiaScript blok mimo blockquote. Pomoc i vysvětlení patří do zavřených `details`/`summary` bloků.

---

## 6. Kvízy

V ověřeném JS Quest používáme pouze single-choice syntax:

```text
[( )] chybná možnost
[(X)] správná možnost
```

Nikdy do studentských lekcí nevkládejte `[[?]]`, `[[X]]` ani `[[ ]]`: renderer je může interpretovat jako další formulář se Submit. Stejně zakázané jsou dekorativní LiaScript Tasks `- [ ]`, `- [x]` a `- [X]`. Pomoc a vysvětlení vždy napište do zavřených `details`.

Příklad single choice:

```text
Co udělá `x += 2`?

[( )] nastaví `x` na 2
[(X)] zvýší aktuální `x` o 2
[( )] vytvoří novou proměnnou
```

Kvízy standardně používejte jako učení s možností opravy, nikoli jako trest za první chybný pokus.

---

## 7. Práce s p5.js

### 7.1 Důležité: LiaScript p5js template používá instance mode

V oficiální šabloně se píše:

```js
p5.setup = function () {
  p5.createCanvas(600, 400);
};

p5.draw = function () {
  p5.background(240);
  p5.circle(100, 200, 40);
};
```

Studentům vždy vysvětlete, že v běžném p5.js často uvidí:

```js
function setup() {
  createCanvas(600, 400);
}

function draw() {
  background(240);
  circle(100, 200, 40);
}
```

Rozdíl je způsob spuštění knihovny, nikoli jiný JavaScriptový jazyk.

### 7.2 Začátečnické pravidlo

V jedné úloze měňte primárně jeden nový koncept.

Nevhodné při první proměnné:

```js
// náhodnost + pole + objekty + funkce + podmínky najednou
```

Vhodné:

```js
let x = 100;

p5.draw = function () {
  p5.circle(x, 200, 40);
  x += 2;
};
```

### 7.3 Nepoužívat canvas násilně

Pole cen, textové operace nebo DOM úlohy mohou být vhodnější jako čistý JavaScript nebo WebDev.

---

## 8. Complete Code

Starter kód musí být téměř funkční.

```js
let x = 100;

p5.setup = function () {
  p5.createCanvas(600, 400);
};

p5.draw = function () {
  p5.background(240);
  p5.circle(x, 200, 40);

  // TODO: posuň x o hodnotu speed
};
```

Student nemá ve stejné chvíli řešit tři neznámé problémy.

---

## 9. Bug Hunt

Chyba musí být:

- realistická,
- tematicky relevantní,
- lokalizovatelná pomocí znalostí z lekce.

Příklad:

```js
x =+ speed;
```

Typická chybná interpretace:

> „Je to totéž jako `x += speed`.“

Následující otázka má vyžadovat vysvětlení rozdílu.

---

## 10. Mission

Mission zadává chování, ne konkrétní řádek k doplnění.

Špatně:

> Na řádku 17 napiš `x += speed`.

Lépe:

> Uprav program tak, aby se kruh pohyboval doprava rychlostí uloženou v samostatné proměnné `speed`.

### Mission scaffolding

Mission vždy obsahuje editor s runnable výchozím kódem. Známé části jsou předpřipravené; student řeší právě nový koncept ve 1–3 významných `TODO`. TODO popisuje problém, nikoli hotovou syntaxi. Pomoc je progresivní a řešení zůstává skryté.

```js
// TODO: Rozhodni, zda objekt překročil hranici.
// TODO: Pokud ano, změň jeho chování.
```

COMPLETE obvykle chybí jeden příkaz či výraz; BONUS nabízí méně scaffoldu a více svobody; BOSS poskytuje pouze minimální technickou kostru a specifikaci.

### Web/DOM Mission

V `08-web/` napište bezprostředně po sobě HTML a JavaScript code block a poté `@WebDev.HTML_JS`. Používejte pro každý příklad jedinečné id, aby selector mířil na správný prvek. Výchozí kód musí fungovat i před doplněním TODO.

---

## 11. Boss

Boss musí kombinovat již probrané koncepty, nikoli skrytě zavádět několik nových.

Boss WORLD 1 může vyžadovat:

- více proměnných,
- různé počáteční hodnoty,
- více rychlostí,
- změny v každém průchodu `draw()`.

Neměl by vyžadovat `if`, pole nebo objekty, pokud ještě nebyly vysvětleny.

---

## 12. Důkaz porozumění po grafické úloze

Canvasový výsledek nemusí být automaticky strojově ověřitelný.

Proto po Mission používejte jednu z metod:

- otázka na význam konkrétního řádku,
- předpověď dalšího snímku,
- textové vysvětlení,
- výběr správné modifikace,
- jednoduchý automatizovatelný čistě-JS test.

Nikdy nepřidělujte „ověřené“ body jen proto, že student klikl na Run.

---

## 13. Side Quest

Side Quest musí být skutečně dobrovolný.

Má:

- rozšířit myšlenku,
- zaměstnat rychlejší studenty,
- neblokovat pokračování Main Questu.

Příklady:

- přidání druhého objektu,
- změna směru,
- kreativní barevná varianta,
- parametrizace.

---

## 14. Soutěžní úlohy

Soutěž musí mít krátký horizont.

Vhodné:

- 10min Bug Race,
- 15min Creative Challenge,
- Duel ve dvojici,
- Random Arena,
- týdenní miniliga.

Nevhodné:

- jeden trvalý veřejný pořadník celé třídy za celé pololetí.

---

## 15. Přístupnost a vizuální styl

- význam nesmí být sdělován pouze barvou,
- každý typ aktivity má symbol + název,
- text musí zůstat čitelný v dark i light mode,
- kód má být krátký a dobře členěný,
- animace nesmí být nutná k pochopení jediného kritického sdělení,
- u rychlé animace nabídněte možnost Stop.

---

## 16. Názvy a adresářová struktura

```text
js-quest/
├── GAME-DESIGN.md
├── GAME-MACROS.md
├── AUTHORING-GUIDE.md
├── 00-boot/
├── 01-variables/
│   ├── 01-moving-ball.md
│   └── ...
└── ...
```

Soubor:

```text
NN-topic-slug.md
```

WORLD:

```text
NN-world-name/
```

---

## 17. Kontrolní checklist autora

Před dokončením lekce:

Před commitem si ověř: aktivita před výkladem, skutečná předpověď, LEARN podle uvedeného standardu, editovatelný a runnable scaffold, izolovaný nový koncept, realistický Bug Hunt, dobrovolný Bonus, Boss bez nové syntaxe, kompetenční Flag a skrytou pomoc. Karty používej jen jako samostatný řádek `@JSQ.*` bezprostředně před blockquotem; attribute comment nikdy nevkládej do odstavce.

Potom spusť `python tools/validate_course.py`, oficiální LiaScript Exporter pro upravenou lekci, regresní `rg` search a `git diff --check`. Varování validátoru pro krátký LEARN nebo dlouhou jednořádkovou konstrukci vyřeš, nebo v revizi zdůvodni, proč je ukázka výjimkou.

---

## 18. Technické zdroje ověřené pro pilot

- LiaScript dokumentace: `https://raw.githubusercontent.com/LiaScript/docs/master/README.md`
- p5js template: `https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md`
- WebDev template: `https://raw.githubusercontent.com/liaTemplates/WebDev/master/README.md`
- p5.js reference: `https://p5js.org/reference/`

V době návrhu pilotu dokumentace LiaScriptu uvádí makra, importy, kvízy, interaktivní scripting a lokální ukládání průběhu; oficiální p5js template nabízí `@P5.eval` a `@P5.project`.
