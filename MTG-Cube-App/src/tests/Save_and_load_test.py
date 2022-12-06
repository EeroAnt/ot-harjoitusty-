import unittest
from data.saver_loader import save, load, load_from_list
import os
from unittest.mock import patch
from io import StringIO

class TestSavingAndLoading(unittest.TestCase):
    def setUp(self):
        self.cube = load_from_list("TestCube","Testilista.txt")
        save(self.cube)

    def test_loading_from_list(self):
        self.assertEqual(self.cube.card_names, ['Blood Scrivener', 'Dauthi Slayer', 'Hydroblast', 'Mizzium Skin', 'Anafenza, Kin-Tree Spirit', 'Eight-and-a-Half-Tails', 'Carnival // Carnage', 'Sol Ring', 'Dimir Signet', 'Lightning Greaves'])

    @patch('sys.stdout', new_callable= StringIO)
    def test_loading_from_list_print(self, stdout):
        load_from_list("TestCube","Testilista.txt")
        self.assertEqual(stdout.getvalue(),"Kortit, joiden lisääminen ei onnistunut:\n\nEi validi kortti\n" )

    def test_saving_cube(self):
        self.assertEqual(os.path.exists("src/data/Saved_Cubes/TestCube.db"), True)

    def test_loading_from_db(self):
        load_test_cube = load("TestCube")
        self.assertEqual(load_test_cube.card_names, ['Blood Scrivener', 'Dauthi Slayer', 'Hydroblast', 'Mizzium Skin', 'Anafenza, Kin-Tree Spirit', 'Eight-and-a-Half-Tails', 'Carnival // Carnage', 'Sol Ring', 'Dimir Signet', 'Lightning Greaves'])