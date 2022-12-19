# Changelog

## Viikko 3:

- Käyttäjä voi luoda, tallentaa ja ladata cuben
- Cubeen voi lisätä kortteja ja aiemmin ladatut kortit löytyvät paikallisesta .db tiedostosta
- testailu on aloitettu


## Viikko 4:

- Cuben sisältöä voi suodattaa ja suodatetusta tai suodattamattomasta cubesta saa hmtl-tulosteen
- Kortin hakeminen apikutsulla hakee myös png-kuvan kortista talteen. Se on aika iso (yli 1mb), joten saatan vaihtaa kevyempään. Toki testaillessa varmaan riittänee muutama kymmenen korttia ja omaan käyttöön taas ei niin väliä.
- pylint otettu käyttöön ja suurinosa erheistä on korjattu. Jeesiä tarvitaan loppuihin.
- Tekstitiedostosta luodut Cubet sietävät huonoja rivejä ja prosessi printtaa listan riveistä, joita ei saatu cubeen lisättyä.

## Viikko 5:

- Suodatus toimii nyt paremmin. Tulostus vaihtoehdoiksi on muodostunut joko taulukon tai kuvien tulostaminen
- p_t arvo jaettu power- ja toughness-arvoiksi. Lähinnä suodatuksen mahdollistamiseksi

## Viikko 6:

- Korttien lisääminen könttänä tekstitiedostosta olemassaolevaan cubeen onnistuu

## Viikko 7:

- Kaksipuolisten korttien lisääminen ja poistaminen onnistuu.
