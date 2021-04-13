# Ohjelmistotekniikka, harjoitustyö

Harjoitustyö on elokuvien kirjallapito-sovellus. Käyttäjä voi etsiä elokuvia ja lisätä niitä tietokantaan. Elokuvien tiedoista löytyy esim. ohjaaja, julkaisupäivä ja imdb-rating. Halutessaan käyttäjä voi myös lisätä oman arvostelun ja katsomispäivän elokuvan tietoihin. Käyttäjä pystyy selaamaan katsomiaan elokuvian ja järjestelemään niitä niiden tietojen mukaan. 

## Nykyinen versio

Tämänhetkisen version tarkoitus on täyttää ensimmäisen viikon vaatimukset.

### Toiminnallisuus

Tämänhetkisen version ensisijainen tarkoitus on testata IMDB-Apin toiminnallisuutta. Ohjelmassa voi etsiä elokuvan nimen mukaan IMDB:stä elokuvia, mikä antaa hakutuloksena parhaimmin vastaavat elokuvat. Käyttäjä voi lisätä halutessaan jonkun näistä elokuvista tietokantaan, jossa säilytetään tietoja valituista elokuvista. Ohjelman sisällä ei ole vielä mahdollisuutta tutkia tietokannan sisältöä, mutta se on toiminnallinen. Sen sisältöä voi tutkia esim. DB Browser for SQLite -ohjelmalla. Tietokanta löytyy /data/-hakemistosta ensimmäisen ohjelman suorituksen jälkeen. Ohjelmaa käytetään (väliaikaisella) tekstikäyttöliittymällä. 

### Käyttöohje

Ennen ensimmäistä käyttökertaa riippuvuudet tulee asentaa komennolla: 
```bash
poetry install
```
Ohjelma suoritetaan komennolla:
```bash
poetry run invoke start
```
Testaus suoritetaan komennolla:
```bash
poetry run invoke test
```
Coverage-report luodaan komennolla:
```bash
poetry run invoke coverage-report
```
Tämän jälkeen juurihakemistosta löytyyy hakemisto htmlcov/, josta voi katsoa raportin.

### Tiedetyt ongelmat

Koska tämän viikon version tarkoitus on pääosin testata sqlite3:n ja IMDB-Apin toiminnallisuutta, vääränkaltaisia syötteitä ja virhetilanteita ei ole juuri otettu huomioon. Esim. kun ohjelma suoritetaan python shellistä, vain kirjaimet a-y ja numerot 0-9 toimivat. Backspace ja ääkköset tuottavat aina virheen. Tietokannan polku on myös suurinpiirtein kovakoodattu, jolloin ainoa tapa suorittaa ohjelma on silloin, kun working directory on juurihakemisto. poetry run invoke start -komento siis toimii, mutta jos haluaa suorittaa yksittäisä python-skriptejä src-hakemistosta, polku pitää manuaalisesti muuttaa config.py-tiedostossa. 

Luokkarakenteet ja sovelluslogiikka on tällä hetkellä erittäin keskeneräistä. Koska tekstikäyttöliittymä on väliakainen se ei ole erkaantunut sovelluslogiikasta millään tavalla.

Api-kutsut ovat rajoittuneet 5000:n päivässä. On epätodennäköistä, että tämä tulisis täyteen, mutta kannattaa silti ottaa huomioon. Haku vie aina yhden api-kutsun ja testaus kolme.

## Dokumentaatio

- [Työaikakirja](./documentation/tyoaikakirja.md)
- [Vaatimusmäärittely](./documentation/vaatimusmaarittely.md)

## Python-versio

Ohjelma on testattu Python-versioilla 3.6.9 ja 3.8.5. Ohjelman pitäisi pystyä toimimaan millä tahansa Pythonin versiolla joka on korkeampi kuin 3.6.0. 
