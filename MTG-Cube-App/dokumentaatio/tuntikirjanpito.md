# Tuntikirjanpito


|  pvm  |  tunteja  |  kuvaus                   |
|:-----:|:---------:|---------------------------|
| 7.11 |3|tutustuttu tehtävänantoon, valittu aihe, tehty vaatimusmäärittely, luotu tuntikirjanpito |
|10.11|1|karkeimmista karkein tekstipohjainen UI tehty|
|11.11|2|kortin luominen (nimi ainoa attribuutti) ja lisääminen kokoelmaan onnistuu. Apin ihmettely alkanut|
|11.11|2|Apin ihmettely tuottanut tulosta. Nyt on CardData-luokka, josta saa kaiken tarpeellisen scryfallista lisättyä Card-luokan attribuuteiksi (nyt on nimi, cmc ja korttityyppi, mutta lisääminen on nyt helppoa). Erotin luokat, jotta jokaista korttia kohden tarvitsisi tehdä vain 1 api-kutsu.|
|12.11|3|Koitin ensiksi painia pickle-moduulin kanssa, jos olisin siihen saanut talteen kokoelmat, mutta päädyinkin sql-tietokantoihin. Nyt toimii tallennus|
|17.11|1|Korjasin kansiorakennetta lähinnä saadakseni omat moduulit toimimaan. Loin .db tiedoston, johon kerään ladatut kortit, jotta samoja kortteja ei tarvitse hakea aina uudestaam apin kautta|
