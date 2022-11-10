```mermaid
 classDiagram
      Pelilauta "1" -- "*" Ruutu
      Pelinappula "1" -- "1" Ruutu
      Pelaaja "1" -- "1" Pelinappula
      Monopoli -- Pelilauta
      Monopoli -- Pelaaja
      Monopoli -- Nopat
      class Monopoli
      class Pelilauta{
      }
      class Ruutu{
      }
      class Pelinappula{
      }
      class Pelaaja{
      }
      class Nopat{
      }
```
