# JS Quest — GAME-DESIGN

**Stav:** pilot v0.1  
**Účel:** jednotná herní a didaktická gramatika interaktivního kurzu základů JavaScriptu v LiaScriptu.

---

## 1. Cíl kurzu

JS Quest není elektronická učebnice doplněná o kvízy. Je to posloupnost malých programátorských problémů, v nichž student:

1. nejprve předpovídá,
2. potom experimentuje,
3. formuluje pozorování,
4. dostane krátké vysvětlení,
5. upraví nebo doplní kód,
6. hledá chyby,
7. řeší samostatnou misi,
8. prokazuje porozumění,
9. získává XP, vlajky a achievementy.

Hlavní didaktická smyčka:

```text
PROBLÉM
  ↓
PŘEDPOVĚĎ
  ↓
EXPERIMENT
  ↓
POZOROVÁNÍ
  ↓
VYSVĚTLENÍ
  ↓
ÚPRAVA KÓDU
  ↓
DEBUGGING
  ↓
MISE
  ↓
DŮKAZ POROZUMĚNÍ
  ↓
VLAJKA
```

Základní zásada:

> Student má psát, měnit a analyzovat více kódu, než kolik ho pouze přečte.

---

## 2. Co gamifikace smí a nesmí dělat

Gamifikace má podporovat:

- pravidelnou aktivitu,
- zvědavost,
- experimentování,
- krátkodobé cíle,
- viditelný postup,
- dobrovolné překračování minima,
- spolupráci i krátké soutěže.

Gamifikace nesmí:

- trestat experimentování,
- odměňovat bezmyšlenkovité klikání,
- směšovat rychlost s porozuměním,
- vytvářet dlouhodobý žebříček, který po několika týdnech demotivuje slabší studenty,
- vydávat XP za známku,
- přidělovat body za grafický výstup, který systém ve skutečnosti neumí ověřit.

---

## 3. Tři vrstvy postupu

### 3.1 XP — aktivita

XP jsou jemná motivační měna. V pilotu jsou zobrazena v textu a slouží především k orientaci v náročnosti.

Doporučená hodnota:

| Aktivita | XP |
|---|---:|
| Predict | 1 |
| Quick Quiz | 1 |
| Complete Code | 2 |
| Bug Hunt | 2 |
| Mission | 3–5 |
| Bonus | 2–5 |
| Boss | 8–12 |

**Důležité:** v pilotu v0.1 nejsou XP považována za spolehlivě persistentní skóre. Trvalou evidenci řeší až pozdější SCORM/Moodle vrstva.

### 3.2 Vlajky — kompetence

Vlajka znamená zvládnutí konkrétní schopnosti.

Každý WORLD může mít:

- 🟦 **CODE FLAG** — umím konstrukci zapsat,
- 🟨 **THINK FLAG** — rozumím jejímu chování,
- 🟥 **BUILD FLAG** — umím ji samostatně použít,
- 🏴 **WORLD FLAG** — zvládl jsem syntetický Boss úkol.

Vlajka se nesmí získat pouze kliknutím. Musí být spojena alespoň s jedním důkazem porozumění: kvízem, vysvětlením, opravou programu nebo samostatnou úlohou.

### 3.3 Achievementy — vedlejší úspěchy

Achievement není povinný.

Příklady:

- 🐞 BUG HUNTER — opraveno 10 chybných programů,
- 🧠 PREDICTOR — série správných předpovědí,
- 🎨 GENERATOR — dokončena generativní výzva,
- 🛠 BUILDER — vytvořeno vlastní rozšíření,
- 💎 EXPLORER — dokončeno 5 bonusových úloh.

Achievementy mají umožnit vyniknout různým typům studentů, ne pouze nejrychlejším programátorům.

---

## 4. Typy aktivit

### ❓ PREDICT

Student nesmí nejprve program spustit. Má předpovědět výsledek.

Cíl: mentální simulace programu.

### 🧪 EXPERIMENT

