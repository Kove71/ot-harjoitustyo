# Arkkitehtuurikuvaus

## Rakenne

Korkean tason kuvaus ohjelman pakkausrakenteesta.

![pakkauskaavio](https://user-images.githubusercontent.com/81042269/117027075-037e9080-ad05-11eb-909e-10850fc0eecf.png)

Pakkaus *ui* on vastuussa käyttöliittymäkoodista, *services* sovelluslogiikasta, *repositories* tietokannasta ja *entities* sovelluksen käyttämistä tietokohteista.

## Sovelluslogiikka ja pysyväistallennus

Ohjelman sovelluslogiikka on hyvin yksinkertainen. IMDBSearch-luokka vastaa API-kutsuista, joita on kaksi. Molemmilla on oma metodinsa:

- `request_search(searchword)`

- `request_title(title)`

IMDBSearch käyttää apunaan SearchMovie- ja MovieDetails-tietoluokkia, joita käytetään elokuvien haussa ja niiden tietokantaan lisäämisessä. Tietoluokat ovat toisistaan riipumattomia. SearchMovie-luokkaan tallenetaan tiedot elokuvista, jotka haetaan hakusanalla. MovieDetails-luokkaan tallenetaan tiedot elokuvista, jotka lisätään tietokantaan. API-kutsujen ulkopuolella sovelluksen toiminta rajoittuu täysin tietokannan manipulointiin, josta vastaa DatabaseActions-luokka. Sen metodit ovat vastuussa kustakin SQL-kyselystä, kuten:

- `add_movie_to_database(selected_movie)`
- `select_movies()`
- `update_data(movie_id, review, watch_date)`
- `delete_row(movie_id)`

Koska sovelluksen toiminta pääosin rajoittuu tietokannan manipulointiin, pysyväistallenusta ja sovelluslogiikkaa ei voi erotella järkevästi.

## Sekvenssikaavio


![sekvenssi](https://user-images.githubusercontent.com/81042269/116272359-82b21880-a789-11eb-91fb-313106531215.png)

Sekvenssikaavio kuvaa tilannetta, jossa käyttäjä on *Search*-näkymässä, ja hakee elokuvan nimellä *Nomadland*. Käyttöliittymäluokka tekee kutsun request_search("nomadland") IMDBSearch-luokkaan. IMDBSearch tekee api-kutsun, joka palauttaa listan elokuvista, joka palautetaan käyttöliittymään. Käyttöliittymä päivittää listan elokuvista ja näyttää sen käyttäjälle.
