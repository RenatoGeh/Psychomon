from Pokebattle import Pokebattle
from Pokedex import Pokedex

class Pokestadium:
    
    "Manages the creation of a new pokebattle."
    def new_battle(self):
        Pokebattle = Pokebattle(Pokedex.get(input('Enter the name of the first pokemon: ')), Pokedex.get(input('Enter the name of the second pokemon: ')))
        winner = Pokebattle.fight()        
        
