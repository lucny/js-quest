# Stav

Pilot WORLD 1 je připraven jako referenční LiaScript lekce ve větvi `experimental/pilot`. Opravná iterace odstranila nespolehlivé HTML wrappery i okamžitě viditelnou pomoc. Zdroj zůstává čitelný jako Markdown, společné prvky jsou centralizované a je k dispozici lokální strukturální validace.

## Co bylo ověřeno

- Hlavní metadata, `import:`, parametrizovaná makra, blok makra, HTML/CSS, single-choice kvízy, hinty/řešení a editovatelný kód byly porovnány s oficiální dokumentací LiaScriptu.
- Aktuální lokální `GAME-MACROS.md` úspěšně zpracoval oficiální LiaScript Exporter do JSON; export obsahoval atributové definice všech maker `@JSQ.*` bez wrapperů.
- Exporter byl spuštěn i nad pilotní lekcí. Syntaxe lekce prošla, ale import z raw URL ještě stáhl starší vzdálený `GAME-MACROS.md`; úplné ověření aktuální kombinace vyžaduje push větve a opakování exportu.
- Minimální sketch s importem aktuální p5js template úspěšně zpracoval tentýž Exporter. Template definuje `@P5.eval` a vytváří `new p5(sketch, div)`, tedy instanční kontext s prefixem `p5.`.
- `python tools/validate_course.py` prošel: ověřuje soubory, UTF-8, code fences, metadata a importy pilotu, sadu maker, samostatné blockquoty karet, nepřítomnost wrapperů, progresivní pomoc, WORLD a lokální odkazy.
- `git diff --check` prošel bez chyb mezer a konců řádků.

## Provedené opravy

- Pilot importuje sdílené `GAME-MACROS.md`; duplicita CSS a maker v lekci byla odstraněna.
- Sada maker je jednotná pro `PREDICT`, `EXPERIMENT`, `COMPLETE`, `BUG`, `MISSION`, `BONUS`, `QUIZ`, `BOSS`, `FLAG` a `XP`. Zachován je i kompatibilní alias `@JSQ.flagbox`.
- Vzhled karet používá rámeček, textový název a symbol aktivity, ne pouze barvu; akcenty mají variantu pro tmavé schéma.
- Karty nyní používají jen attribute comment a následující Markdown blockquote; v renderovatelném obsahu nezůstává párové `section` HTML ani uzavírací makro.
- Complete Code a Bug Hunt skrývají nápovědy i opravu za postupnou nativní disclosure strukturou. Kvízy používají nativní `[[?]]`, skryté řešení a tlačítka odemčená po prvním chybném pokusu.
- p5.js poznámka nyní ukazuje standardní `setup()`/`draw()` i LiaScript `p5.setup`/`p5.draw`.
- Boss výslovně končí problémem, že objekt opustí canvas; motivuje tím následující lekci o podmínkách bez zavedení `if` do WORLD 1.

## Známá omezení LiaScriptu

- `import:` načítá makra z veřejně dostupné raw URL. Dokud větev `experimental/pilot` neobsahuje pushnutou opravnou iteraci, pilot v Exporteru i Preview načte starší vzdálenou verzi `GAME-MACROS.md`.
- Lokální validátor není parser LiaScriptu. Neověří síťovou dostupnost importů, výsledný DOM ani vizuální rozvržení.
- p5js template je externí závislost; interaktivní canvas vyžaduje prohlížeč a dostupnost šablony/CDN.

## Co nelze automaticky hodnotit

- Zda student opravdu nejprve předpovídal, místo aby sketch okamžitě spustil.
- Zda samostatně vytvořil požadovaný pohyb v Mission nebo Boss.
- Zda rozumí rozdílu mezi `x += speed` a `x =+ speed`, pokud jej nedoplní vysvětlením nebo navazujícím úkolem.
- Přístupnost a srozumitelnost vizuálního renderu na konkrétním mobilu či ve čtečce obrazovky.

## Doporučení pro pilotní test

1. Pushni větev a znovu spusť Exporter i LiaScript Preview nad odkazem v `README.md`.
2. Ověř, že se každá karta vykreslí jako blockquote s rámečkem a nikde se nezobrazí technický tag.
3. Ověř, že Complete Code a Bug Hunt po prvním načtení ukazují jen zadání a kód; pomoc i řešení musí zůstat zavřené.
4. Ověř na desktopu i mobilu import maker, všechna tlačítka `@P5.eval`, Stop a vykreslení canvasu.
5. Nech několik studentů projít lekci bez nápovědy od učitele a zaznamenej, zda rozumějí prefixu `p5.` a chybě `x =+ speed`.

## Doporučený další krok

Po pilotním testu vyhodnoť pozorování podle sekce „Co se má ověřit po pilotu“ v `GAME-DESIGN.md`. Teprve potom rozhodni o rozsahu a podobě WORLD 2 — Decisions; v této větvi jej zatím nevytvářej.

## Seznam změněných souborů

- `AGENTS.md` — nové trvalé instrukce a validační postup.
- `TECHNICAL-NOTES.md` — zdroje a technické opravy.
- `PILOT-REPORT.md` — tento závěrečný report.
- `tools/validate_course.py` — lehká strukturální validace.
- `GAME-MACROS.md` — sjednocená sada atributových maker bez HTML wrapperů.
- `01-variables/01-moving-ball.md` — import sdílených maker, upřesnění p5.js, postupná pomoc a závěr Bossu.
- `AUTHORING-GUIDE.md` — aktuální zápis karet a nativní pomoc pro budoucí lekce.
- `README.md` — technický vstup do projektu, spuštění a validace.
