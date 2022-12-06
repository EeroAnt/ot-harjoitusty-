# Tuntikirjanpito


|  pvm  |  tunteja  |  kuvaus                   |
|:-----:|:---------:|---------------------------|
| 7.11 |3|tutustuttu tehtävänantoon, valittu aihe, tehty vaatimusmäärittely, luotu tuntikirjanpito |
|10.11|1|karkeimmista karkein tekstipohjainen UI tehty|
|11.11|2|kortin luominen (nimi ainoa attribuutti) ja lisääminen kokoelmaan onnistuu. Apin ihmettely alkanut|
|11.11|2|Apin ihmettely tuottanut tulosta. Nyt on CardData-luokka, josta saa kaiken tarpeellisen scryfallista lisättyä Card-luokan attribuuteiksi (nyt on nimi, cmc ja korttityyppi, mutta lisääminen on nyt helppoa). Erotin luokat, jotta jokaista korttia kohden tarvitsisi tehdä vain 1 api-kutsu.|
|12.11|3|Koitin ensiksi painia pickle-moduulin kanssa, jos olisin siihen saanut talteen kokoelmat, mutta päädyinkin sql-tietokantoihin. Nyt toimii tallennus|
|17.11|1|Korjasin kansiorakennetta lähinnä saadakseni omat moduulit toimimaan. Loin .db tiedoston, johon kerään ladatut kortit, jotta samoja kortteja ei tarvitse hakea aina uudestaam apin kautta|
|18.11|3|Tekstitiedostosta, joissa korttien nimit listattuna, cuben luominen onnistuu. Korttien tallentaminen omaan tietokantaan, jotta ei tarvitse aina tehdä api-kutsua, toimii|
|18.11|2|Testit aloitettu|
|21.11|3|rakennettu build.py, joilla alustaa ohjelma toimivaksi repon kopioinnin jälkeen, readme päivitetty, kansiorakennetta korjattu ja siitä syntyviä ongelmia fiksattu, changelog luotu|
|28.11|6|pylint aloitettu ja suodattimet rakennettu. Suodattimet tulostavat .html tiedoston, jossa sisältö jotenkin tarkkailtavissa|
|29.11|5|pitkän tutkailun jälkeen opin, että ilman javascriptiä (tai ainakaan pelkällä css) en saa kuvia niin sukkelasti, kuin toivoisin. Tavoitteena oli siis näyttää kortin kuva vain, kun kursori on tämän nimen kohdalla taulukossa, ja taulukon ulkopuolella. Sain joko tai. Toteutettu testejä vähän eteenpäin ja muutenkin tarkasteltu viikon tehtävänantoa. Pajaohjauksen avulla sain siirryttyä UI.py:n ajamisesta main.py:n ajamiseen ja muutenkin siistittyä yhtä ja toista.|
|5.12|2|palautteen huomioita tarkasteltu. Pakkaus- ja testirakenteet uusittu, ja laitettu toimimaan|
|6.12|10|cuben suodattimet saatu kokonaan toimimaan (siinä missä ovat ui:ssä) pylintin erheet saatu alle 5 ja viikon 5 tehtävät ainakin jotenkin tehtyä. Paljon tuli painittua että saisin unittest.mockin patch dekoraattorit toimimaan. en saanut|
|summa|31||
