POKE_TYPES = ("Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bird", "Bug", "Ghost", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Blank")

TYPE_BLANK = len(POKE_TYPES)-1

class Attribute:
    "Attribute class constructor."
    def __init__(self, hp, atk, df, spd, spc):
        self.hp = hp
        self.atk = atk
        self.df = df        # def is already a keyword.
        self.spd = spd
        self.spc = spc
    
    "Creates a cloned instance of same object."
    def __copy__(self):
        return Attribute(self.hp, self.atk, self.df, self.spd, self.spc)

class Attack:
    "Attack class constructor."
    def __init__(self, name, typ, acu, pwr, pp):
        self.name = name
        self.typ = typ
        self.acu = acu
        self.pwr = pwr
        self.base_pp = self.curr_pp = pp
    
    "Produces the attack on target opponent."
    def attack(self, me, opponent):
        # Do attack stuff.
        pass
        
