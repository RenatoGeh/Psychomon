import random

POKE_TYPES = ('Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bird', 'Bug', 'Ghost', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Blank')
POKE_TYPES_INDEX = { poke_type: index for index, poke_type in enumerate(POKE_TYPES) }

TYPE_EFF_CHART = (
# NO  FI  FL  PO  GR  RO  BI  BU  GH  FR  WA  GS  EL  PS  IC  DR  BL
( 1,  1,  1,  1,  1, .5,  1,  1,  0,  1,  1,  1,  1,  1,  1,  1,  1), # NOrmal
( 2,  1, .5, .5,  1,  2, .5,  1,  0,  1,  1,  1,  1, .5,  2,  1,  1), # FIght
( 1,  2,  1,  1,  1, .5,  1,  1,  1,  1,  1,  2, .5,  1,  1,  1,  1), # FLying
( 1,  1,  1, .5, .5, .5,  1,  1, .5,  1,  1,  2,  1,  1,  1,  1,  1), # POison
( 1,  1,  0,  2,  1,  2,  0,  1,  1,  2,  1, .5,  2,  1,  1,  1,  1), # GRound
( 1, .5,  2,  1, .5,  1,  2,  1,  1,  2,  1,  1,  1,  1,  2,  1,  1), # ROck
( 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1), # BIrd
( 1, .5, .5,  2,  1,  1, .5,  1, .5, .5,  1,  2,  1,  2,  1,  1,  1), # BUg
( 0,  1,  1,  1,  1,  1,  1,  1,  2,  1,  1,  1,  1,  0,  1,  1,  1), # GHost
( 1,  1,  1,  1,  1, .5,  1,  1,  1, .5, .5,  2,  1,  1,  2, .5,  1), # FiRe
( 1,  1,  1,  1,  2,  2,  1,  1,  1,  2, .5, .5,  1,  1,  1, .5,  1), # WAter
( 1,  1, .5, .5,  2,  2, .5,  1,  1, .5,  2, .5,  1,  1,  1, .5,  1), # GraSs
( 1,  1,  2,  1,  0,  1,  2,  1,  1,  1,  2, .5, .5,  1,  1, .5,  1), # ELetric
( 1,  2,  1,  2,  1,  1,  1,  1,  1,  1,  1,  1,  1, .5,  1,  1,  1), # PSych
( 1,  1,  2,  1,  2,  1,  2,  1,  1,  1, .5,  2,  1,  1, .5,  2,  1), # ICe
( 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1), # DRagon
( 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1)  # BLank
)

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
    def copy(self):
        return Attribute(self.hp, self.atk, self.df, self.spd, self.spc)

class Attack:
    "Attack class constructor."
    def __init__(self, name, typ, acu, pwr, pp):
        self.name = name
        self.typ = typ
        self.acu = acu
        self.pwr = pwr
        self.base_pp = self.current_pp = pp

    USES_SPC = {'Water', 'Grass', 'Fire', 'Ice', 'Electric', 'Psychic', 'Dragon', 'Dark'}

    """Returns base damage of attack on target opponent
    Ignores criticals and the random modifier.
    """
    def _get_base_damage(self, me, opp, verboose=True):
        damage = (2 * me.lvl + 10) / 250
        if POKE_TYPES[self.typ] in Attack.USES_SPC:
            damage *= me.current_atts.spc / opp.current_atts.spc
        else:
            damage *= me.current_atts.atk / opp.current_atts.df
        damage = damage * self.pwr + 2

        stab = 1.5 if (self.typ == me.types[0]) or (self.typ == me.types[1]) else 1
        typ_eff = TYPE_EFF_CHART[self.typ][opp.types[0]] * TYPE_EFF_CHART[self.typ][opp.types[1]]

        if verboose:
            if typ_eff > 1:
                print('It\'s super effective!')
            elif typ_eff == 0:
                print('It\'s not effective...')
            elif typ_eff < 1:
                print('It\'s not very effective...')

        mod = stab * typ_eff
        return damage * mod

    "Returns average damage of attack."
    def get_average_damage(self, me, opp):
        base_dam = self._get_base_damage(me, opp, verboose=False)
        chance_to_hit = self.acu / 100
        chance_to_crit = me.current_atts.spd / 512
        return chance_to_hit * (1 + chance_to_crit) * base_dam

    "Attacks target opponent."
    def attack(self, me, opp):
        print('\n%s uses %s.' % (me.name, self.name))
        self.current_pp = self.current_pp - 1

        chance_to_hit = self.acu / 100 # Accuracy and Evasion are always 100
        if random.random() >= chance_to_hit:
            print('\n%s missed!' % me.name)
            return

        damage = self._get_base_damage(me, opp)

        crit = 2 if random.random() < me.current_atts.spd / 512 else 1
        if crit > 1:
            print('Critical Hit!')
        
        damage = int(damage * crit * random.uniform(.85, 1))

        print('%s deals %d damage to %s.' % (self.name, damage, opp.name))
        opp.current_atts.hp -= damage
