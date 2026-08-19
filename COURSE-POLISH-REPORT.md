# Stav

Kurz prošel globální redakční, prezentační a didaktickou revizí na větvi `experimental/course-polish`.

# Opravené navigační problémy

`COURSE-MAP.md` je nyní manuální QA rozcestník. Všech 36 lekcí uvádí cestu, přímý GitHub zdroj a LiaScript Preview z aktuální větve.

# Opravené prezentační problémy

Významné jednorázové ukázky cyklů, podmínek, funkcí a callbacků byly převedeny na odsazené víceřádkové bloky. Nezaváděly se nové styly, fonty ani makra.

# Revize LEARN bloků

Významně bylo redigováno 29 studentských lekcí: klíčové LEARN bloky nyní vysvětlují problém, syntax, mentální model, běžnou chybu a návaznost. Doplněny byly zejména výklady indexu, `length`, změny property, myši, klávesnice, DOM, event listeneru a plánování Final Questu.

# Změny v AUTHORING-GUIDE

Přidán závazný LEARN BLOCK STANDARD a pravidlo pro čitelné víceřádkové ukázky. Průvodce také stanovuje bezpečné použití karet `@JSQ.*` bez inline attribute komentářů.

# Rozšíření validace / heuristik

Validátor selže při inline nebo neasociovaném `jsq-card` attribute commentu či kartě bez bezprostředního blockquotu. Varuje pro krátký LEARN a dlouhou jednorázovou konstrukci v code fence; po této revizi zůstává počet těchto varování nulový.

# Co stále vyžaduje ruční kontrolu

Po publikování větve ověř v LiaScript Preview všechny odkazy z COURSE-MAP, skutečné vykreslení attribute comments, dark mode, českou diakritiku v sidebaru, p5 canvas, WebDev click/input a úzký viewport.

# Doporučený další krok

Proveď manuální Preview QA podle `COURSE-TEST.md`. Případnou renderovací chybu opravuj ve sdílené infrastruktuře, ne lokální CSS záplatou v lekci.
