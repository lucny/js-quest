<!--

@JSQ.styles
<style>
.jsq-card {
  border-left: 0.45rem solid #52616b;
  border-radius: 0.55rem;
  padding: 0.8rem 1rem;
  margin: 1rem 0 1.25rem 0;
  background: rgba(127,127,127,0.07);
}

.jsq-card strong:first-child {
  letter-spacing: 0.02em;
}

.jsq-predict { border-left-color: #2563eb; }
.jsq-experiment { border-left-color: #0891b2; }
.jsq-complete { border-left-color: #ea580c; }
.jsq-bug { border-left-color: #dc2626; }
.jsq-mission { border-left-color: #1d4ed8; }
.jsq-bonus { border-left-color: #7e22ce; }
.jsq-quiz { border-left-color: #ca8a04; }
.jsq-boss { border-left-color: #111827; }
.jsq-flag { border-left-color: #15803d; }

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
@JSQ.flagbox:    <section class="jsq-card jsq-flag">
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
@JSQ.flagbox
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
