from Pokedata import *
from Pokemon import Pokemon

class Pokedex:
    "Pokedex's constructor."
    def __init__(self):
        self.pokemons = []

    "Read single pokemon from stdin"
    def read_pokemon(self):
        try:
            name = input()
            level = int(input())
            hp = int(input())
            atk = int(input())
            df = int(input())
            spd = int(input())
            spc = int(input())
            typ = (int(input()), int(input()))
            
            att = Attribute(hp, atk, df, spd, spc)

            n_attacks = int(input())
            attacks = []

            for i in range(n_attacks):
                atk_name = input()
                atk_typ = int(input())
                acu = int(input())
                pwr = int(input())
                pp = int(input())

                attacks.append(Attack(atk_name, atk_typ, acu, pwr, pp))
            
            self.pokemons.append(Pokemon(name, level, att, attacks, *typ))

            return True
        except (EOFError, ValueError):
            return False
        

    "Reads from stdin a list of Pokemons."
    def read_all(self):
        while(self.read_pokemon()):
            pass

    def get(self, pokename):
        # TODO: use table with names or something better.
        for i in self.pokemons:
            if i.name == pokename:
                return i
        return None

