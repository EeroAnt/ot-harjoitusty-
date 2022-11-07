import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 11.00 euroa")

    def test_ottaessa_saldo_vahenee_oikein_jos_on_riittavasti(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 9.00 euroa")

    def test_ottaessa_saldo_ei_muutu_jos_ei_ole_riittavasti(self):
        self.maksukortti.ota_rahaa(100000)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 10.00 euroa")

    def test_metodi_palauttaa_True_jos_rahat_riittivat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100),True)

    def test_metodi_palauttaa_False_jos_rahat_eivat_riittaneet(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100000),False)

