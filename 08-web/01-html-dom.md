<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 8.1 HTML a DOM.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/liaTemplates/WebDev/master/README.md
-->
@JSQ.styles
# WORLD 8 — HTML a DOM
@JSQ.world(8, Web a DOM)

## PROBLÉM

Webová stránka už obsahuje nadpis a odstavec. Jak může JavaScript poznat, který konkrétní prvek má změnit?

## PREDICT
@JSQ.predict
> **PŘEDPOVĚĎ** @JSQ.xp(2)
> Než program spustíš: jaký text bude po spuštění v zeleném panelu?

```html
<p id="dom-message-1" style="padding: 12px; background: #dcfce7;">Čekám na JavaScript.</p>
```
```js
document.querySelector('#dom-message-1').textContent = 'JavaScript prvek našel.';
```
@WebDev.HTML_JS

DOM je strom prvků stránky. JavaScript nezačíná novou stránku tvořit; může pracovat s prvky, které HTML už vytvořilo.

## EXPERIMENT
@JSQ.experiment
> Změň `textContent` na vlastní větu. Potom změň id v HTML a ověř, proč se musí změnit i selector.

```html
<h2 id="dom-title-1">Signál</h2>
<p id="dom-status-1">Stav: čekám</p>
```
```js
const status = document.querySelector('#dom-status-1');
status.textContent = 'Stav: doručen';
```
@WebDev.HTML_JS

`document.querySelector('#dom-status-1')` vrací prvek s daným id. Znak `#` znamená, že hledáme id, ne běžný text.

## QUICK QUIZ
@JSQ.quiz
> K čemu slouží `document.querySelector('#dom-title-1')`?

[( )] Vytvoří nový HTML soubor.
[(X)] Najde prvek stránky s id `dom-title-1`.
[( )] Spustí cyklus přes všechny nadpisy.

## MISSION
@JSQ.mission
> **MISSION: OPRAV PANEL** @JSQ.xp(6)
> V panelu je jméno průzkumníka. Po spuštění změň jeho text na vlastní přezdívku a změň stav na „připraveno“. Scaffold už stránku vykreslí.

```html
<article style="padding: 12px; border: 2px solid #60a5fa;">
  <h2 id="dom-player-name">Průzkumník: neznámý</h2>
  <p id="dom-player-status">Stav: čekám</p>
</article>
```
```js
const playerName = document.querySelector('#dom-player-name');
const playerStatus = document.querySelector('#dom-player-status');

// TODO: Změň text prvku playerName na vlastní přezdívku.
// TODO: Změň text prvku playerStatus na „Stav: připraveno“.
console.log(playerName.textContent, playerStatus.textContent);
```
@WebDev.HTML_JS

<details><summary>Nápověda 1</summary>Obě proměnné už obsahují nalezené HTML prvky.</details>
<details><summary>Nápověda 2</summary>Text prvku změníš vlastností <code>textContent</code>.</details>
<details><summary>Možné řešení</summary><code>playerName.textContent = 'Průzkumník: Ada';</code> a potom obdobně změň stav.</details>

@JSQ.flag
> @JSQ.codeflag
> Dokážu najít HTML prvek podle id a změnit jeho obsah.
