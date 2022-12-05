import unittest
from data.saver_loader import save, load, load_from_list
import os

class TestSavingAndLoading(unittest.TestCase):
    def setUp(self):
        self.cube = load_from_list("TestCube","Testilista.txt")
        save(self.cube)

    def test_loading_from_list(self):
        self.assertEqual(self.cube.card_names, ['Blood Scrivener', 'Bloodthrone Vampire', 'Burglar Rat', 'Caligo Skin-Witch', 'Dauthi Horror', 'Dauthi Slayer', 'Dregscape Zombie', 'Dusk Legion Zealot', 'Gnawing Zombie', 'Golgari Thug', 'Pack Rat', 'Hydroblast', 'Mizzium Skin', 'Opt', 'Ponder', 'Preordain', 'Serum Visions', 'Sleight of Hand', 'String of Disappearances', 'Stubborn Denial', 'Swan Song', 'Anafenza, Kin-Tree Spirit', 'Eight-and-a-Half-Tails'])
    
    def test_saving_cube(self):
        self.assertEqual(os.path.exists("src/data/Saved_Cubes/TestCube.db"), True)

    def test_loading_from_db(self):
        load_test_cube = load("TestCube")
        self.assertEqual(load_test_cube.card_names, ['Blood Scrivener', 'Bloodthrone Vampire', 'Burglar Rat', 'Caligo Skin-Witch', 'Dauthi Horror', 'Dauthi Slayer', 'Dregscape Zombie', 'Dusk Legion Zealot', 'Gnawing Zombie', 'Golgari Thug', 'Pack Rat', 'Hydroblast', 'Mizzium Skin', 'Opt', 'Ponder', 'Preordain', 'Serum Visions', 'Sleight of Hand', 'String of Disappearances', 'Stubborn Denial', 'Swan Song', 'Anafenza, Kin-Tree Spirit', 'Eight-and-a-Half-Tails'])
