# Arkkitehtuurikuva

## Luokkakaavio

Luokkien puolesta sovellus on todella simppeli. CardData-luokka sisältää yksittäisen kortin datan yhtenä sanakirjana ja yhtenä .png-tiedostona. Se on haettu ensisijaisesti fetched_cards.db tietokannasta, toissijaisesti api-kutsulla scryfall.comin tietokannoista, jonka jälkeen lisättyy kyseiseen lokaaliin tietokantaan.
Card luokka tekee CardDatan tiedosta Card-olion, joilla oleelliset tiedot attribuutteina. Cube on kokoelma Card-olioita. Sen attribuutteina ovat nimi, lista siihen kuuluvista korteista ja niiden nimistä. 

```mermaid
 classDiagram
      Cube "1" <-- "*" Card
      Card "1" -- "1" CardData
      class Card{
        name
        colors
        color_id
        cmc
        mana_cost
        type
        keywords
        text
        img_uri
        p_t
        name_for_img          
      }
      class Cube{
        name
        collection
        card_names
      }
      class CardData{
        card_dict
      }
```

## Pakkauskaavio

```mermaid
 classDiagram
     Main --> UI
     UI --> CubeUI
     UI --> Saver_loader
     Saver_loader <|--|> CubeUI
     Saver_loader <|--|> Saved_Cubes
     CubeUI <|--|> Card
     Card  <|--|> CardData
     CubeUI --> filter
     CubeUI --> printer
     filter --> printer
     CardData --> fetched_cards
     printer --> Printed_lists
     class Saver_loader{
       save()
       load()
       load_from_file()
}
     class CardData{
       card_test()
}
     class CubeUI{
       add_card()
}
     class filter{
       color_filter()
       color_id_filter()
       cmc_filter()
       type_filter()
       text_filter()
}
     class fetched_cards{
       fetched_cards.db
       .png files
}
     class Printed_lists{
       .html files
}
```
## Sovelluslogiikka

Sovellus koostuu korttikokoelmista (cube) ja korteista. Cubeja voi muokata, tarkastella ja tallentaa sekä ladata. Cubet tallennetaan .db-tiedostoina ja kortit ovat siellä yksittäisiä rivejä.

Korttia haettaessa ensimmäistä kertää ohjelma tekee api-kutsun api.scryfall.comiin ja hakee sieltä json-objektin, joka sisältää kattavasti kortin tiedot. Sovellus poimii siitä itselleen olelliset palat ja luo rivin fetched_cards.db-tiedostoon ja lataa kortin kuvan talteen. Myöhemmillä kerroilla samaa korttia hakiessa se noudetaan suoraan tästä tiedostosta.

Cuben tarkastelu tarkoittaa tällä hetkellä tulosteen tekemistä sen sisällöstä. Tulosteet ovat .html tiedostoja, jotka sisältävät joko korttien kuvat tai korttien olennaisemmat tiedot taulukoituna. Tämän lisäksi cuben sisällöstä voidaan suodattaa osia erikseen tarkasteltavaksi.

Suodattimien käyttöliittymän avaaminen luo aluksi väliaikaisen cuben, joka on kopio alkuperäisestä. Tätä kopiota voi suodattaa muutamalla eri vaihtoehdolla ja joka vaiheessa voi ottaa tulosteen ulos. Kun suodattelu lopetetaan, sovellus lataa suodattamattoman cuben takaisin. Suodattaminen tapahtuu käytännössä sql-komennoilla ja tallentamalla väliaikaisen kopion päälle suodatetut listat.

Ohjelman toimii tekstipohjaisella käyttöliittymällä, koska hienompi ei ole tarpeellinen, enkä osaa tehdä sellaista. Käyttöliittymä koostuu kolmesta tasosta. Ensimmäisessä valitaan cube käsiteltäväksi (uusi tai vanha). Toisessa on cuben käyttöliittymä, missä voi lisätä tai poistaa kortteja, tulostella, tallentaa tai suodattaaa. Viimeinen on suodattamisen käyttöliittymä, jossa avataan eri vaihtoehdot suodattamiseen.

## Sekvenssikaavio

```mermaid
sequenceDiagram
  participant Cube
  participant Card
  participant CardData
  participant fetched_cards.db
  Cube->>Cube: kuutio.add_card("Forest")
  Cube->>CardData: Initial_load = CardData("Forest")
  CardData->>fetched_cards.db: Check if card has been used before
  fetched_cards.db->>CardData: True
  CardData->>CardData: Initial_load.card_dict = data_from_db("Forest")
  CardData->>Cube: CardData("Forest")
  Cube->>Cube: Checks if "Forest" in it
  Cube->>Cube: True
  Cube->>Cube: Print("Forest on jo cubessa")
```
