import unittest
from Pokemon import Pokemon
from Pokedata import *

class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.p1 = Pokemon('p1', 1, Attribute(2, 3, 4, 5, 6), [Attack("atk", 7, 8, 9, 10)], 11)
        self.primitive = (int, float, str, tuple, dict, list)

    def test_blank(self):
        self.assertEqual(TYPE_BLANK, self.p1.types[1], 'Second type failed to be attributed as Blank.')

    def test_copy(self):
        cpy = self.p1.copy()

        for member in vars(cpy):
            if member in self.primitive:
                self.assertEqual(eval('cpy.' + member), eval('self.p1.' + member))
            else:
                self.assertIsInstance(eval('cpy.' + member), eval('self.p1.' + member).__class__)

    def test_struggle(self):
        self.assertEqual(self.p1.atks[Pokemon.STRUGGLE].name, 'Struggle', 'Struggle not present.')


if __name__ == '__main__':
    unittest.main()
