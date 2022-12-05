import unittest
from data.saver_loader import load_from_list

class TestFitlering(unittest.TestCase):
    def setUp(self):
        self.cube = load_from_list("TestCube","Testilista.txt")
    
    def test_color_filter(self):
        filter.color_filter(self.cube.name)