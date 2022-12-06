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
  participant Cube(kuutio)
  participant Card
  participant CardData
  Cube->>FuelTank: kuutio.add_card("Forest")
  Machine->>FuelTank: kone._tank = FuelTank()
  Machine->>FuelTank: kone._tank.fill(40)
  activate FuelTank
  FuelTank->>FuelTank: kone._tank.fuel_contents += 40  
  deactivate FuelTank
  Machine->>Engine: kone._engine = Engine(kone._tank)
  activate Engine
  Engine->>Machine: kone._engine._fuel_tank = kone._tank
  deactivate Engine
  Main->>Machine: call kone.drive
  Machine->>Engine: kone._engine.start()
  activate FuelTank
  Engine->>FuelTank: kone._engine._fuel_tank.consume(5)
  FuelTank->>FuelTank: kone._tank.fuel_contents -= 5
  deactivate FuelTank
  Machine->>Engine: running = kone._engine.is_running()
  Engine->>FuelTank: kone._tank._fuel_contents > 0
  FuelTank->>Engine: True
  Engine->>Machine: True
  Machine->>Engine: kone._engine.use_energy()
  activate FuelTank
  Engine->>FuelTank: kone._engine._fuel_tank.consume(10)
  FuelTank->>FuelTank: kone._tank.fuel_contents -= 5
  deactivate FuelTank
```
