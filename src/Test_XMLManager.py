import unittest
from Pokedex import Pokedex
from Pokemon import Pokemon
from Pokedata import *
import XMLManager
import io
import lxml.etree as ET

class TestXMLManager(unittest.TestCase):
    def runTest(self):
        super.runTest()

    def test_get_xml(self):
        p = Pokemon('PoKeMoN', 1, Attribute(2, 3, 4, 5, 6), [Attack('atk', 7, 8, 9, 10)], 11, 12)
        self.assertTrue(XMLManager.check_xml(XMLManager.get_basic_xml(p)), 'Generating wrong XML.')

    def test_wrong_xml(self):
        xml = ET.parse(io.StringIO('<battle_state><wrong></wrong></battle_state>'))
        self.assertFalse(XMLManager.check_xml(xml), 'Not detecting wrong xml.')

if __name__ == '__main__':
    unittest.main()
