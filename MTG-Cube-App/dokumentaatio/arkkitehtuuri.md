# Arkkitehtuurikuva

Luokkien puolesta sovellus on todella simppeli. CardData-luokka sisältää yksittäisen kortin datan yhtenä sanakirjana ja yhtenä .png-tiedostona. Se on haettu ensisijaisesti fetched_cards.db tietokannasta, toissijaisesti api-kutsulla scryfall.comin tietokannoista, jonka jälkeen lisättyy kyseiseen lokaaliin tietokantaan.
Card luokka tekee CardDatan tiedosta Card-olion, joilla oleelliset tiedot attribuutteina. Cube on kokoelma Card-olioita. Sen attribuutteina ovat nimi, lista siihen kuuluvista korteista ja niiden nimistä. 


## Luokkakaavio

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

Toiminnallisuus käy vähän monimutkaisemmaksi. main.py käynnistää UI:n, joka kysyy ladataanko tallennettu cube, luodaanko uusi cube tyhjästä vai listasta (.txt-tiedosto). Tämän jälkeen siirrytään valitun cuben kanssa CubeUI:hin ja sieltä voi tällä hetkellä:
 - lisätä kortteja
 - tallentaa cuben omana .db tiedostona (joka on sitten ladattavissa myöhemmin)
 - tulostaa cubesta .html tiedosto sisällön tarkastelua varten (kuvat tähän mukaan joskus)
 - suodattaa cuben sisältöä ja suodatetun sisällön voi tulostaa

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
