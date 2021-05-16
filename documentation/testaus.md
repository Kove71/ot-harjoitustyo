# Testausdokumentti

Sovellusogiikka ja ohjelman pysyväistallenus on testattu Unittestin avulla

## Yksikkötestaus

### Sovelluslogiikka

`TestIMDBSearch`-luokka testaa luokan `IMDBSearch` toimintaa eri syötteillä. request_search()-metodia kutsutaan kolmesti eri syötteillä. Toimivuus tarkastetaan katsomalla metodin palauttaman listan pituutta. request_title()-metodi testataan kovakoodatulla IMDB-id:llä. Metodi lisää elokuvan tiedot testaustietokantaan, jonka testaus tarkastaa. 

### Pysyväistallenus

`TestDatabase`- ja `TestInit`-luokat testaavat pysyväistallenuksen eri toimintoja. Testaus ei käsittele ohjelman varsinaista tietokantaa, vaan testausta varten luotua tietokantaa "fake_database.db". Testiluokassa `TestInit` testataan tietokannan alustusta. Se vuorollaan luo ja poistaa taulukon tietokannasta ja tarkistaa taulukoiden määrän. Testiluokassa `TestDatabase` testataan tietokannan käsittelyyn liittyviä toimintoja, eli `DatabaseActions`-luokkaa. Toimminot, joita testataan ovat elokuvan lisääminen tietokantaan ja elokuvien valitseminen tietokannasta. Kaikkia toimintoja ei testata, sillä testaus jostain syystä välillä lukitsee tietokannan, vaikka lukitusaikaa pidennettäisiin. 

### Testauskattavuus

![coverage](https://user-images.githubusercontent.com/81042269/118396715-63f0c480-b659-11eb-9941-e1ff07d2593b.png)

## Järjestelmätestaus

Ohjelma on järjestelmätestattu manuaalisesti.

### Asennus ja konfigurointi

Ohjelma on testattu Linux-ympäristössä. Ohjelmaa on testattu niin, että tietokanta löytyy jo valmiiksi, ja niin, että ohjelma luo ne itse.

### Toiminallisuus

Määrittelydokumentissa mainittu toiminallisuus on testattu ja ohjelma mukautuu moneen erilaiseen virheelliseen syötteeseen.
