from Pokedata import *
from Pokemon import Pokemon

class Pokedex:
    "Pokedex's constructor."
    def __init__(self):
        self.pokemons = ()
        
    "Searches for a type and returns its index from POKE_TYPES list."
    def _search_type(self, query):
        for i in range(0, len(POKE_TYPES)):
            if query == POKE_TYPES[i]:
                return i

        return TYPE_BLANK   # Else returns Blank.

    "Reads from stdin a list of Pokemons."
    def read(self):
        try:
            while(1):
                name = input()
                level = int(input())
                hp = int(input())
                atk = int(input())
                df = int(input())
                spd = int(input())
                spc = int(input())
                typ = (_search_type(input()), _search_type(input()))
                
                att = Attribute(hp, atk, df, spd, spc)

                n_attacks = int(input())
                attacks = ()

                while(n_attacks):
                    atk_name = input()
                    atk_typ = _search_type(input())
                    acu = int(input())
                    pwr = int(input())
                    pp = int(input())

                    attacks.append(Attack(atk_name, atk_typ, acu, pwr, pp))
                    n_attacks = n_attacks - 1
                
                self.pokemons.append(Pokemon(att, attacks, *typ))
        except EOFError:
            pass

    def get(self, pokename):
        for i in self.pokemons:
            if i.name == pokename:
                return i
        return None

