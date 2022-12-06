from unittest import TestCase
from data.saver_loader import load_from_list
import filter.filter as filter
from unittest.mock import patch

class TestFiltering(TestCase):
    def setUp(self):
        self.cube = load_from_list("TestCube","Testilista.txt")
    # Tää meni läpi. Sit tein ton toisen. Se ei menny läpi. Sit ensimmäisen vaihdoin return_valuen B:ksi.
    # Sit ei toiminu kumpikaan. Sit vaihdoin sen takas. Kumpikaan ei toimi enää.
    # Kumpikin ominaisuus toimii, jos ajaa itse ohjelman
    @patch('filter.filter.get_input',return_value="W")    
    def test_color_filter(self, input):
        cube = filter.color_filter(self.cube)
        self.assertEqual(cube.card_names,["Anafenza, Kin-Tree Spirit","Eight-and-a-Half-Tails"])

    # @patch('filter.filter.get_input',return_value="W")    
    # def test_color_id_filter(self, input):
    #     cube = filter.color_id_filter(self.cube)
    #     self.assertEqual(cube.card_names,["Anafenza, Kin-Tree Spirit","Eight-and-a-Half-Tails","Sol Ring","Lightning Greaves"])
