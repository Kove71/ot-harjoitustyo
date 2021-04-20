# Arkkitehtuurikuvaus

## Rakenne

![pakkauskaavio](https://user-images.githubusercontent.com/81042269/115453654-8b09d100-a228-11eb-9d3a-79b9332446a4.png)

Pakkaus *ui* on vastuussa käyttöliittymäkoodista, *services* sovelluslogiikasta, *repositories* tietokannan (tarkoitus on siis siirtää database_actions.py uuteen repositories-hakemistoon, mutta polkujen kanssa on ollut ongelmia. Nykyinen rakenne vastaa kuvaa ilman repositories-pakkausta) ja *entities* sovelluksen käyttämistä tietokohteista.

