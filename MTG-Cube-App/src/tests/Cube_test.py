import unittest
from entities.cube import Cube

class TestCube(unittest.TestCase):
    def setUp(self) -> None:
        self.cube = Cube("TestCube")

    def test_cube_named_right(self):
        self.assertEqual(str(self.cube), "TestCube")

    def test_empty_cube_is_empty(self):
        self.assertEqual(
            [self.cube.collection, self.cube.card_names], [[], []])

    def test_adding_cards_works(self):
        self.cube.add_card("forest")
        self.assertEqual([self.cube.card_names, len(
            self.cube.collection)], [["Forest"], 1])

    def test_adding_duplicate_cards_doesnt_work(self):
        self.cube.add_card("forest")
        self.cube.add_card("forest")
        self.assertEqual([self.cube.card_names, len(
            self.cube.collection)], [["Forest"], 1])
