# Käyttöohje

Lataa projektin viimeisin release README.md:stä

## Ohjelman käynnistys

Ennen kuin käynnistät ohjelman, asenna riippuvuudet komennolla:

```bash
poetry install
```

Alusta sitten tietokanta komennolla:

```bash
poetry run invoke build
```

Kun ohjelma on alustettu, ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Ohjelman käyttäminen

Kun ohjelma käynnistetään, käyttöliittymän pitäisi näyttää seuraavalta:

![initial_view](https://user-images.githubusercontent.com/81042269/117036900-94a63500-ad0e-11eb-8885-6711b864761c.png)

### Elokuvan haku
 
 Voit hakea elokuvia haluamallasi elokuvan nimellä:
 
![search_view](https://user-images.githubusercontent.com/81042269/117036920-996ae900-ad0e-11eb-8169-9e6229d1f2c1.png)

(HUOM, haut toimivat vain elokuvan nimellä. Näyttelijöiden tai ohjaajien perusteella ohjelma ei anna sopivia tuloksia)

Kun haluat lisätä elokuvan tietokantaan, valitse haluamasi elokuva listasta ja paina "Add movie"-nappia. Jos elokuvan lisääminen onnistuu, napin alapuolelle ilmestyy "Movie added!"-viesti.

### Tietokantanäkymä

Painamalla ylhäällä olevaa "Movies"-tabia voit vaihtaa näkymän tietokantanäkymään. Voit selata lisäämiäsi elokuvia ja niiden tietoja. Klikkaamalla sarakkeiden otsikoita voit järjestää tiedot niiden mukaan.

![table_view](https://user-images.githubusercontent.com/81042269/117036928-9b34ac80-ad0e-11eb-9894-b3db7c93680a.png)

Ohjelma tarjoaa kaksi toimintoa tietokannan muokkaukseen. "Remove"-nappi poistaa elokuvan tietokannasta. "Edit"-nappi avaa uuden ikkunan, kuten kuvassa näkyy.

![edit_view](https://user-images.githubusercontent.com/81042269/117036933-9cfe7000-ad0e-11eb-8869-09b10b1197c9.png)

Voit antaa elokuvalle oman arvion välillä 1-10, ja vaihtaa katsomispäivää (formaatti on yyyy-mm-dd). Päivän voi vaihtaa elokuvan julkaisupäivän ja nykyisen päivän välillä. Kun olet antanut haluamasi parametrit, elokuvan tiedot voi päivittää painamalla "Update"-nappia, joka myös sulkee muokkaus-ikkunan.

