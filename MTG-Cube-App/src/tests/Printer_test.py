from unittest import TestCase
from printer.printer import print_list_table, print_list_imgs
from data.saver_loader import load_from_list
import os
from unittest.mock import patch

class TestPrinting(TestCase):
    def setUp(self):
        self.cube = load_from_list("TestCube","Testilista.txt")

    def test_printing_to_table(self):
        print_list_table(self.cube, "Testing")
        self.assertEqual(os.path.exists("src/printer/Printed_lists/Testing.html"), True)

    def test_printing_to_img(self):
        print_list_imgs(self.cube, "Testing")
        self.assertEqual(os.path.exists("src/printer/Printed_lists/Testing.html"), True)
