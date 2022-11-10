```mermaid
sequenceDiagram
  participant Main
  participant laitehallinto
  participant rautatietori
  participant ratikka6
  participant bussi244
  participant lippu_luukku
  participant kallen_kortti
  Main->>laitehallinto: laitehallinto = HKLLaitehallinto()
  laitehallinto->laitehallinto: laitehallinto._lataajat = []
  laitehallinto->laitehallinto: laitehallinto._lukijat = []
  Main->>rautatietori: rautatietori = Lataajalaite()
  Main->>ratikka6: ratikka6 = Lukijalaite()
  Main->>bussi244: bussi244 = Lukijalaite()
  Main->>laitehallinto: laitehallinto.lisaa_lataaja(rautatietori)
  activate laitehallinto
  laitehallinto->>laitehallinto: laitehallinto.lataajat.append(rautatietori)
  deactivate laitehallinto
  Main->>laitehallinto: laitehallinto.lisaa_lukija(ratikka6)
  activate laitehallinto
  laitehallinto->>laitehallinto: laitehallinto.lukija.append(ratikka6)
  deactivate laitehallinto
  Main->>laitehallinto: laitehallinto.lisaa_lukija(bussi244)
  activate laitehallinto
  laitehallinto->>laitehallinto: laitehallinto.lukija.append(bussi244)
  deactivate laitehallinto
  Main->>lippu_luukku: lippu_luukku = Kioski()
  Main->>kallen_kortti: kallen_kortti = lippu_luukku.osta_matkakortti("Kalle")
  kallen_kortti->>kallen_kortti: kallen_kortti.omistaja = "kalle"
  kallen_kortti->>kallen_kortti: kallen_kortti.pvm = 0
  kallen_kortti->>kallen_kortti: kallen_kortti.kk = 0
  kallen_kortti->>kallen_kortti: kallen_kortti.arvo = 0

```
