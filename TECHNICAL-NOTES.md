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

## 2026-08-19 — Vedlejší formulář Submit u kvízů

- **Problém:** po některých kvízech renderer zobrazil samostatný blok se dvěma nezaškrtnutými položkami a tlačítkem `Submit`.
- **Přesný audit zdroje:** žádný řádek `01-variables/01-moving-ball.md` ani `GAME-MACROS.md` nezačínal task-list syntaxí `- [ ]`, `- [x]`, `- [X]`, `* […]` nebo `+ […]`. Text ze samostatného formuláře pocházel z dvojic řádků `[[?]]` (například ř. 334–335: „Začni hodnotou…“ a „Každé provedení…“). V aktuálním Preview tyto nativní hinty nebyly připojené k předchozímu single-choice kvízu a renderer je vyložil jako vlastní odpovědní rozhraní.
- **Provedená oprava:** všech 12 řádků `[[?]]` bylo z pilotu odstraněno. Každá dvojice nápověd i následné vysvětlení je nyní ve standardním `details`/`summary` bloku bez vstupních polí a tlačítka `Submit`. Volby `[( )]` / `[(X)]` zůstávají jediným interaktivním rozhraním kvízu.
- **Prevence:** validátor kontroluje každou studentskou lekci adresářů `NN-*` přes přesný vzor `^[-*+] \[[ xX]\]` a při nalezení LiaScript Task selže.
- **Zdroj:** [LiaScript — single-choice quiz](https://raw.githubusercontent.com/LiaScript/docs/master/README.md#L3275-L3316), [LiaScript — nápovědy a řešení](https://raw.githubusercontent.com/LiaScript/docs/master/README.md#L3789-L4014), [LiaScript — task lists](https://raw.githubusercontent.com/LiaScript/docs/master/README.md#L3006-L3042).

## 2026-08-19 — Fallback fontu pro české znaky v navigaci

- **Problém:** české znaky v levém menu a obsahu kapitol používaly jiný font než ostatní text.
- **Příčina:** projekt nenačítal externí webfont ani vlastní `@font-face`; navigační komponenty tak dědily typografii rendereru jinak než obsah a pro znaky Latin Extended se mohl uplatnit glyph fallback.
- **Provedená oprava:** `@JSQ.styles` nyní nastavuje pro dokument, ovládací prvky a navigační/sidebar/TOC selektory jednotný systémový stack `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Arial, sans-serif`. `Segoe UI` na Windows a `Noto Sans` jako další volba pokrývají českou diakritiku bez per-glyph fallbacku.
- **Ověření zdroje:** v projektu nejsou další definice `font-family` ani `@font-face`; globální pravidlo je jediným zdrojem typografie.

## 2026-08-19 — Export pilotu zatím načítá starší vzdálené makro

- **Problém:** Exporter pilotní lekce proběhl, ale jeho JSON obsahuje starší verzi `GAME-MACROS.md` s původními wrappery.
- **Příčina:** hlavička lekce importuje raw URL větve `experimental/pilot`; vzdálená větev zatím neobsahuje lokální opravnou iteraci.
- **Provedená oprava:** žádná změna zdroje není vhodná — import má zůstat sdílený. Před dalším vizuálním testem je nutné pushnout tuto větev a export/preview zopakovat.
- **Zdroj:** [LiaScript — import](https://raw.githubusercontent.com/LiaScript/docs/master/README.md#L9634-L9639).

## Ověřená syntaxe

## 2026-08-19 — WORLD 2 používal vzdálený template jiné větve

- **Příčina:** všechny čtyři lekce WORLD 2 importovaly `GAME-MACROS.md` z raw URL větve `experimental/pilot`. Lokální `GAME-MACROS.md` s globálním systémovým font stackem se tak v Preview větve WORLD 2 nepoužil jako jeho sdílený template.
- **Ovlivněné soubory:** `02-decisions/01-boolean-questions.md`, `02-if.md`, `03-bounce-and-logic.md` a `04-zones.md`.
- **Proč se lišil WORLD 1:** WORLD 1 je publikován v `experimental/pilot`, tedy ve stejné větvi jako importovaný template; WORLD 2 odkazoval zpět na jinou větev.
- **Oprava:** všechny lekce WORLD 2 nyní importují jeden sdílený template z `experimental/world2/GAME-MACROS.md`; nepřidávalo se žádné lokální `font-family` pravidlo. Po pushi je nutné Preview načíst znovu.

Header s metadaty, `import:`, jednoduchá a parametrizovaná makra, blokové makro definice, HTML/CSS, single-choice kvízy, skrytá vysvětlení a editovatelný kód odpovídají dokumentaci LiaScriptu. Pilot používá `@P5.eval` podle aktuální dokumentace p5js template. Kvízy jsou mimo blockquote herních karet a pilot neobsahuje task-list syntaxi ani řádky `[[?]]`.

Oficiální LiaScript Exporter úspěšně zpracoval aktuální lokální `GAME-MACROS.md` do JSON a potvrdil jeho atributová makra. Export pilotu ověřil syntaxi lekce, ale před pushem importoval starší vzdálenou verzi maker. Vizuální render s aktuálními kartami je proto nutné po pushi ověřit znovu v LiaScriptu.
