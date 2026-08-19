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

## 2026-08-19 — Párové HTML makro zobrazovalo technické tagy

- **Problém:** v LiaScript Preview se karty zobrazovaly s doslovným otevíracím a uzavíracím tagem místo stylovaného obsahu.
- **Příčina:** otevírací tag byl vložen jedním makrem a uzavírací jiným makrem v samostatném Markdown bloku. Tento přesah přes hranice bloků není pro renderer spolehlivý.
- **Provedená oprava:** každý typ karty nyní expanduje pouze na LiaScript attribute comment `<!-- class="…" -->`; ten se aplikuje na bezprostředně následující blockquote. HTML wrappery a uzavírací makro byly odstraněny.
- **Zdroj:** [LiaScript — attribute comments](https://raw.githubusercontent.com/LiaScript/docs/master/README.md#L502-L537), [LiaScript — macro basics](https://raw.githubusercontent.com/LiaScript/docs/master/README.md#L820-L943).

## 2026-08-19 — Pomoc nesmí předcházet samostatnému pokusu

- **Problém:** Complete Code a Bug Hunt bezprostředně po zadání ukazovaly nápovědu i úplné řešení.
- **Příčina:** otevřené programátorské aktivity nemají vlastní LiaScript quiz mechanismus a pomoc byla zapsaná jako běžný Markdown obsah.
- **Provedená oprava:** u otevřených úloh je pomoc nyní v postupně otevíraných standardních prvcích `details`/`summary`: nasměrování, konkrétnější koncept a až potom řešení. Skutečné LiaScript kvízy používají `[[?]]`, blok nativního řešení a tlačítka zpřístupněná po prvním chybném pokusu.
- **Zdroj:** [LiaScript — details a summary](https://raw.githubusercontent.com/LiaScript/docs/master/README.md#L1666-L1694), [LiaScript — quiz hints a solution](https://raw.githubusercontent.com/LiaScript/docs/master/README.md#L3789-L3896), [LiaScript — hint/solution buttons](https://raw.githubusercontent.com/LiaScript/docs/master/README.md#L3957-L4014).

## 2026-08-19 — Export pilotu zatím načítá starší vzdálené makro

- **Problém:** Exporter pilotní lekce proběhl, ale jeho JSON obsahuje starší verzi `GAME-MACROS.md` s původními wrappery.
- **Příčina:** hlavička lekce importuje raw URL větve `experimental/pilot`; vzdálená větev zatím neobsahuje lokální opravnou iteraci.
- **Provedená oprava:** žádná změna zdroje není vhodná — import má zůstat sdílený. Před dalším vizuálním testem je nutné pushnout tuto větev a export/preview zopakovat.
- **Zdroj:** [LiaScript — import](https://raw.githubusercontent.com/LiaScript/docs/master/README.md#L9634-L9639).

## Ověřená syntaxe

Header s metadaty, `import:`, jednoduchá a parametrizovaná makra, blokové makro definice, HTML/CSS, single-choice kvízy, hinty/řešení a editovatelný kód odpovídají dokumentaci LiaScriptu. Pilot používá `@P5.eval` podle aktuální dokumentace p5js template.

Oficiální LiaScript Exporter úspěšně zpracoval aktuální lokální `GAME-MACROS.md` do JSON a potvrdil jeho atributová makra. Export pilotu ověřil syntaxi lekce, ale před pushem importoval starší vzdálenou verzi maker. Vizuální render s aktuálními kartami je proto nutné po pushi ověřit znovu v LiaScriptu.
