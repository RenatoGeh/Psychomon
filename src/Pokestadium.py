from Pokebattle import Pokebattle
from Pokedex import Pokedex

class Pokestadium:
    "The latest Pokemon winner."  
    winner = None

    @staticmethod
    def choose_pokemon(text = 'Nome do pokemon: '):
        poke = None
        while poke == None:
            poke = Pokedex.get(input(text))
        return poke

    "Manages the creation of a new pokebattle."
    @staticmethod
    def new_battle():
        poke1 = Pokestadium.choose_pokemon('Nome do primeiro pokemon: ')
        poke2 = Pokestadium.choose_pokemon('Nome do segundo pokemon: ')
        print('\n\n -- The Battle Begins -- ')
        battle = Pokebattle(poke1, poke2)
        Pokestadium.winner = battle.fight()
        return Pokestadium.winner
        
