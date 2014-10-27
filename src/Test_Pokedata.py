import unittest
from Pokedata import *

class TestPokedata(unittest.TestCase):
    def setUp(self):
        self.att_1 = Attribute(10, 11, 12, 13, 14)
        self.att_2 = Attribute(20, 21, 22, 23, 24)

        self.atk_1 = Attack('atk_1', 1, 2, 3, 4)
        self.atk_2 = Attack('atk_2', 5, 6, 7, 8)

    def test_copy_attribute(self):
        cpy_1 = self.att_1.copy()
        cpy_2 = self.att_2.copy()
        
        for member in vars(cpy_1):
            self.assertEqual(eval('cpy_1.' + member), eval('self.att_1.' + member), '1-Attribute: Copying ' + member + ' failed.')
            
        for member in vars(cpy_2):
            self.assertEqual(eval('cpy_2.' + member), eval('self.att_2.' + member), '2-Attribute: Copying ' + member + ' failed.')

    def test_types(self):
        for typ in POKE_TYPES_INDEX:
            self.assertEqual(typ, POKE_TYPES[POKE_TYPES_INDEX[typ]], 'Type ' + typ + ' has conflicting pair.')

if __name__ == '__main__':
    unittest.main()
