```mermaid
 classDiagram
      Pelilauta "1" -- "*" Ruutu
      Pelinappula "*" -- "1" Ruutu
      Pelaaja "1" -- "1" Pelinappula
      Monopoli -- Pelilauta
      Monopoli -- Pelaaja
      Monopoli -- Nopat
      Monopoli -- Aloitusruutu
      Monopoli -- Vankila
      Ruutu -- Toiminto
      Sattuma -- Sattumakortti
      Yhteismaa -- Yhteismaakortti
      Sattumakortti -- Toiminto
      Yhteismaakortti -- Toiminto
      Katu "1" -- "4" Talo
      Katu "1" -- "1" Hotelli
      Katu -- Pelaaja
      Ruutu -- Aloitusruutu
      Ruutu -- Vankila
      Ruutu -- Sattuma
      Ruutu -- Katu
      Ruutu -- Yhteismaa
      class Monopoli
      class Pelilauta
      class Ruutu
      class Pelinappula
      class Pelaaja{
          rahaa
      }
      class Nopat
      class Aloitusruutu
      class Vankila
      Class Sattuma
      Class Yhteismaa
      Class Asema
      Class Laitos
      class Katu{
          kadunnimi
          omistaja
      }
      Class Sattumakortti
      Class Yhteismaakortti
      Class Toiminto
      Class Talo
      Class Hotelli
```
