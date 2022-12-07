from unittest import TestCase
from data.saver_loader import load_from_list, save
import filter.filter as filter
from unittest.mock import patch

class TestFiltering(TestCase):
    def setUp(self):
        self.cube = load_from_list("temp","Testilista.txt")
        save(self.cube)
    
    def test_color_filter(self):
        cube = filter.color_filter(self.cube, "WR")
        self.assertEqual(cube.card_names,["Anafenza, Kin-Tree Spirit","Eight-and-a-Half-Tails","Carnival // Carnage","Angel of Despair"])
    
    def test_color_id_filter(self):
        cube = filter.color_id_filter(self.cube, "B,U")
        self.assertEqual(cube.card_names,["Blood Scrivener", "Dauthi Slayer", "Hydroblast", "Mizzium Skin", "Sol Ring", "Dimir Signet", "Lightning Greaves"])
    
    def test_cmc_filter_at_most(self):
        cube = filter.cmc_filter(self.cube, 1, 2)
        self.assertEqual(cube.card_names,["Blood Scrivener","Dauthi Slayer","Hydroblast", "Mizzium Skin","Anafenza, Kin-Tree Spirit","Eight-and-a-Half-Tails", "Sol Ring","Dimir Signet","Lightning Greaves"])
    
    def test_cmc_filter_at_least(self):
        cube = filter.cmc_filter(self.cube, 2, 3)
        self.assertEqual(cube.card_names,["Carnival // Carnage", "Angel of Despair"])
    
    def test_cmc_filter_exactly(self):
        cube = filter.cmc_filter(self.cube, 3, 1)
        self.assertEqual(cube.card_names,["Hydroblast", "Mizzium Skin", "Sol Ring"])
    
    def test_type_filter(self):
        cube = filter.type_filter(self.cube, "sorcery")
        self.assertEqual(cube.card_names,["Carnival // Carnage"])
    
    def test_oracle_filter(self):
        cube = filter.oracle_filter(self.cube, "control")
        self.assertEqual(cube.card_names,["Mizzium Skin","Anafenza, Kin-Tree Spirit","Eight-and-a-Half-Tails","Carnival // Carnage"])
    
    def test_power_filter_at_most(self):
        cube = filter.power_filter(self.cube, 1, 2)
        self.assertEqual(cube.card_names,["Blood Scrivener","Dauthi Slayer", "Anafenza, Kin-Tree Spirit","Eight-and-a-Half-Tails"])

    def test_power_filter_at_least(self):
        cube = filter.power_filter(self.cube, 2, 3)
        self.assertEqual(cube.card_names,["Angel of Despair"])

    def test_power_filter_exactly(self):
        cube = filter.power_filter(self.cube, 3, 5)
        self.assertEqual(cube.card_names,["Angel of Despair"])

    def test_toughness_filter_at_most(self):
        cube = filter.toughness_filter(self.cube, 1, 1)
        self.assertEqual(cube.card_names,["Blood Scrivener"])
    
    def test_toughness_filter_at_least(self):
        cube = filter.toughness_filter(self.cube, 2, 2)
        self.assertEqual(cube.card_names,["Dauthi Slayer", "Anafenza, Kin-Tree Spirit","Eight-and-a-Half-Tails","Angel of Despair"])
    
    def test_toughness_filter_exactly(self):
        cube = filter.toughness_filter(self.cube, 3, 1)
        self.assertEqual(cube.card_names,["Blood Scrivener"])
    