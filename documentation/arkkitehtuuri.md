# Arkkitehtuurikuvaus

## Rakenne

![pakkauskaavio](https://user-images.githubusercontent.com/81042269/115456802-408a5380-a22c-11eb-8287-d82da45a5b87.png)

Pakkaus *ui* on vastuussa käyttöliittymäkoodista, *services* sovelluslogiikasta, *repositories* tietokannan (tarkoitus on siis siirtää database_actions.py uuteen repositories-hakemistoon, mutta polkujen kanssa on ollut ongelmia. Nykyinen rakenne vastaa kuvaa ilman repositories-pakkausta) ja *entities* sovelluksen käyttämistä tietokohteista.

