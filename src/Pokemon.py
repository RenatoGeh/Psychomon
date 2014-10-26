import Pokedata
import copy

class Pokemon:
    STRUGGLE = -1

    "Pokemon class constructor."
    def __init__(self, name, lvl, atts, atks, type1, type2 = Pokedata.TYPE_BLANK):
        self.name = name
        self.lvl = lvl
        self.atts = atts
        self.current_atts = copy.copy(atts) # Current attribute takes into account ATT altering attacks.
        self.atks = atks
        self.types = (type1, type2)
        # The default struggle attack is present in all pokemon.
        self.atks.append(Pokedata.Attack('Struggle', 0, 100, 50, float('inf')))
        # Tuples are faster and 'safer'
        self.atks = tuple(self.atks)
    
    "This pokemon attacks target opponent pokemon with given attack."
    def attack(self, opponent, atk_index):
        self.atks[atk_index].attack(self, opponent)
        
