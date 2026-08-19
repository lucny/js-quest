# JS Quest — Answer Guide pro učitele

Tento materiál neodkazujte ze studentských lekcí. U otevřených úloh existuje více korektních řešení; níže jsou kontrolované principy, nikoli jediný povinný zápis.

# WORLD 1–2

- Variables: po změnách `x += speed` se sleduje aktuální hodnota `speed`; hlavní kvíz s `x = 7`, `speed = 4`, potom `-2` končí `11`.
- Decisions: `x > p5.width` je pro 580 při šířce 600 `false`; porovnání stejnosti používá `===`, ne přiřazení `=`.
- Bug Hunt: `x = 300` mění stav; `x === 300` vytváří boolean. Odraz vyžaduje změnit znaménko rychlosti při splnění hranice.

# WORLD 3 — Loops

- Počet průchodů plyne z počáteční hodnoty, podmínky a změny počítadla. Pro index pole `0…length - 1` je poslední platný index `length - 1`.
- Bug Hunt: `<= length` vede k neexistující položce; `while` musí změnit hodnotu, na níž závisí podmínka.
- Boss: Pattern Machine potřebuje alespoň jeden funkční cyklus a promyšlenou vazbu indexu na polohu, barvu nebo velikost.

# WORLD 4 — Functions

- Funkce seskupuje opakovaný krok; parametry mění vstup, `return` vrací hodnotu volajícímu místu.
- Bug Hunt: proměnná vytvořená uvnitř funkce není dostupná mimo ni; vrácení hodnoty musí být před místem, kde ji chceme použít.
- Boss: Procedural Scene kombinuje více vlastních funkcí; přijatelné jsou různé názvy i vizuální podoby.

# WORLD 5 — Arrays

- Pole začíná indexem 0, `length` je počet prvků a `push` přidává na konec.
- Bug Hunt: poslední index není `length`; při průchodu čteme `items[index]` jen pro `index < items.length`.
- Boss: Data Field používá pole a cyklus; korektní je libovolné funkční zobrazení dat bez chyby indexu.

# WORLD 6 — Objects

- Objekt drží související properties. `player.x` čte nebo mění x konkrétní entity; metoda patří objektu a pracuje s jeho stavem.
- Bug Hunt: nezaměňujte objekt s property ani `this.x` s neexistující volnou proměnnou.
- Boss: Creature System vyžaduje entity se stavem a průchod přes pole objektů; více správných struktur je přijatelné.

# WORLD 7 — Interaction

- `mouseX` a `mouseY` jsou aktuální poloha, click událost má změnit stav jednou a `keyIsDown` může řídit pohyb po snímcích.
- Bug Hunt: `addEventListener('click', change())` funkci hned zavolá; správně se předá `change`.
- Boss: Micro Game musí mít ovládání, cíl, změnu skóre a čitelný stav. Algoritmus kolize může být jednoduchý.

# WORLD 8 — Web / DOM

- `document.querySelector('#id')` najde prvek s daným id; `textContent` mění jeho text, `style.background` jeho styl.
- Bug Hunt: selector id začíná `#`; `addEventListener('click', addClick)` předává funkci, zatímco `addClick()` ji okamžitě spustí.
- Mission Kódový vzkaz: přečte `messageInput.value` a přes `if` vypíše zprávu pro prázdný i vyplněný input.
- Boss Vysílač úkolů: neprázdnou hodnotu přidá do `tasks`, vyčistí input a zavolá `renderTasks()`. Je přípustné použít alternativní funkci vykreslení.

# WORLD 9 — Final Quest

- Mapa projektu musí umět pojmenovat vstup, stav, pravidlo, výstup a jednu funkci. V objektu properties oddělují čárky.
- MVP je správně malé: musí předvést jednu skutečnou interakci nebo změnu stavu a její viditelný následek.
- Debugging: rychlé skóre vzniká proto, že `draw` běží opakovaně; jeden bod za klik patří do `p5.mousePressed`.
- Final Quest přijměte, pokud má proměnnou/stav, podmínku, cyklus, funkci, pole nebo objekt, interakci či DOM událost a čitelnou strukturu. Neexistuje jediné referenční řešení.
