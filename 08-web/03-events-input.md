<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 8.3 Události, tlačítko a input.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/liaTemplates/WebDev/master/README.md
-->
@JSQ.styles
# WORLD 8 — Událost mění stav
@JSQ.world(8, Web a DOM)

## PROBLÉM

DOM sám nic nezmění. Program potřebuje vědět, kdy člověk klikl na tlačítko nebo napsal hodnotu.

## PREDICT
@JSQ.predict
> Kolikrát se po dvou kliknutích změní číslo v panelu?

```html
<button id="event-button-3">Přidej signál</button>
<p id="event-count-3">Signály: 0</p>
```
```js
let signals = 0;
const button = document.querySelector('#event-button-3');
const count = document.querySelector('#event-count-3');

button.addEventListener('click', function () {
  signals = signals + 1;
  count.textContent = `Signály: ${signals}`;
});
```
@WebDev.HTML_JS

## LEARN — Událost odloží práci na později

`addEventListener('click', ...)` uloží funkci pro budoucí kliknutí. Funkce neběží při načtení; běží až při události.

```js
button.addEventListener('click', function () {
  signals = signals + 1;
  count.textContent = `Signály: ${signals}`;
});
```

První argument `'click'` říká, na jakou událost čekáme. Druhý argument je funkce, kterou má prohlížeč zavolat později. Uvnitř funkce nejdřív změníme stav v proměnné `signals`, potom zobrazíme nový stav v DOM. Závorky za názvem funkce by ji spustily hned; pro listener předáváme funkci samotnou.

## EXPERIMENT
@JSQ.experiment
> Napiš do políčka své slovo a klikni. Pak uprav větu, kterou aplikace zobrazí.

```html
<input id="event-input-3" value="Ada">
<button id="event-send-3">Pozdrav</button>
<p id="event-output-3">Zpráva čeká.</p>
```
```js
const input = document.querySelector('#event-input-3');
const send = document.querySelector('#event-send-3');
const output = document.querySelector('#event-output-3');

send.addEventListener('click', function () {
  output.textContent = `Ahoj, ${input.value}!`;
});
```
@WebDev.HTML_JS

Hodnota z inputu je v `input.value`. Stav aplikace zde tvoří proměnná `signals` i aktuální obsah inputu.

## BUG HUNT
@JSQ.bug
> Proč se v následujícím programu změní počítadlo hned při načtení místo po kliknutí?

```html
<button id="event-bug-button-3">Klikni</button>
<p id="event-bug-output-3">0</p>
```
```js
let clicks = 0;
const bugButton = document.querySelector('#event-bug-button-3');
const bugOutput = document.querySelector('#event-bug-output-3');

function addClick() {
  clicks = clicks + 1;
  bugOutput.textContent = clicks;
}

bugButton.addEventListener('click', addClick());
```
@WebDev.HTML_JS

<details><summary>Nápověda 1</summary>Rozliš mezi zavoláním funkce a předáním funkce jako hodnoty.</details>
<details><summary>Nápověda 2</summary>Za název funkce při registraci události nepatří závorky.</details>
<details><summary>Možné řešení</summary>Použij <code>bugButton.addEventListener('click', addClick);</code>.</details>

## MISSION
@JSQ.mission
> **MISSION: KÓDOVÝ VZKAZ** @JSQ.xp(7)
> Po kliknutí má panel převzít slovo z inputu. Pokud je políčko prázdné, zobraz přátelskou výzvu k napsání zprávy.

```html
<input id="event-mission-input-3" placeholder="Napiš zprávu">
<button id="event-mission-button-3">Odeslat</button>
<p id="event-mission-output-3">Zatím nic.</p>
```
```js
const messageInput = document.querySelector('#event-mission-input-3');
const messageButton = document.querySelector('#event-mission-button-3');
const messageOutput = document.querySelector('#event-mission-output-3');

messageButton.addEventListener('click', function () {
  // TODO: Přečti hodnotu z messageInput.
  // TODO: Rozhodni, jaký text zobrazit pro prázdnou a vyplněnou zprávu.
  messageOutput.textContent = 'Zpráva čeká na tvoje pravidlo.';
});
```
@WebDev.HTML_JS

<details><summary>Nápověda 1</summary>Hodnota inputu je v <code>messageInput.value</code>.</details>
<details><summary>Nápověda 2</summary>Podmínka může porovnat hodnotu s prázdným řetězcem <code>''</code>.</details>
<details><summary>Možné řešení</summary>V obsluze kliknutí ulož hodnotu do proměnné a přes <code>if</code> vyber jednu ze dvou zpráv.</details>

@JSQ.flag
> @JSQ.buildflag
> Dokážu propojit input, událost kliknutí a změnu DOM.
