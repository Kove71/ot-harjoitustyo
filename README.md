# Ohjelmistotekniikka, harjoitustyö

Harjoitustyö on elokuvien kirjallapito-sovellus. Käyttäjä voi etsiä elokuvia ja lisätä niitä tietokantaan. Elokuvien tiedoista löytyy esim. ohjaaja, julkaisupäivä ja imdb-rating. Halutessaan käyttäjä voi myös lisätä oman arvostelun ja katsomispäivän elokuvan tietoihin. Käyttäjä pystyy selaamaan katsomiaan elokuvian ja järjestelemään niitä niiden tietojen mukaan. 

## Nykyinen versio

Tämänhetkisen version tarkoitus on täyttää toisen viikon vaatimukset.

### Toiminnallisuus

Tämänhetkisessä versiossa on implentoitu käyttöliittymä, jonka avulla käyttäjä pystyy hakemaan elokuvia elokuvan nimen perusteella. Ohjelma palauttaa listaan parhaiten osuvat elokuvat ja käyttäjä voi lisätä haluamansa elokuvat omaan tietokantaan, johon tallenetaan elokuvan tiedot.

### Käyttöohje

Ennen ensimmäistä käyttökertaa riippuvuudet tulee asentaa komennolla: 
```bash
poetry install
```
Ohjelma tulee myös alustaa ennen ensimmäistä käyttökertaa komennolla:
```bash
poetry run invoke build
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
Tämän jälkeen juurihakemistosta löytyy hakemisto htmlcov/, josta voi katsoa raportin.

### Tiedetyt ongelmat

Virhetilanteet ovat edelleen huonosti käsiteltyjä, eli ohjelma pääosin olettaa kaiken toimivan hyvin ja käyttäjän olevan järkevä. Esim. jos koittaa lisätä elokuvan silloin, kun mitään ei ole valittuna, ohjelma tuottaa virheen. Jos haluaa tutkia tietokannan sisältöä pitää ne katsoa manuaalisesti haluamallaan ohjelmalla.

Etätyöpöydällä tietokanta ei toimi (locked), mutta käyttöliittymä toimii, ja ssh-melkillä tietokanta toimii, mutta käyttöliittymä ei.

Api-kutsut ovat rajoittuneet 5000:n päivässä. On epätodennäköistä, että tämä tulisi täyteen, mutta kannattaa silti ottaa huomioon. Haku vie aina yhden api-kutsun ja testaus kolme.

## Dokumentaatio

- [Työaikakirja](./documentation/tyoaikakirja.md)
- [Vaatimusmäärittely](./documentation/vaatimusmaarittely.md)

## Python-versio

Ohjelma on testattu Python-versioilla 3.6.9 ja 3.8.5. Ohjelman pitäisi pystyä toimimaan millä tahansa Pythonin versiolla joka on korkeampi kuin 3.6.0. 

## Huomioita pylintistä

Pylint ei jostain syystä löydä PyQt5 kirjastoja, joten olen laittanut näistä johtuvat ongelmat pois päältä. Samaten pylint tuottaa ongelmia kun muokkaan sys.pathia, jotta löytäisin omat moduulit, joten sekin on laitettu pois. Sen lisäksi ui/search_result_model.py on pyqt5:n oma luokkarakenne, jonka avulla voi käyttää QListView-luokkaa. Tämän takia se ei ole pep8 standardien mukainen. 
