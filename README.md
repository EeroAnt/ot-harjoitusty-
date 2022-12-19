# MTG-Cuben HallinnointiApp

Sovelluksen tarkoitus on helpottaa hallinnoida omaa tietynlaista korttikokoelmaa, cubea. Tavoitteena on pystyä listaamaan kortit mielekkäästi tarkasteluun ja tarvittaessa suodattamaan listoja. Kokoelman muokkaaminen (niin kasvattaminen kuin pienentäminen) on tarpeen myös.

Kortteja voi lisätä yksittäisenä tai listana .txt-tiedoston avulla. Uusista korteista tehdään api-kutsu scryfall.com-sivulle ja sieltä haetaan relevantit tiedot ja kuva. Tiedot tallennetaan fetched_cards.db tiedostoon ja kuvat samaiseen kansioon. Cuben "tulostaminen" tuottaa html-sivun, johon listautuu cuben, mahdollisesti suodatettuna, sisältö taulukoituna muutamalla tiedolla.

### Dokumentaatio

 - [Vaatimusmäärittely](https://github.com/EeroAnt/ot-harjoitusty-/blob/main/MTG-Cube-App/dokumentaatio/vaatimusmaarittely.md)

 - [Tuntikirjanpito](https://github.com/EeroAnt/ot-harjoitusty-/blob/main/MTG-Cube-App/dokumentaatio/tuntikirjanpito.md)

 - [Changelog](https://github.com/EeroAnt/ot-harjoitusty-/blob/main/MTG-Cube-App/dokumentaatio/changelog.md)

 - [Arkkitehtuurikuvaus](https://github.com/EeroAnt/ot-harjoitusty-/blob/main/MTG-Cube-App/dokumentaatio/arkkitehtuuri.md)

 - [Release](https://github.com/EeroAnt/ot-harjoitusty-/releases/tag/viikko5)

 - [Testaus](https://github.com/EeroAnt/ot-harjoitusty-/blob/main/MTG-Cube-App/dokumentaatio/Testaus.md)

### Asennus ja käyttöohje

MTG-Cube-App kansiossa tulee ajaa komennot

 - poetry install

 - poetry run invoke build

Tämän jälkeen ohjelman voi ajaa komennolla

 - poetry run invoke start

Testit ajetaan

 - poetry run invoke test

Testikattavuusraportti luodaan komennolla

 - poetry run invoke coverage-report


Manuaaliseen testailuun ja tutkimiseen:

scryfall.com sivustolla on painike "random card", jos haluaa testata eri korttien lataamista
mountain, black lotus, elvish piper on myös luultavasti toimivia esimerkkejä. Välttämättä jokaisen kortin lataaminen ei vielä toimi, koska voi olla hassuja erikoismerkkejä nimissä
Korttien lisääminen taitaa olla ainoa tekstisyöte, joka ei ole case sensitive, listoista ladattaessa on muistettava .txt pääte, mutta tallennettuja cubeja haettaessa tulee .db jättää syötteestä pois.
testilista.txt löytyy jo jos haluaa testata listan lataamista
Kaksipuoleisten korttien kohdalla ohjelma toimii parhaiten, jos lisää/poistaa etupuolen. Tällöin automaattisesti myös takapuolisko seuraa perästä. Aiemmin ladatuilla korteilla ei tule ongelmia, jos lisää takapuoliskon ensin. Etupuoliskon voi lisätä jälkikäteen, mutta api-kutsun kautta tehdessä on tärkeä kutsua etupuoli, koska se rakentaa kirjauksen oikein fetched_cards-tietokantaan.
Kaksipuoliset kortit siis haeataan vain etupuolen nimillä, tuplakortit (kaksi korttia yhdellä sivulla) haetaan 'nimi1 // nimi2' mallin mukaisesti.
