import unittest
from Pokedex import Pokedex
from Pokemon import Pokemon
from Pokedata import *
import XMLManager
import io
import lxml.etree as ET

class TestXMLManager(unittest.TestCase):
    def test_get_xml(self):
        p = Pokemon('PoKeMoN', 1, Attribute(2, 3, 4, 5, 6), [Attack('atk', 7, 8, 9, 10)], 11, 12)
        self.assertTrue(XMLManager.check_xml(XMLManager.get_xml(p)), 'Generating invalid XML.')

    def test_two_pokemons(self):
        p1 = Pokemon('PoKeMoN1', 1, Attribute(2, 3, 4, 5, 6), [Attack('atk', 7, 8, 9, 10)], 11, 12)
        p2 = Pokemon('PoKeMoN2', 2, Attribute(3, 4, 5, 6, 7), [Attack('atk', 8, 9, 10, 11)], 12, 13)
        x = XMLManager.get_xml(p1, p2)
        self.assertEqual(len(x), 2, 'XML doesn\'t have 2 pokemons')

    def test_content(self):
        p = Pokemon('PoKeMoN', 1, Attribute(2, 3, 4, 5, 6), [Attack('atk', 7, 9, 8, 10)], 11, 12)
        pok = XMLManager.get_xml(p)[0]
        try:
            assert(pok[0].text == 'PoKeMoN')
            assert(pok[1].text == '1')
            for i in range(2, 6):
                assert(pok[2][i - 2].text == str(i))
            assert(pok[3].text == '11')
            assert(pok[4].text == '12')
            assert(pok[5][0].text == '1')
            assert(pok[5][1].text == 'atk')
            for i in range(7, 10):
                assert(pok[5][i - 5].text == str(i))
        except AssertionError:
            self.fail('Created XML has wrong data.')



    def test_wrong_xml(self):
        xml = ET.parse(io.StringIO('<battle_state><wrong></wrong></battle_state>'))
        self.assertFalse(XMLManager.check_xml(xml), 'Not detecting wrong xml.')

if __name__ == '__main__':
    unittest.main()
