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
- Stav: čeká na WORLD 7; před tvorbou ověřit dostupnou LiaScript Web/DOM infrastrukturu.

# WORLD 9

- Plán: volba projektu → rozklad → MVP → debugging → rozšíření → Final Quest.
- Stav: čeká na WORLD 8.

# Globální QA

Po každém WORLDu: validace, Exporter pro každou lekci, regresní search a didaktický audit. Na konci metriky, COURSE-TEST, COURSE-REPORT, Teacher a Answer guide.

# Otevřené problémy

- Web/DOM prostředí musí být před WORLD 8 ověřeno oficiální dokumentací/template.
- Finální vizuální kontrola vyžaduje publikovanou raw větev a LiaScript Preview.

# Rozhodnutí

- WORLD 3–7 budou používat existující p5.js template jen tehdy, když vizualizace zjednoduší koncept.
- Kvízy zůstávají single-choice `[( )]` / `[(X)]`; nápovědy a řešení jsou `details`.

# Dokončeno

- Založena větev `experimental/course-completion`.