Student mění hodnoty a sleduje důsledky. Nemusí existovat jediná správná odpověď.

Cíl: objevování významu syntaxe a parametrů.

### 🔧 COMPLETE CODE

Student dostane funkční nebo téměř funkční program s jasně vyznačeným místem `TODO`.

Cíl: doplnění jednoho izolovaného principu.

### 🐞 BUG HUNT

Student dostane záměrně chybný program.

Cíl: čtení kódu, formulace hypotézy a debugging.

### 🧩 CODE PUZZLE

Student rekonstruuje pořadí příkazů, propojuje části nebo doplňuje výraz.

Cíl: porozumění struktuře programu.

### ⚡ QUICK QUIZ

Krátká kontrola porozumění bez změny tématu.

Cíl: retrieval practice.

### 🎯 MISSION

Samostatnější úloha. Student už nedostává jediný řádek s `TODO`, ale specifikaci chování.

Cíl: přenos principu do nové situace.

### 💎 BONUS / SIDE QUEST

Dobrovolná úloha pro rychlejší nebo motivovanější studenty.

Cíl: diferenciace bez zvyšování povinného minima.

### 🏆 BOSS

Syntetická úloha na konci světa. Kombinuje několik dříve osvojených principů.

Cíl: kompetence, nikoli reprodukce syntaxe.

---

## 5. Standardní struktura jedné lekce

Každá referenční lekce má v tomto pořadí:

1. **ENTRY / Hook** — krátký problém, animace nebo překvapivý výsledek.
2. **PREDICT** — první mentální model.
3. **EXPERIMENT** — změna jedné věci.
4. **LEARN** — stručné vysvětlení principu.
5. **TRAINING** — 2–4 malé úlohy.
6. **BUG HUNT** — alespoň jedna typická chyba.
7. **MISSION** — samostatnější použití.
8. **PROOF OF UNDERSTANDING** — kvíz nebo vysvětlení.
9. **BONUS** — dobrovolná obtížnější větev.
10. **BOSS** — pokud lekce uzavírá větší celek.
11. **FLAGS** — rekapitulace kompetencí.

Ne každá krátká lekce musí mít Boss, ale každý WORLD musí mít alespoň jeden.

---

## 6. Mapa kurzu

### WORLD 0 — Boot
- příkaz,
- syntaxe,
- konzole,
- chyba,
- první vykreslení.

### WORLD 1 — Variables
- `let`,
- `const`,
- čísla,
- řetězce,
- boolean,
- přiřazení,
- operátory,
- stav programu.

### WORLD 2 — Decisions
- `if`,
- `else`,
- porovnání,
- `&&`,
- `||`,
- `!`.

### WORLD 3 — Loops
- `for`,
- `while`,
- počítadlo,
- vnořené cykly.

### WORLD 4 — Functions
- funkce,
- parametry,
- argumenty,
- `return`,
- scope.

### WORLD 5 — Arrays
- pole,
- index,
- `length`,
- `push`,
- průchod polem.

### WORLD 6 — Objects
- objekt,
- property,
- method,
- reference,
- lehký úvod do `class`.

### WORLD 7 — Interaction
- myš,
- klávesnice,
- události,
- stav aplikace.

### WORLD 8 — JavaScript + Web
- DOM,
- `querySelector`,
- události,
- formuláře,
- HTML/CSS/JS.

### WORLD 9 — Final Quest
- samostatná specifikace,
- plánování,
- implementace,
- debugging,
- prezentace řešení.

---

## 7. p5.js jako vizuální laboratoř

Pokud lze princip přirozeně vizualizovat, preferujeme p5.js:

| JavaScriptový koncept | Vizuální reprezentace |
|---|---|
| číslo | poloha, velikost, úhel |
| proměnná | měnící se stav objektu |
| boolean | zapnuto/vypnuto |
| `if` | reakce na podmínku |
| cyklus | opakovaný obrazec |
| pole | populace objektů |
| objekt | entita se stavem |
| funkce | opakovatelná operace |
| událost | interakce |

