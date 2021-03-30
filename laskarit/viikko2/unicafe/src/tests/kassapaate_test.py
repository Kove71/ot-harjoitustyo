import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaatteen_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_myytyjen_maara_oikea(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_edullisten_osto_kateinen_riittavasti_kateista(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(palautus, 60)

    def test_edullisten_osto_kateinen_ei_riittavasti_kateista(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(palautus, 200)

    def test_maukkaiden_osto_kateinen_riittavasti_kateista(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(palautus, 100)

    def test_maukkaiden_osto_kateinen_ei_riittavasti_kateista(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(palautus, 200)
    
    def test_edullisten_osto_kortti_riittavasti(self):
        kortti = Maksukortti(300)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(onnistui, True)
        self.assertEqual(kortti.saldo, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisten_osto_kortti_ei_riittavasti(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(onnistui, False)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaiden_osto_kortti_riittavasti(self):
        kortti = Maksukortti(500)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(onnistui, True)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaiden_osto_kortti_ei_riittavasti(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(onnistui, False)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille_positiivinen_summa(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(kortti.saldo, 200)

    def test_lataa_rahaa_kortille_negatiivinen_summa(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 100)