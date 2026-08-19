<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 8.4 Boss Mini Web App.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/liaTemplates/WebDev/master/README.md
-->
@JSQ.styles
# WORLD 8 — Mini Web App
@JSQ.world(8, Web a DOM)

## BOSS
@JSQ.boss
> **BOSS: VYSÍLAČ ÚKOLŮ** @JSQ.xp(10)
> Vytvoř malou aplikaci pro vysílač: student napíše úkol, klikne na tlačítko a aplikace jej přidá do seznamu. Zobraz také počet uložených úkolů.

```html
<div style="max-width: 440px; padding: 16px; border: 2px solid #818cf8; border-radius: 8px;">
  <h2>Vysílač úkolů</h2>
  <input id="app-task-input-4" placeholder="Nový úkol">
  <button id="app-add-button-4">Přidat</button>
  <p id="app-count-4">Úkoly: 0</p>
  <ul id="app-list-4"></ul>
</div>
```
```js
const tasks = [];
const taskInput = document.querySelector('#app-task-input-4');
const addButton = document.querySelector('#app-add-button-4');
const taskCount = document.querySelector('#app-count-4');
const taskList = document.querySelector('#app-list-4');

function renderTasks() {
  taskList.innerHTML = '';
  for (let index = 0; index < tasks.length; index = index + 1) {
    const item = document.createElement('li');
    item.textContent = tasks[index];
    taskList.appendChild(item);
  }
  taskCount.textContent = `Úkoly: ${tasks.length}`;
}

addButton.addEventListener('click', function () {
  // TODO: Ulož neprázdnou hodnotu inputu do pole tasks.
  // TODO: Po změně pole zavolej renderTasks a vyčisti input.
  console.log('Čekám na nový úkol.');
});

renderTasks();
```
@WebDev.HTML_JS

<details><summary>Nápověda 1</summary>Nejprve si ulož <code>taskInput.value</code> do proměnné a ověř, že není prázdná.</details>
<details><summary>Nápověda 2</summary>Novou hodnotu přidá <code>tasks.push(...)</code>; pak zavolej existující funkci <code>renderTasks()</code>.</details>
<details><summary>Možné řešení</summary>V obsluze kliknutí přidej neprázdnou hodnotu do pole, nastav <code>taskInput.value = ''</code> a zavolej <code>renderTasks()</code>.</details>

## BONUS
@JSQ.bonus
> Přidej tlačítko „Vyčistit“, které vyprázdní pole a znovu vykreslí seznam. Než začneš, napiš si: která proměnná je stav a která funkce jen zobrazuje stav?

## FLAG
@JSQ.flag
> @JSQ.worldflag
> Dokážu spojit HTML, CSS, JavaScript, pole, funkci a click událost do malé webové aplikace.
