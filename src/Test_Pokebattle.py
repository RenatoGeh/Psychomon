import unittest
from Pokebattle import Pokebattle
from Pokedex import Pokedex
from Pokemon import Pokemon
from Pokedata import *

class TestPokebattle(unittest.TestCase):
    def setUp(self):
        self.p1 = Pokemon("test_1", 1, Attribute(100, 10, 5, 5, 10), [Attack("atk_1", 4, 5, 2, 10)], 2, 1)
        self.p2 = Pokemon("test_2", 2, Attribute(50, 2, 1, 1, 5), [Attack("atk_2", 2, 10, 1, 5)], 5, 7)
        self.battle = Pokebattle(self.p1, self.p2)

    def test_assignment(self):
        self.assertIs(self.p1 if self.p1.current_atts.spd > self.p2.current_atts.spd else self.p2, self.battle.pokemon1, 
            "Speed test failed")
        
    def test_winner_1(self):
        self.p1.current_atts.hp = 0
        self.assertIs(self.p2, self.battle.fight(), "Winner assignment failed. Supposed to be P2.")

    def test_winner_2(self):
        self.p2.current_atts.hp = 0
        self.assertIs(self.p1, self.battle.fight(), "Winner assignment failed. Supposed to be P1.")

if __name__ == '__main__':
    unittest.main()
