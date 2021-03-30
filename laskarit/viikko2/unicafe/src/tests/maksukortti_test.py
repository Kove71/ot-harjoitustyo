import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alustettu_raha_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_arvon_lataus(self):
        self.maksukortti.lataa_rahaa(90)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
    
    def test_saldo_vähenee(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
    
    def test_saldo_ei_muutu_jos_nostaa_liikaa(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_ota_rahaa_palauttaa_true_jos_onnistui(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)


    def test_ota_rahaa_palauttaa_false_jos_ei_onnistu(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20), False)