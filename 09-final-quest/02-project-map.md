<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 9.2 Rozklad projektu.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 9 — Rozlož projekt
@JSQ.world(9, Final Quest)

## PROBLÉM

Velké zadání se špatně programuje jako první krok. Rozlož ho na stav, vstupy, pravidla a výstupy.

## EXPERIMENT
@JSQ.experiment
> Ve výchozím programu změň jednu vlastnost objektu `plan` a sleduj, která část vizitky se promění.

```js
const plan = {
  input: 'šipky',
  state: 'pozice hráče',
  rule: 'sběr cíle přidá bod',
  output: 'skóre na obrazovce'
};

p5.setup = function () {
  p5.createCanvas(620, 260);
  p5.background(250);
  p5.textSize(20);
  p5.text(`Vstup: ${plan.input}`, 30, 55);
  p5.text(`Stav: ${plan.state}`, 30, 105);
  p5.text(`Pravidlo: ${plan.rule}`, 30, 155);
  p5.text(`Výstup: ${plan.output}`, 30, 205);
};
```
@P5.eval

## LEARN — Mapa odděluje rozhodnutí od kódu

Než začneš psát funkce, pojmenuj pět částí projektu: vstup, stav, pravidlo, výstup a funkci. Každá odpovídá na jinou otázku.

```js
const plan = {
  input: 'šipky',
  state: 'pozice hráče',
  rule: 'sběr cíle přidá bod',
  output: 'skóre na obrazovce'
};
```

Vstup říká, co udělá člověk. Stav je hodnota, kterou si program pamatuje. Pravidlo rozhoduje, kdy se stav změní, a výstup ukáže důsledek. Taková mapa ještě není hotový program; chrání ale před tím, abys začal náhodně kreslit dřív, než víš, jaké údaje a pravidla potřebuješ.

## BUG HUNT
@JSQ.bug
> Proč se v tomto plánu neukáže pravidlo? Najdi rozdíl mezi názvem property v objektu a při čtení.

```js
const plan = { rule: 'kliknutí přidá bod' };
console.log(plan.rules);
```

<details><summary>Nápověda 1</summary>Objekt obsahuje jen jednu property.</details>
<details><summary>Nápověda 2</summary>Porovnej přesně <code>rule</code> a <code>rules</code>.</details>
<details><summary>Možné řešení</summary>Čti <code>plan.rule</code>.</details>

## MISSION
@JSQ.mission
> **MISSION: MAPA SYSTÉMU** @JSQ.xp(5)
> Přepiš čtyři hodnoty plánu pro vlastní projekt. Potom přidej pátou property `functionName` a nech ji vypsat do posledního řádku.

```js
const plan = {
  input: 'uživatel klikne',
  state: 'počet bodů',
  rule: 'kliknutí změní skóre',
  output: 'panel se skóre',
  // TODO: Přidej název funkce, která bude řídit hlavní změnu.
};

p5.setup = function () {
  p5.createCanvas(620, 280);
  p5.background(255, 251, 235);
  p5.textSize(19);
  p5.text(`Vstup: ${plan.input}`, 30, 55);
  p5.text(`Stav: ${plan.state}`, 30, 105);
  p5.text(`Pravidlo: ${plan.rule}`, 30, 155);
  p5.text(`Výstup: ${plan.output}`, 30, 205);
  // TODO: Vypiš novou property na poslední řádek.
};
```
@P5.eval

<details><summary>Nápověda 1</summary>Mezi properties objektu patří čárka.</details>
<details><summary>Nápověda 2</summary>Novou hodnotu můžeš číst zápisem <code>plan.functionName</code>.</details>
<details><summary>Možné řešení</summary>Jedna možnost je property <code>functionName: 'updateScore'</code>; název ale může být vlastní.</details>

@JSQ.flag
> @JSQ.thinkflag
> Dokážu rozdělit projekt na vstupy, stav, pravidla, výstupy a funkce.
