import unittest
import io
import sys

from Pokedex import Pokedex
from Pokemon import Pokemon
from Pokedata import *

class TestPokedex(unittest.TestCase):
    def setUp(self):
        self.primitives = (int, float, str)

    def tearDown(self):
        sys.stdin = sys.__stdin__
        
    def test_read_exception(self):
        p1 = Pokemon('p1', 1, Attribute(2, 3, 4, 5, 6), [Attack('atk', 7, 8, 9, 10)], 11, 12)
        
        sys.stdin = io.StringIO('p1\nd\nwhat\n3.4\nthe\n5.5\nhell\n11\n12\n1\natk\n7\n8\n9\n10')        

        self.assertFalse(Pokedex.read_pokemon(), "Pokedex exception not being caught.")


    def test_read(self):
        p1 = Pokemon('p1', 1, Attribute(2, 3, 4, 5, 6), [Attack('atk', 7, 8, 9, 10)], 11, 12)
        
        sys.stdin = io.StringIO('p1\n1\n2\n3\n4\n5\n6\n11\n12\n1\natk\n7\n8\n9\n10')
      
        Pokedex.read_pokemon()

        p2 = Pokedex.get(p1.name.lower())

        for member in vars(p1):
            val = eval('p1.' + member)
            if(type(val) in self.primitives):
                self.assertEqual(val, eval('p2.' + member))

    def test_get(self):
        p1 = Pokemon('PoKeMoN', 1, Attribute(2, 3, 4, 5, 6), [Attack('atk', 7, 8, 9, 10)], 11, 12)

        sys.stdin = io.StringIO('PoKeMoN\n1\n2\n3\n4\n5\n6\n11\n12\n1\natk\n7\n8\n9\n10')

        Pokedex.read_pokemon()

        self.assertEqual(p1.name, Pokedex.get(p1.name).name)

    def test_get_wrong(self):
        try:
            Pokedex.get("blah")
        except:
            self.fail('Shouldn\'t throw exception')


if __name__ == '__main__':
    unittest.main()
