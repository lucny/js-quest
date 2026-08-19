# Pokyny pro práci na JS Quest

## Didaktický účel

- Kurz je určen začínajícím středoškolským studentům.
- Primárním cílem je pochopení JavaScriptu, nikoli gamifikace.
- Student má principy pokud možno objevit vlastním experimentem.
- Preferuj didaktický cyklus: problém → předpověď → experiment → vysvětlení → modifikace → samostatná úloha → reflexe.
- Nepředkládej kompletní řešení dříve, než student dostane prostor pro samostatný pokus.
- Používej malé, čitelné a izolované příklady; nová úloha má měnit hlavně jeden nový koncept.

## Technologie a obsah

- Pokud lze JavaScriptový princip vhodně vizualizovat, preferuj p5.js; nepoužívej jej samoúčelně.
- Pravidelně používej i čistý JavaScript a v dalších částech kurzu DOM/Web API.
- V LiaScript p5js template je `p5.setup` / `p5.draw` instance-mode adaptace. V první relevantní lekci stručně odliš tuto podobu od běžného globálního p5.js `setup()` / `draw()`.
- Chyba je legitimní součást programování. Bug Hunt má učit čtení, formulaci hypotézy a diagnostiku cizího kódu.
- Mission ověřuje samostatné použití probíraného konceptu; Boss kombinuje již vysvětlené koncepty; Side Quest je vždy dobrovolný.
- XP jsou motivační metadata, nikdy známka ani automaticky ověřený důkaz porozumění.
- U otevřených aktivit COMPLETE, BUG, MISSION, BONUS a BOSS má student při prvním otevření vidět pouze zadání a editovatelný kód. Nápovědy a řešení schovej za postupné nativní disclosure prvky; první nápověda jen nasměruje, druhá pojmenuje koncept a řešení je poslední možnost.
- U LiaScript kvízů používej `[[?]]` pro postupné nápovědy a nativní blok řešení oddělený hvězdičkami. Podle smyslu úlohy nastav `data-hint-button` a `data-solution-button`.

## Autorské konvence

- Nové lekce musí dodržovat `AUTHORING-GUIDE.md` a didaktické zásady z `GAME-DESIGN.md`.
- Společné vizuální prvky a makra patří do `GAME-MACROS.md`, ne do jednotlivých lekcí.
- Neopakuj CSS nebo HTML maker v lekcích.
- Herní karta je atributový komentář před samostatným Markdown blokem, ne dvojice maker otevírající a zavírající HTML element.
- Zachovej maximální čitelnost Markdownových zdrojů i mimo renderer LiaScriptu.
- Nezaváděj do lekce koncept, který ještě nebyl vysvětlen. U tohoto pilotu nepřidávej `if`, odraz od okraje, pole ani objekty.

## Kontroly

Před předáním změn spusť:

```powershell
python tools/validate_course.py
git diff --check
git status --short
```

Volitelně lze po publikování importovaných souborů ověřit zpracování také oficiálním Exporterem; výstup patří do dočasného ignorovaného adresáře:

```powershell
npx --yes @liascript/exporter -i 01-variables/01-moving-ball.md -p . -f json -o .tmp/lesson
```

Po publikování větve otevři pilot také v LiaScriptu:

```text
https://liascript.github.io/course/?https://raw.githubusercontent.com/lucny/js-quest/experimental/pilot/01-variables/01-moving-ball.md
```

Lokální validátor ani Exporter nenahrazují manuální kontrolu rendereru; neověří chování canvasu ani odpovědi studentů.
