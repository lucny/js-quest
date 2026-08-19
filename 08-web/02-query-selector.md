<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 8.2 Selektory a vlastnosti DOM.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/liaTemplates/WebDev/master/README.md
-->
@JSQ.styles
# WORLD 8 — Selektor a stav panelu
@JSQ.world(8, Web a DOM)

## PROBLÉM

Jedna stránka má více prvků. Potřebujeme vybrat právě ten správný a změnit nejen text, ale třeba i jeho vzhled.

## PREDICT
@JSQ.predict
> Co se po spuštění změní: text, barva, nebo obojí?

```html
<p id="selector-lamp-2" style="padding: 12px; background: #fee2e2;">Lampa je vypnutá.</p>
```
```js
const lamp = document.querySelector('#selector-lamp-2');
lamp.textContent = 'Lampa svítí.';
lamp.style.background = '#fef08a';
```
@WebDev.HTML_JS

Jeden selector najde jeden prvek. Přes proměnnou potom čteme a měníme jeho vlastnosti: například `textContent` nebo `style.background`.

## BUG HUNT
@JSQ.bug
> **BUG HUNT** @JSQ.xp(4)
> Proč se tento program nezmění podle očekávání? Formuluj hypotézu a potom oprav pouze selector.

```html
<p id="selector-score-2">Skóre: 0</p>
```
```js
const score = document.querySelector('selector-score-2');
score.textContent = 'Skóre: 10';
```
@WebDev.HTML_JS

<details><summary>Nápověda 1</summary>Porovnej selector s hodnotou atributu <code>id</code>.</details>
<details><summary>Nápověda 2</summary>Selector pro id začíná znakem <code>#</code>.</details>
<details><summary>Možné řešení</summary>Použij <code>document.querySelector('#selector-score-2')</code>.</details>

## QUICK QUIZ
@JSQ.quiz
> Co je po tomto příkazu v proměnné `score`?

[( )] Řetězec `'#selector-score-2'`.
[(X)] Nalezený HTML prvek s daným id.
[( )] Vždy celé HTML stránky.

## MISSION
@JSQ.mission
> **MISSION: INDIKÁTOR ENERGIE** @JSQ.xp(6)
> Najdi panel energie. Nastav mu text „Energie: 80 %“ a zvol barvu pozadí, která odpovídá bezpečnému stavu.

```html
<p id="selector-energy-2" style="padding: 12px; background: #e5e7eb;">Energie: neznámá</p>
```
```js
const energy = document.querySelector('#selector-energy-2');

// TODO: Nastav srozumitelný text energie.
// TODO: Nastav barvu pozadí bezpečného stavu přes energy.style.background.
console.log(energy.textContent);
```
@WebDev.HTML_JS

<details><summary>Nápověda 1</summary>Stejný prvek můžeš upravit ve dvou samostatných příkazech.</details>
<details><summary>Nápověda 2</summary>Pro barvu stačí řetězec, například <code>'#dcfce7'</code>.</details>
<details><summary>Možné řešení</summary>Nastav <code>energy.textContent</code> a pak <code>energy.style.background</code>.</details>

@JSQ.flag
> @JSQ.codeflag
> Dokážu vybrat konkrétní prvek a upravit jeho text i styl.
