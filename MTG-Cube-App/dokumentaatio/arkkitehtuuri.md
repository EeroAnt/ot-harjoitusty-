# Arkkitehtuurikuva

Luokkien puolesta sovellus on todella simppeli. CardData-luokka sisältää yksittäisen kortin datan yhtenä sanakirjana. Se on haettu ensisijaisesti fetched_cards.db tietokannasta, toissijaisesti api-kutsulla scryfall.comin tietokannoista, jonka jälkeen lisättyy kyseiseen lokaaliin tietokantaan.
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

##Pakkauskaavio


```mermaid
 classDiagram
     Main --> UI
     UI --> CubeUI
     UI --> Saver_loader
     Saver_loader -- CubeUI
     Saver_loader -- /Saved_Cubes
     CubeUI --> Card
     Card --> CardData
     CubeUI --> filter
     CubeUI --> printer
     filter --> printer
     CardData --> /fetched_cards
     printer --> /Printed_lists
     class Saver_loader{
       save()
       load()
       load_from_file()
}
     class CardData{
       card_test()
}
     class filter{
       color_filter()
       color_id_filter()
       cmc_filter()
       type_filter()
       text_filter()
}
```