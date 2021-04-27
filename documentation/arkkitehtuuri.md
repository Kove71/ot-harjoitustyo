# Arkkitehtuurikuvaus

## Rakenne

![pakkauskaavio](https://user-images.githubusercontent.com/81042269/115456802-408a5380-a22c-11eb-8287-d82da45a5b87.png)

Pakkaus *ui* on vastuussa käyttöliittymäkoodista, *services* sovelluslogiikasta, *repositories* tietokannan ja *entities* sovelluksen käyttämistä tietokohteista.

## Sekvenssikaavio


![sekvenssi](https://user-images.githubusercontent.com/81042269/116272359-82b21880-a789-11eb-91fb-313106531215.png)

Sekvenssikaavio kuvaa tilannetta, jossa käyttäjä on *Search*-näkymässä, ja hakee elokuvan nimellä *Nomadland*. Käyttöliittymäluokka tekee kutsun request_search("nomadland") IMDBSearch-luokkaan. IMDBSearch tekee api-kutsun, joka palauttaa listan elokuvista, joka palautetaan käyttöliittymään. Käyttöliittymä päivittää listan elokuvista ja näyttää sen käyttäjälle.
