from Pokedata import *
from Pokemon import Pokemon

"List of pokemons."
_pokemons = {}

"Read single pokemon from stdin"
def read_pokemon():
    global _pokemons

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
        
        _pokemons[name.lower()] = Pokemon(name, level, att, attacks, *typ)

        return True
    except (EOFError, ValueError):
        return False
    

"Reads from stdin a list of Pokemons."
def read_all():
    while(read_pokemon()):
        pass

def get(pokename):
    global _pokemons
    poke = _pokemons.get(pokename.lower())
    return poke.copy() if poke else None

"Returns a pokemon list that can be iterated"
def get_pokemons():
    global _pokemons
    return _pokemons.values()

