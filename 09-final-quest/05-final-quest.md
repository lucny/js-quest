<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 9.5 Final Quest.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 9 — Final Quest
@JSQ.world(9, Final Quest)

## FINAL BOSS
@JSQ.boss
> **FINAL QUEST: VLASTNÍ FUNKČNÍ PROGRAM** @JSQ.xp(15)
> Vytvoř samostatný program z cesty A–D nebo vlastní varianty. Nehodnotí se rychlost ani počet řádků: cílem je srozumitelný funkční zážitek.

Tvůj projekt musí obsahovat:

- proměnnou a smysluplný stav;
- podmínku;
- cyklus;
- vlastní funkci;
- pole nebo objekt;
- interakci uživatele nebo DOM událost;
- čitelně pojmenované části kódu.

Pro p5 projekt můžeš začít touto minimální kostrou. Pro DOM variantu navazuj na Mini Web App z WORLD 8 a zachovej stejná kritéria.

```js
const projectState = {
  score: 0,
  items: []
};

function updateProject() {
  // TODO: Popiš a napiš jednu malou změnu vlastního stavu.
}

function drawProject() {
  // TODO: Nakresli nebo zobraz aktuální stav projektu.
}

p5.setup = function () {
  p5.createCanvas(620, 360);
};

p5.draw = function () {
  p5.background(248);
  updateProject();
  drawProject();
  // TODO: Přidej interakci a pravidlo, které mění stav.
};
```
@P5.eval

<details><summary>První krok po vlastním pokusu</summary>Napiš nejdřív jen jeden průchod: co uživatel udělá a co se hned viditelně změní.</details>
<details><summary>Kontrola struktury</summary>Najdi v kódu pojmenovaný stav, funkci, podmínku, cyklus, data a interakci. Když některá část chybí, doplň ji kvůli projektu, ne jen kvůli seznamu.</details>
<details><summary>Jak ověřit hotový projekt</summary>Požádej spolužáka, aby bez nápovědy provedl hlavní akci. Sleduj, zda vidí důsledek a zda umí popsat, co program dělá.</details>

## REFLEXE

Napiš si: Který problém jsi vyřešil? Co bylo tvoje nejužitečnější debugovací zjištění? Jaké jedno rozšíření bys přidal, kdybys měl další hodinu?

@JSQ.flag
> @JSQ.worldflag
> Dokážu samostatně navrhnout, vytvořit, otestovat a vysvětlit malý JavaScriptový program.