p5.js se ale nesmí stát synonymem JavaScriptu. Kurz pravidelně střídá:

```text
čistý JavaScript → p5.js → konzole → p5.js → DOM/WebDev
```

---

## 8. Soutěžní režimy

### Duel
Dvojice řeší stejný problém různým způsobem a následně porovnává řešení.

### Arena
Každý student dostane náhodný výběr z banky úloh.

### Bug Race
Skupiny hledají chyby v několika krátkých programech.

### Code Golf
Cílem je jednoduché nebo krátké řešení; hodnotí se až po správnosti a čitelnosti.

### Creative Challenge
Stejné omezené prostředky, různé výsledky.

### Weekly League
Krátkodobá soutěž, jejíž skóre se pravidelně resetuje.

### Team Quest
3–4 studenti rozdělují větší problém na části.

**Zakázaný výchozí režim:** celosemestrální veřejný žebříček všech studentů.

---

## 9. Hodnocení

Platí:

```text
XP ≠ známka
achievement ≠ známka
rychlost ≠ známka
```

Pro klasifikaci lze využít zejména:

- CODE FLAG,
- THINK FLAG,
- BUILD FLAG,
- WORLD FLAG,
- závěrečné projekty.

---

## 10. Technický model pilotu v0.1

Pilot odděluje tři věci:

### A. Interaktivní výuka
Řeší LiaScript:
- editovatelný obsah,
- kvízy,
- pokusy,
- nápovědy,
- interaktivní kód,
- lokální průběh.

### B. Canvas
Řeší oficiální p5js LiaScript template:
- `@P5.eval`,
- případně `@P5.project`,
- interaktivní canvas,
- terminál.

### C. Trvalá evidence
V pilotu se neimplementuje vlastní backend.

Pozdější cesta:
- export SCORM,
- Moodle,
- případně SCORM-Progress.

---

## 11. Důležitá vlastnost p5js šablony

Aktuální oficiální LiaScript p5js template používá **instance mode**.

Proto se v kurzu píše:

```js
p5.setup = function () {
  p5.createCanvas(600, 400);
};

p5.draw = function () {
  p5.background(240);
  p5.circle(100, 200, 40);
};
```

Nikoli standardní globální varianta:

```js
function setup() {
  createCanvas(600, 400);
}
```

Každá první p5.js lekce musí tento rozdíl vysvětlit. Studenti se zároveň musí naučit, že mimo LiaScript mohou běžně potkat globální syntaxi p5.js.

---

## 12. Acceptance criteria pilotu

Pilotní lekce „Pohybující se kulička“ je úspěšná, pokud:

- [ ] student spustí p5.js sketch bez externího IDE,
- [ ] student změní hodnotu a okamžitě vidí změnu,
- [ ] student vysvětlí rozdíl mezi inicializací a změnou proměnné,
- [ ] student použije `x += speed`,
- [ ] student opraví chybu `x =+ speed`,
- [ ] student samostatně vytvoří pohyb ve dvou osách nebo dva objekty s různými rychlostmi,
- [ ] student projde alespoň třemi různými typy aktivit,
- [ ] lekce obsahuje dobrovolnou větev pro rychlejší studenty,
- [ ] vizuální XP nejsou vydávána za automaticky ověřené skóre,
- [ ] kurz zůstává čitelný i jako Markdown.

---

## 13. Co se má ověřit po pilotu

Po prvním použití zaznamenat:

1. kolik času studenti tráví čtením versus editací,
2. zda rozumí `p5.` prefixu,
3. zda je XP vrstva motivuje nebo ruší,
4. zda je počet kvízů přiměřený,
5. zda slabší studenti zvládnou Main Quest,
6. zda rychlejší studenti skutečně využívají Side Quest,
7. které chyby se opakují,
8. zda je potřeba automatický judge pro část kódových úloh.

Teprve poté má smysl škálovat kurz na všechny WORLDy.
