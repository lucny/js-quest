<!--

@JSQ.styles
<style>
.jsq-card {
  border: 1px solid var(--jsq-accent, currentColor);
  border-left: 0.45rem solid var(--jsq-accent, currentColor);
  border-radius: 0.5rem;
  padding: 0.85rem 1rem;
  margin: 1rem 0 1.25rem 0;
  background: transparent;
  color: inherit;
}

.jsq-card strong:first-child {
  letter-spacing: 0.02em;
}

.jsq-predict { --jsq-accent: #1d4ed8; }
.jsq-experiment { --jsq-accent: #0e7490; }
.jsq-complete { --jsq-accent: #c2410c; }
.jsq-bug { --jsq-accent: #b91c1c; }
.jsq-mission { --jsq-accent: #1e40af; }
.jsq-bonus { --jsq-accent: #6b21a8; }
.jsq-quiz { --jsq-accent: #a16207; }
.jsq-boss { --jsq-accent: #374151; }
.jsq-flag { --jsq-accent: #166534; }

@media (prefers-color-scheme: dark) {
  .jsq-predict { --jsq-accent: #93c5fd; }
  .jsq-experiment { --jsq-accent: #67e8f9; }
  .jsq-complete { --jsq-accent: #fdba74; }
  .jsq-bug { --jsq-accent: #fca5a5; }
  .jsq-mission { --jsq-accent: #bfdbfe; }
  .jsq-bonus { --jsq-accent: #d8b4fe; }
  .jsq-quiz { --jsq-accent: #fde68a; }
  .jsq-boss { --jsq-accent: #e5e7eb; }
  .jsq-flag { --jsq-accent: #86efac; }
}

.jsq-xp,
.jsq-badge {
  display: inline-block;
  border: 1px solid currentColor;
  border-radius: 999px;
  padding: 0.08rem 0.48rem;
  margin-left: 0.35rem;
  font-size: 0.78em;
  font-weight: 700;
  line-height: 1.35;
  vertical-align: middle;
}

.jsq-world {
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
</style>
@end

@JSQ.predict:    <section class="jsq-card jsq-predict">
@JSQ.experiment: <section class="jsq-card jsq-experiment">
@JSQ.complete:   <section class="jsq-card jsq-complete">
@JSQ.bug:        <section class="jsq-card jsq-bug">
@JSQ.mission:    <section class="jsq-card jsq-mission">
@JSQ.bonus:      <section class="jsq-card jsq-bonus">
@JSQ.quiz:       <section class="jsq-card jsq-quiz">
@JSQ.boss:       <section class="jsq-card jsq-boss">
@JSQ.flag:       <section class="jsq-card jsq-flag">
@JSQ.flagbox:    @JSQ.flag
@JSQ.end:        </section>

@JSQ.xp: <span class="jsq-xp">+@0 XP</span>

@JSQ.codeflag:  <span class="jsq-badge">🟦 CODE FLAG</span>
@JSQ.thinkflag: <span class="jsq-badge">🟨 THINK FLAG</span>
@JSQ.buildflag: <span class="jsq-badge">🟥 BUILD FLAG</span>
@JSQ.worldflag: <span class="jsq-badge">🏴 WORLD FLAG</span>

@JSQ.world: <span class="jsq-world">WORLD @0 · @1</span>

-->

# JS Quest — GAME-MACROS

Tento soubor definuje společnou prezentační vrstvu kurzu JS Quest.

> Záměrně **neimplementuje vlastní persistentní XP engine**. V pilotu jsou XP a vlajky didaktická metadata. Trvalé skóre se má později řešit přes SCORM/Moodle nebo samostatnou ověřenou integrační vrstvu.

## Použití jako LiaScript template

Po publikování souboru na veřejně dostupné raw URL jej vložte do hlavičky lekce:

```text
<!--
import: https://RAW-URL/GAME-MACROS.md
-->
```

Potom na začátku lekce jednou zavolejte:

```text
@JSQ.styles
```

> Poznámka: importy LiaScriptu načítají definice z hlavní hlavičky importovaného dokumentu. `GAME-MACROS.md` proto neimportuje p5js šablonu; p5js se importuje přímo v každé lekci, která jej potřebuje.

---

## Autorský zápis

Každá karta je párová: otevře se typovým makrem a uzavře `@JSQ.end`.

### Predict

```text
@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
>
> Kód zatím nespouštěj. Co podle tebe nastane?
@JSQ.end
```

### Experiment

```text
@JSQ.experiment
> **🧪 EXPERIMENT**
>
> Změň jedinou hodnotu a popiš, co se stalo.
@JSQ.end
```

### Complete Code

```text
@JSQ.complete
> **🔧 COMPLETE CODE** @JSQ.xp(2)
>
> Doplň řádek označený `TODO`.
@JSQ.end
```

### Bug Hunt

```text
@JSQ.bug
> **🐞 BUG HUNT** @JSQ.xp(2)
>
> Najdi a oprav chybu.
@JSQ.end
```

### Mission

```text
@JSQ.mission
> **🎯 MISSION** @JSQ.xp(4)
>
> Specifikace úlohy...
@JSQ.end
```

### Bonus

```text
@JSQ.bonus
> **💎 SIDE QUEST** @JSQ.xp(3)
>
> Dobrovolné rozšíření...
@JSQ.end
```

### Boss

```text
@JSQ.boss
> **🏆 BOSS** @JSQ.xp(10)
>
> Syntetická úloha...
@JSQ.end
```

### Vlajka

```text
@JSQ.flag
> @JSQ.buildflag
>
> Dokážu samostatně použít proměnné k řízení pohybu.
@JSQ.end
```

---

## p5js import

V lekci, která používá aktuální oficiální p5js template:

```text
<!--
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
```

Jednoduchý sketch:

````text
```js
p5.setup = function () {
  p5.createCanvas(600, 400);
};

p5.draw = function () {
  p5.background(240);
  p5.circle(100, 200, 40);
};
```
@P5.eval
````

Pro rozsáhlejší úlohy lze použít `@P5.project`.

---

## Návrhové omezení v0.1

Makra mají být:

- jednoduchá,
- čitelná i bez LiaScript rendereru,
- sémanticky konzistentní,
- bez závislosti na vlastním backendu,
- snadno nahraditelná pozdější verzí.

Do makra se v pilotu nemá přidávat automatické přičítání bodů jen proto, že student klikl na tlačítko nebo spustil kód.
