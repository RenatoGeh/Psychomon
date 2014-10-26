import random

POKE_TYPES = ('Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bird', 'Bug', 'Ghost', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Blank')
POKE_TYPES_INDEX = { poke_type: index for index, poke_type in enumerate(POKE_TYPES) }

TYPE_BLANK = len(POKE_TYPES) - 1

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
        self.ppi = self.ppc = pp # pp inicial e pp atual 

    USES_SPC = {'Water', 'Grass', 'Fire', 'Ice', 'Electric', 'Psychic', 'Dragon', 'Dark'}

    "Attacks target opponent."
    def attack(self, me, opp):
        self.ppc = self.ppc - 1

        chance_to_hit = self.acu / 100 # Accuracy and Evasion are always 100
        if random.random() > chance_to_hit:
            print('\n%s missed!' % me.name)
            return

        damage = (2 * me.lvl + 10) / 250
        if POKE_TYPES[self.typ] in Attack.USES_SPC:
            damage *= me.current_atts.spc / opp.current_atts.spc
        else:
            damage *= me.current_atts.atk / opp.current_atts.df
        damage = damage * self.pwr + 2

        stab = 1.5 if (self.typ == me.types[0]) or (self.typ == me.types[1]) else 1
        # TODO: Use this chart (http://bulbapedia.bulbagarden.net/wiki/Type/Type_chart#Generation_I) to calculate
        typ_eff = 1 
        # TODO: Different crit for some moves, maybe
        crit = 2 if random.random() < me.current_atts.spd / 512 else 1

        mod = stab * typ_eff * crit * random.uniform(.85, 1)
        damage = int(damage * mod)

        print('\n%s uses %s and deals %d damage to %s.' % (me.name, self.name, damage, opp.name))
        opp.current_atts.hp -= damage
