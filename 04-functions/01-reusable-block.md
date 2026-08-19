<!--
author: JS Quest
version: 0.1.0
language: cs
comment: WORLD 4.1 opakovaný blok a funkce.
import: https://raw.githubusercontent.com/lucny/js-quest/experimental/course-completion/GAME-MACROS.md
import: https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md
-->
@JSQ.styles
# WORLD 4 — Pojmenovaná operace
@JSQ.world(4, Functions)
## ENTRY — Tři stejné roboty
Kód pro každého robota vypadá téměř stejně. Jak mu dát jméno a nepřepisovat ho?
@JSQ.predict
> **❓ PREDICT** @JSQ.xp(1)
> Co se stane, když program funkci pouze definuje, ale nezavolá ji?
[(X)] její tělo se ještě neprovede
[( )] zavolá se třikrát
[( )] canvas se zastaví
[( )] vznikne cyklus
## EXPERIMENT
```js
function drawRobot() {
  p5.rect(100, 120, 60, 80);
  p5.circle(130, 100, 45);
}

p5.setup = function () {
  p5.createCanvas(600, 300);
};

p5.draw = function () {
  p5.background(245);
  drawRobot();
};
```
@P5.eval
## LEARN
Funkce řeší opakovaný blok, kterému chceme dát jméno. Definice popisuje, co funkce umí; sama o sobě ještě nic nekreslí. Teprve volání ji nechá práci vykonat.

```js
function drawRobot() {
  p5.rect(100, 120, 60, 80);
}

drawRobot();
```

`function drawRobot()` vytváří pojmenovaný návod. Složené závorky obsahují příkazy návodu. Řádek `drawRobot()` dole návod použije. Závorky při volání znamenají „proveď funkci teď“. Když funkci jen definuješ, ale nezavoláš, její tělo se neprovede — to je častý důvod, proč na scéně nic není.
## COMPLETE CODE
@JSQ.complete
> **🔧 COMPLETE CODE** @JSQ.xp(2)
> Zavolej funkci ještě dvakrát, aby vznikli tři roboti.
```js
function signal() {
  p5.circle(100, 150, 40);
}
signal();
// TODO: Zopakuj volání funkce.
```
## MISSION
@JSQ.mission
> **🎯 MISSION: SYMBOL MACHINE** @JSQ.xp(4)
> Vytvoř funkci pro vlastní jednoduchý symbol a zavolej ji na scéně alespoň třikrát.
```js
p5.setup = function () {
  p5.createCanvas(600, 300);
};
p5.draw = function () {
  p5.background(245);
  // TODO: Pojmenuj a vytvoř funkci pro jeden symbol.
  // TODO: Zavolej ji na několika místech.
};
```
@P5.eval
<details><summary>Pomoc po vlastním pokusu</summary>Funkci definuj nad `p5.setup`; volání patří do `draw`.</details>
@JSQ.flag
> @JSQ.codeflag
> Umím definovat a zavolat jednoduchou funkci.
