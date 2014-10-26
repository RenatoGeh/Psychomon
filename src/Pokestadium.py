from Pokebattle import Pokebattle
from Pokedex import Pokedex

class Pokestadium:
    "The latest Pokemon winner."  
    winner = None

    "Manages the creation of a new pokebattle."
    @staticmethod
    def new_battle():
        poke1 = None
        while poke1 == None:
            poke1 = Pokedex.get(input('Nome do primeiro pokemon: '))
        poke2 = None
        while poke2 == None:
            poke2 = Pokedex.get(input('Nome do segundo pokemon: '))
        print('\n\n -- The Battle Begins -- ')
        battle = Pokebattle(poke1, poke2)
        Pokestadium.winner = battle.fight()
        return Pokestadium.winner
        
