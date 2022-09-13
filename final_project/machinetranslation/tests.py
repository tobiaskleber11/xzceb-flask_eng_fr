import unittest
from translator import french_to_english
from translator import english_to_french
class TestMyModule(unittest.TestCase):
    def test_f2e1(self):
        self.assertEqual(french_to_english("Bonjour"),"hello")
    def test_f2e_bonjou2(self):
        self.assertNotEqual(french_to_english("None")," ")


class TestMyModule(unittest.TestCase):
    def test_e2f1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_e2f_bonjour2(self):
        self.assertNotEqual(english_to_french("None"), " ")
unittest.main()