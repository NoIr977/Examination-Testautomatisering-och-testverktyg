### 1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?

**Enhetstester** validerar att enskilda delar av systemet fungerar som de ska.

**Integrationstester** validerar hur olika delar av systemet fungerar tillsammans och kommunicerar med varandra.

**Regressionstester** validerar att allt som fungerade i systemet innan förändringar (t.ex. nya funktioner eller uppdateringar) fortfarande fungerar efter förändringarna.

**Prestandatester** validerar hur snabbt och stabilt systemet fungerar, till exempel om en webbsida fungerar lika bra med 1 användare som med 1000 användare samtidigt, när belastningen på systemet ökar.


### 2. Beskriv hur det går till när man arbetar med TDD.

TDD betyder Test Driven Development.

Man börjar med att skriva ett test utifrån kraven. Först kör man testet och ser att det inte fungerar (Red).

Sedan skriver man koden som behövs för att testet ska fungera (Green).

Efter det förbättrar man koden om det behövs (Refactor) och testar igen för att kontrollera att allt fortfarande fungerar.

Så fortsätter man tills alla tester är gröna.


### 3. Beskriv hur BDD skiljer sig från TDD.

BDD betyder Behavior Driven Development.

I BDD börjar man med att beskriva systemets beteende utifrån användarens perspektiv, till exempel med user stories.

Utifrån dessa skriver man testscenarier med Given, When och Then.

Skillnaden är att TDD fokuserar mer på att testa och utveckla koden, medan BDD fokuserar på hur systemet ska fungera för användaren.


### 4. Vilka sorters tester skulle du vilja använda? Motivera ditt val.

Jag skulle använda BDD med Playwright för att testa frontend, eftersom man ska tänka ur användarens perspektiv och kontrollera att sidan fungerar som förväntat.

Jag skulle också använda enhetstester och integrationstester för backend, för att kontrollera att olika metoder fungerar och att de fungerar tillsammans.

Efter utvecklingen skulle jag göra användbarhetstester, eftersom jag vill kontrollera att riktiga användare kan använda sidan på ett enkelt sätt.

Jag skulle även använda prestandatester för att kontrollera att sidan fungerar snabbt och stabilt, även när många användare använder den samtidigt.