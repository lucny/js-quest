# JS Quest — Arena aktivity

Krátké průřezové výzvy se zařazují po příslušném WORLDu. Nejde o závod v rychlosti: dvojice porovnávají vysvětlení, čitelnost a nápady.

## LOOP ARENA — po WORLD 3

**Predict.** Kolikrát se vykreslí kruh a pro jaké hodnoty `index`?

```js
for (let index = 1; index < 5; index = index + 1) {
  p5.circle(index * 70, 120, 30);
}
```

**Bug Hunt.** Autor chtěl čtyři sloupce. Proč poslední zasahuje za zamýšlenou šířku?

```js
for (let column = 0; column <= 4; column = column + 1) {
  p5.rect(column * 80, 80, 60, 60);
}
```

**Challenge.** Vytvoř ornament z jednoho cyklu. Vyhrává nejoriginálnější obrazec, který spolužák dokáže vysvětlit pomocí počítadla.

## DATA ARENA — po WORLD 5

**Predict.** Jakou hodnotu vypíše poslední řádek?

```js
const temperatures = [18, 21, 19];
temperatures.push(23);
console.log(temperatures.length);
```

**Bug Hunt.** Proč poslední průchod nepatří do pole?

```js
const signals = ['A', 'B', 'C'];
for (let index = 0; index <= signals.length; index = index + 1) {
  console.log(signals[index]);
}
```

**Challenge.** Navrhni malé pole dat pro vlastní téma a funkci, která z něj vytvoří jednoduchý výstup. Porovnejte, zda názvy dat dávají smysl i bez vysvětlování autora.

## GAME ARENA — po WORLD 7

**Predict.** Co se změní po jednom kliknutí a co po podržení myši?

```js
let score = 0;
p5.mousePressed = function () {
  score = score + 1;
};
```

**Bug Hunt.** Proč se funkce spustí hned při registraci místo po kliknutí?

```js
button.addEventListener('click', changeScore());
```

**Challenge.** Ve dvojici navrhněte jednu novou herní mechaniku. Musí mít stav, vstup, pravidlo a viditelnou odezvu. Druhá dvojice má z popisu odhadnout, co se po interakci stane.
