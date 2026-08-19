# Stav

Pilot WORLD 1 je připraven jako referenční LiaScript lekce ve větvi `experimental/pilot`. Zdroj zůstává čitelný jako Markdown, společné prvky jsou centralizované a je k dispozici lokální strukturální validace.

## Co bylo ověřeno

- Hlavní metadata, `import:`, parametrizovaná makra, blok makra, HTML/CSS, single-choice kvízy, hinty/řešení a editovatelný kód byly porovnány s oficiální dokumentací LiaScriptu.
- `GAME-MACROS.md` úspěšně zpracoval oficiální LiaScript Exporter do JSON; export obsahoval všechny makra `@JSQ.*`.
- Minimální sketch s importem aktuální p5js template úspěšně zpracoval tentýž Exporter. Template definuje `@P5.eval` a vytváří `new p5(sketch, div)`, tedy instanční kontext s prefixem `p5.`.
- `python tools/validate_course.py` prošel: ověřuje soubory, UTF-8, code fences, metadata a importy pilotu, sadu maker, párování karet, WORLD a lokální odkazy.
- `git diff --check` prošel bez chyb mezer a konců řádků.

## Provedené opravy

- Pilot importuje sdílené `GAME-MACROS.md`; duplicita CSS a maker v lekci byla odstraněna.
- Sada maker je jednotná pro `PREDICT`, `EXPERIMENT`, `COMPLETE`, `BUG`, `MISSION`, `BONUS`, `QUIZ`, `BOSS`, `FLAG` a `XP`. Zachován je i kompatibilní alias `@JSQ.flagbox`.
- Vzhled karet používá rámeček, textový název a symbol aktivity, ne pouze barvu; akcenty mají variantu pro tmavé schéma.
- p5.js poznámka nyní ukazuje standardní `setup()`/`draw()` i LiaScript `p5.setup`/`p5.draw`.
- Boss výslovně končí problémem, že objekt opustí canvas; motivuje tím následující lekci o podmínkách bez zavedení `if` do WORLD 1.

## Známá omezení LiaScriptu

- `import:` načítá makra z veřejně dostupné raw URL. Dokud větev `experimental/pilot` není pushnutá, její import `GAME-MACROS.md` nelze načíst z GitHubu.
- Lokální validátor není parser LiaScriptu. Neověří síťovou dostupnost importů, výsledný DOM ani vizuální rozvržení.
- p5js template je externí závislost; interaktivní canvas vyžaduje prohlížeč a dostupnost šablony/CDN.

## Co nelze automaticky hodnotit

- Zda student opravdu nejprve předpovídal, místo aby sketch okamžitě spustil.
- Zda samostatně vytvořil požadovaný pohyb v Mission nebo Boss.
- Zda rozumí rozdílu mezi `x += speed` a `x =+ speed`, pokud jej nedoplní vysvětlením nebo navazujícím úkolem.
- Přístupnost a srozumitelnost vizuálního renderu na konkrétním mobilu či ve čtečce obrazovky.

## Doporučení pro pilotní test

1. Pushni větev a otevři pilot přes odkaz v `README.md`.
2. Ověř na desktopu i mobilu import maker, všechna tlačítka `@P5.eval`, Stop a vykreslení canvasu.
3. Nech několik studentů projít lekci bez nápovědy od učitele a zaznamenej, zda rozumějí prefixu `p5.` a chybě `x =+ speed`.
4. Zjisti, zda XP podporují orientaci v postupu, aniž by působily jako známka.

## Doporučený další krok

Po pilotním testu vyhodnoť pozorování podle sekce „Co se má ověřit po pilotu“ v `GAME-DESIGN.md`. Teprve potom rozhodni o rozsahu a podobě WORLD 2 — Decisions; v této větvi jej zatím nevytvářej.

## Seznam změněných souborů

- `AGENTS.md` — nové trvalé instrukce a validační postup.
- `TECHNICAL-NOTES.md` — zdroje a technické opravy.
- `PILOT-REPORT.md` — tento závěrečný report.
- `tools/validate_course.py` — lehká strukturální validace.
- `GAME-MACROS.md` — sjednocená a přístupnější sada maker.
- `01-variables/01-moving-ball.md` — import sdílených maker, upřesnění p5.js a závěr Bossu.
- `README.md` — technický vstup do projektu, spuštění a validace.
