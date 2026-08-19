# Stav

Kurz WORLD 1–9 je obsahově dokončen a připraven k manuálnímu QA v LiaScript Preview.

# Struktura kurzu

Devět WORLDů vede od proměnných přes rozhodování, cykly, funkce, pole, objekty a interakci k Web/DOM a samostatnému Final Questu.

# WORLDy

WORLD 1 Variables, WORLD 2 Decisions, WORLD 3 Loops, WORLD 4 Functions, WORLD 5 Arrays, WORLD 6 Objects, WORLD 7 Interaction, WORLD 8 Web/DOM a WORLD 9 Final Quest jsou v [COURSE-MAP.md](COURSE-MAP.md).

# Počet lekcí

36 studentských lekcí v 9 WORLD ech. Číslo vypočítal `python tools/course_metrics.py`.

# Didaktická architektura

Kurz používá problém → předpověď → experiment → stručné vysvětlení → úpravu → Mission → reflexi. P5 vizualizuje stav, WORLD 8 přirozeně přechází k DOM a WORLD 9 přenáší známé principy do vlastního projektu. Tři Arena aktivity umožňují průřezové opakování.

# Použité technologie

LiaScript, oficiální p5js template, oficiální WebDev template, globální `@JSQ` makra a systémový font stack s podporou češtiny.

# Aktivity

| Metrika | Počet |
|---|---:|
| PREDICT | 22 |
| EXPERIMENT | 9 |
| COMPLETE CODE | 11 |
| BUG HUNT | 17 |
| QUICK QUIZ | 14 |
| MISSION | 28 |
| BONUS | 6 |
| BOSS | 9 |
| FLAG | 47 |
| p5.js interaktivní blok | 54 |
| Web/DOM aktivita | 11 |
| čistý JS interaktivní blok | 0 |

Metriky jsou reprodukovatelné skriptem `python tools/course_metrics.py`. Čistý JS runner je záměrně 0: projekt neintrodukuje neověřený runtime jen kvůli metrice; čistý JS je používán v krátkých příkladech, p5 a WebDev zůstávají jedinými ověřenými živými runtimy.

# Výsledky validace

`python tools/validate_course.py` prošel po dokončení 68 Markdown souborů. Validátor kontroluje hlavičky, importy, code fences, task-list regresi, zakázaný multiple-choice/hint zápis a Mission scaffold.

Polishing navíc kontroluje bezpečné umístění `@JSQ` karet a raw `jsq-card` attribute comments. Nezávazná editorial heuristika upozorňuje na příliš krátký `LEARN` blok a dlouhou jednorázovou konstrukci uvnitř code fence.

# Výsledky LiaScript Exporteru

Oficiální LiaScript Exporter prošel pro všechny nové lekce WORLD 3–9, včetně 4 WebDev lekcí WORLD 8 a 5 lekcí WORLD 9. WORLD 1–2 zůstaly beze změny jako referenční implementace.

# Regresní kontrola

Studentské lekce neobsahují `<section`, `</section>`, `[[?]]`, `[[X]]`, `[[ ]]` ani LiaScript Task listy. Neobsahují lokální `font-family` ani `@font-face`.

# Známá omezení

Automatické kontroly neověří skutečné klikání, izolaci runtime, canvas, dark mode ani glyph fallback v postranní navigaci. Raw importy vyžadují publikovanou větev a připojení k síti.

# Co vyžaduje ruční test

Postupujte podle [COURSE-TEST.md](COURSE-TEST.md) a jednotlivých `WORLD*-TEST.md`: Preview, editor, Run/Stop, p5, WebDev, input, details, font, navigace, dark mode a mobilní šířka.

# Doporučený pilot se studenty

Pilotujte nejprve WORLD 1–3 s malou skupinou, pozorujte především předpovědi a práci s nápovědami. Potom ověřte přechod arrays/objects/interaction a samostatně otestujte WORLD 8 v cílovém prohlížeči. Final Quest vyhraďte na několik hodin s krátkou prezentací řešení.

# Doporučený další vývoj

Po manuálním QA opravujte případné renderovací problémy ve sdílených makrech nebo importech. Teprve po ověření výuky zvažte stabilní čistý-JS runtime nebo další obsah; nepřidávejte backend, účty ani persistentní leaderboard.
