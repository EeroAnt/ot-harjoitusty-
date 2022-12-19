# Käyttöohjeet

Ohjelma koostuu kolmesta käyttöliittymästä.

Ensimmäisessä valitaan halutaanko:

 - aloittaa uuden cuben rakentaminen

 - ladata aiemmin tallennettu cube

 - ladata cube tekstitiedostosta /src/card_list_text_files hakemistosta. .txt liite on sisällytettävä syötteeseen

 - lopettaa ohjelma

Seuraavassa käyttöliittymässä käsitellään valittua cubea. Cubeen/cubelle/cubesta voi:

 - lisätä kortti. Uskoisin ohjelman tukevan kaikki nykyisiä korttimalleja, mutta voin olla väärässä ja uusia voi ilmestyä. Kortin lisäys on case insensitive, mutta kaksipuoleiset kortit kannattaa hakea etupuolen nimellä ja kortit, joissa yhdellä puolella 2 korttia, on haettava muodolla kortinnimi 1 // kortinnimi 2.

 - lisätä kortit tekstitiedostosta aiemmin mainitusta polusta aiemmin mainitulla tavalla.

 - poistaa kortti. Tämä on case sensitive. Kannattaa esim. etsiä poistettava kortti cuben tulosteesta ja varmistaa kirjoitusasu sieltä. Kaksipuolisilla korteilla etupuolen poistaminen poistaa myös takaosan.

 - printata cuben sisällöstä .html-tiedosto, joka sisältää taulukoituna olennaisimmat tiedot korteista.

 - printata cuben sisällöstä .html-tiedosto, jonka sisältönä kortit kuvina

 - suodattaa. Tämä avaa suodattamisen käyttöliittymän

 - tallentaa. Cube tallentaa nimensämukaisen .db-tietokannan /src/saved_cubes hakemistoon. temp on kehno nimi cubelle, koska suodatin käyttää tätä tietokantaa väliaikaistallentamiseen.

 - lopettaa tarkastelun. Tämä palaa ensimmäiseen valikkoon.

Suodattaminen onnistuu:

 - Kaikki numeeriset haut voi asettaa hakemaan joko vähintään, enintään tai tasan haetulla arvolla sisältävät tulokset.

 - Värillä. Väri suodatin kysyy, sisältyykö korttiin jokin haetuista väreistä

 - Väri-identiteetillä. Tämä suodatus jättää kortit pois, joiden väri-identiteettiin kuuluu muita, kuin haettuja värejä.

 - Mana-, power- ja toughness-arvoilla

 - Kortti tyypeillä. Toimii parhaiten, jos useamman tyypin kohdalla jokaisen suodattaa erikseen

Tämän lisäksi suodatteista voi ottaa tulosteet samaan tapaan, kuin koko cubestakin. Suodattajasta palattaessa cube palautuu suodattamattomaan muotoonsa.
