from Pokedata import *
from Pokemon import Pokemon

class Pokedex:
    "List of Pokemons."
    pokemons = []    

    "Read single pokemon from stdin"
    @staticmethod
    def read_pokemon():
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
            
            Pokedex.pokemons.append(Pokemon(name, level, att, attacks, *typ))

            return True
        except (EOFError, ValueError):
            return False
        

    "Reads from stdin a list of Pokemons."
    @staticmethod
    def read_all():
        while(Pokedex.read_pokemon()):
            pass

    @staticmethod
    def get(pokename):
        # TODO: use table with names or something better.
        for i in Pokedex.pokemons:
            if i.name == pokename:
                return i
        return None

