import Pokedata

class Pokemon:
    STRUGGLE = -1

    "Pokemon class constructor."
    def __init__(self, name, lvl, atts, atks, type1, type2 = Pokedata.TYPE_BLANK):
        self.name = name
        self.lvl = lvl
        self.atts = atts
        self.current_atts = atts.copy() # Current attribute takes into account ATT altering attacks.
        self.atks = atks
        self.types = (type1, type2)
        # The default struggle attack is present in all pokemon.
        self.atks.append(Pokedata.Attack('Struggle', 0, 100, 50, float('inf')))
        # Tuples are faster and 'safer'
        self.atks = tuple(self.atks)

    def has_moves(self):
        for i in range(0, len(self.atks) - 1):
            if self.atks[i].current_pp > 0:
                return True
        return False
    
    "This pokemon attacks target opponent pokemon with given attack."
    def attack(self, opponent, atk_index):
        self.atks[atk_index].attack(self, opponent)

    "Returns a copy of this pokemon"
    def copy(self):
        return Pokemon(self.name, self.lvl, self.atts.copy(), list(self.atks[0 : -1]), self.types[0], self.types[1])
        
