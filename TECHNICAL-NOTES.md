# Technické poznámky

## 2026-08-19 — Společná makra byla zduplikovaná v pilotní lekci

- **Problém:** `01-variables/01-moving-ball.md` obsahovala vlastní kopii CSS a maker `@JSQ.*`, přestože projekt má `GAME-MACROS.md`.
- **Příčina:** LiaScript načítá při `import:` pouze definice z hlavního headeru importovaného Markdown souboru; pilot dosud neměl odkaz na publikovatelný projektový template.
- **Provedená oprava:** pilot nyní importuje `GAME-MACROS.md` z raw URL větve `experimental/pilot` a lokální kopie maker byla odstraněna. Vizuální změny se proto provádějí na jednom místě.
- **Zdroj:** [LiaScript — import](https://raw.githubusercontent.com/LiaScript/docs/master/README.md#L9634-L9639), [LiaScript — templates](https://liascript.github.io/blog/import-a-frame-3d-models-scenes-and-more-into-liascript/).

## 2026-08-19 — Jednotné názvy typů aktivit

- **Problém:** template používal pro vlajky pouze interně znějící název `@JSQ.flagbox`, zatímco ostatní typy aktivit mají přímé názvy.
- **Příčina:** původní sada maker nevystavovala jednotné veřejné API pro `FLAG`.
- **Provedená oprava:** přidáno `@JSQ.flag`; `@JSQ.flagbox` zůstává jako kompatibilní alias. Sada nyní pokrývá `PREDICT`, `EXPERIMENT`, `COMPLETE`, `BUG`, `MISSION`, `BONUS`, `QUIZ`, `BOSS`, `FLAG` a `XP`.
- **Zdroj:** [LiaScript — macro basics](https://raw.githubusercontent.com/LiaScript/docs/master/README.md#L820-L943).

## 2026-08-19 — p5.js instance mode je odlišen od běžného sketche

- **Problém:** pilot uváděl běžnou p5.js podobu jen částečně, což mohlo zastřít rozdíl mezi `setup()` / `draw()` a template zápisem s prefixem `p5.`.
- **Příčina:** LiaScript p5js template používá instanční kontext, kde jsou p5 funkce a vlastnosti dostupné přes `p5.`.
- **Provedená oprava:** závěrečná technická poznámka nyní ukazuje obě dvojice funkcí a vysvětluje, že jde o rozdíl způsobu zapojení knihovny, nikoli o jiný JavaScript.
- **Zdroj:** [oficiální p5js template pro LiaScript](https://liascript.github.io/blog/p5js-creative-coding-in-liascript/), [p5.js instance mode](https://github.com/processing/p5.js/wiki/p5.js-overview).

## Ověřená syntaxe

Header s metadaty, `import:`, jednoduchá a parametrizovaná makra, blokové makro definice, HTML/CSS, single-choice kvízy, hinty/řešení a editovatelný kód odpovídají dokumentaci LiaScriptu. Pilot používá `@P5.eval` podle aktuální dokumentace p5js template.

Oficiální LiaScript Exporter úspěšně zpracoval `GAME-MACROS.md` do JSON a potvrdil všechny definice `@JSQ.*`. Celý pilot nelze před pushem větve exportovat se stejnou jistotou, protože jeho nově zavedený import odkazuje na dosud nepublikovanou raw URL větve. Vizuální render je proto nutné po pushi ověřit v LiaScriptu.
