<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 9.1 Volba Final Questu.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 9 — Vyber problém
@JSQ.world(9, Final Quest)

## PROBLÉM

Už nečekáš na další příkaz. Teď rozhoduješ, jaký problém bude tvůj program řešit.

## PREDICT
@JSQ.predict
> Než vybereš projekt, napiš jednu větu: co má uživatel po první minutě umět nebo vidět?

## ČTYŘI CESTY

Vyber jednu cestu, nebo navrhni vlastní variantu podobného rozsahu.

- **A — interaktivní p5 hra:** hráč ovládá objekt a sleduje skóre nebo stav.
- **B — generativní vizualizace:** cykly, funkce a náhoda vytvářejí obrazec.
- **C — datová miniaplikace:** pole nebo objekty drží data, program je zobrazí a změní.
- **D — DOM webová aplikace:** input, tlačítko a událost mění stav stránky.

## QUICK QUIZ
@JSQ.quiz
> Která otázka pomůže vybrat realistické MVP?

[( )] Jak přidám co nejvíce funkcí hned první den?
[(X)] Jaký nejmenší funkční zážitek může uživatel vyzkoušet?
[( )] Který projekt bude mít nejvíce řádků?

## MISSION
@JSQ.mission
> **MISSION: VIZITKA PROJEKTU** @JSQ.xp(4)
> Spusť výchozí vizitku. Doplň název svého projektu a jednu krátkou větu o tom, co uživatel udělá.

```js
const project = {
  // TODO: Pojmenuj vlastní projekt.
  title: 'Můj projekt',
  // TODO: Popiš jednu hlavní akci uživatele.
  goal: 'Uživatel něco vyzkouší.'
};

p5.setup = function () {
  p5.createCanvas(620, 220);
  p5.background(239, 246, 255);
  p5.fill(30, 64, 175);
  p5.textSize(28);
  p5.text(project.title, 30, 70);
  p5.fill(31, 41, 55);
  p5.textSize(18);
  p5.text(project.goal, 30, 120, 560);
};
```
@P5.eval

<details><summary>Nápověda 1</summary>Začni jednou konkrétní činností uživatele: klikne, pohne se, zadá hodnotu nebo sleduje obrazec.</details>
<details><summary>Nápověda 2</summary>Text měň u vlastností <code>title</code> a <code>goal</code>, ne uvnitř kreslicí funkce.</details>
<details><summary>Možné řešení</summary>Správných vizitek je mnoho; důležité je, aby název a cíl odpovídaly zvolené cestě.</details>

@JSQ.flag
> @JSQ.thinkflag
> Umím vybrat malý problém, který má pro uživatele jasný výsledek.
