import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortilla_rahaa = Maksukortti(1000)
        self.maksukortilla_ei_rahaa = Maksukortti(10)

    def test_alkukassa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_alkuun_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_alkuun_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_osto_kateisella_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)

    def test_edullisten_maara_onnistuneen_kateisoston_jalkeen_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kassassa_rahaa_oikein_onnistuneen_edullisen_kateisoston_jalkeen(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukkaan_osto_kateisella_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)

    def test_maukkaan_maara_onnistuneen_kateisoston_jalkeen_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kassassa_rahaa_oikein_onnistuneen_maukkaan_kateisoston_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_ei_tarpeeksi_rahaa_vaihtorahat_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_ei_tarpeeksi_rahaa_lounaiden_maara__edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_ei_tarpeeksi_rahaa_kassan_saldo_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_ei_tarpeeksi_rahaa_vaihtorahat_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_ei_tarpeeksi_rahaa_lounaiden_maara_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_ei_tarpeeksi_rahaa_kassan_saldo_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_onnistunut_korttiosto_summa_veloitettu_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortilla_rahaa)
        self.assertEqual(str(self.maksukortilla_rahaa),"Kortilla on rahaa 7.60 euroa")

    def test_onnistunut_korttiosto_paluuarvo_True_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortilla_rahaa), True)

    def test_onnistunut_korttiosto_lounaiden_maara_ok_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortilla_rahaa)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_epaonnistunut_korttiosto_kortin_saldo_ok_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortilla_ei_rahaa)
        self.assertEqual(str(self.maksukortilla_ei_rahaa),"Kortilla on rahaa 0.10 euroa")

    def test_epaonnistunut_korttiosto_paluuarvo_False_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortilla_ei_rahaa), False)

    def test_epaonnistunut_korttiosto_lounaiden_maara_ok_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortilla_ei_rahaa)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_onnistunut_korttiosto_summa_veloitettu_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortilla_rahaa)
        self.assertEqual(str(self.maksukortilla_rahaa),"Kortilla on rahaa 6.00 euroa")

    def test_onnistunut_korttiosto_paluuarvo_True_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortilla_rahaa), True)

    def test_onnistunut_korttiosto_lounaiden_maara_ok_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortilla_rahaa)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_epaonnistunut_korttiosto_kortin_saldo_ok_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortilla_ei_rahaa)
        self.assertEqual(str(self.maksukortilla_ei_rahaa),"Kortilla on rahaa 0.10 euroa")

    def test_epaonnistunut_korttiosto_paluuarvo_False_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortilla_ei_rahaa), False)

    def test_epaonnistunut_korttiosto_lounaiden_maara_ok_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortilla_ei_rahaa)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassan_saldo_ei_muutu_korttiosto_onnistunut_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortilla_rahaa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_saldo_ei_muutu_korttiosto_epaonnistunut_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortilla_ei_rahaa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_saldo_ei_muutu_korttiosto_onnistunut_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortilla_rahaa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_saldo_ei_muutu_korttiosto_epaonnistunut_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortilla_ei_rahaa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahaa_ladatessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortilla_ei_rahaa, 10)
        self.assertEqual(str(self.maksukortilla_ei_rahaa),"Kortilla on rahaa 0.20 euroa")

    def test_rahaa_ladatessa_kassan_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortilla_ei_rahaa, 100000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 200000)

    def test_rahaa_ladatessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortilla_ei_rahaa, 10)
        self.assertEqual(str(self.maksukortilla_ei_rahaa),"Kortilla on rahaa 0.20 euroa")

    def test_rahaa_ladatessa_negatiivinen_summa_paluuarvo_oikein(self):
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortilla_ei_rahaa, -100000), None)

    def test_rahaa_ladatessa_nolla_e_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortilla_ei_rahaa, 0)
        self.assertEqual(str(self.maksukortilla_ei_rahaa),"Kortilla on rahaa 0.10 euroa")

    def test_rahaa_ladatessa_nolla_e_kassan_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortilla_ei_rahaa, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)



#    def lataa_rahaa_kortille(self, kortti, summa):
#        if summa >= 0:
#            kortti.lataa_rahaa(summa)
#            self.kassassa_rahaa += summa
#        else:
#            return
