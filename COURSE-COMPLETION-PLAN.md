# Cíl

Dokončit JS Quest od WORLD 3 do WORLD 9 při zachování ověřené infrastruktury WORLD 1–2.

# Výchozí stav

Větev `experimental/course-completion` vychází z checkpointu WORLD 2. Platí zákaz LiaScript Tasks, `[[...]]` quiz/hint syntaxe, párových HTML wrapperů a lokálních fontových pravidel.

# WORLD 3

- Plán: opakování → `for` → index → mřížka → bezpečný `while` → Pattern Machine.
- Stav: dokončeno; validátor, Exporter, regresní audit a checkpoint commit.
- Kontroly: validátor, Exporter, regresní search, checkpoint commit.

# WORLD 4

- Plán: opakovaný blok → funkce → parametry → return/scope → Procedural Scene.
- Stav: dokončeno; validátor, Exporter, regresní audit a checkpoint commit.

# WORLD 5

- Plán: hodnoty → pole → index/length → push → data + cyklus → Data Field.
- Stav: dokončeno; validátor, Exporter, regresní audit a checkpoint commit.

# WORLD 6

- Plán: související proměnné → object literal → properties/method → pole objektů → Creature System.
- Stav: dokončeno; validátor, Exporter, regresní audit a checkpoint commit.

# WORLD 7

- Plán: myš/klávesnice → událost → stav → jednoduchá hra → Micro Game.
- Stav: dokončeno; validátor, Exporter, regresní audit a checkpoint commit.

# WORLD 8

- Plán: HTML → selector → změna DOM → click/input → malá webová aplikace.
- Stav: dokončeno; infrastruktura ověřena, validátor, Exporter, regresní audit a checkpoint commit.
- Infrastruktura: oficiální template `liaTemplates/WebDev` s `@WebDev.HTML_JS`; JavaScript se spouští až po vložení HTML do izolovaného výstupu.

# WORLD 9

- Plán: volba projektu → rozklad → MVP → debugging → rozšíření → Final Quest.
- Stav: dokončeno; validátor, Exporter, regresní audit a checkpoint commit.

# Globální QA

Dokončeno: validace, Exporter pro každou novou lekci, regresní search, didaktický audit, metriky, COURSE-TEST, COURSE-REPORT, Teacher Guide a Answer Guide. Čeká pouze manuální Preview publikované větve.

# Otevřené problémy

- Finální vizuální kontrola vyžaduje publikovanou raw větev a LiaScript Preview.

# Rozhodnutí

- WORLD 3–7 budou používat existující p5.js template jen tehdy, když vizualizace zjednoduší koncept.
- Kvízy zůstávají single-choice `[( )]` / `[(X)]`; nápovědy a řešení jsou `details`.
- WORLD 8 používá ověřený WebDev template, nikoli lokální HTML/DOM runtime.

# Dokončeno

- Založena větev `experimental/course-completion`.
- WORLD 3–9 jsou dokončeny v samostatných checkpointech.
- Vytvořeny Arena aktivity, učitelská dokumentace, Answer Guide a globální QA materiály.
- Celokurzová automatická QA a Exporter prošly; stav je READY FOR MANUAL QA.
