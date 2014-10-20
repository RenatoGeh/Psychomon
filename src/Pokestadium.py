import Pokemon
import from Pokebattle Pokebattle
import Pokedex

class Pokestadium:
    
    "Manages the creation of a new pokebattle."
    def new_battle(self):
        pok1 = Pokedex.Get_pokemon(input('enter the name of the first pokemon:'))
        pok2 = Pokedex.Get_pokemon(input('enter the name of the second pokemon:'))
        Pokebattle = Pokebattle(self.pok1,self.pok2)
        winner = Pokebattle.fight()
        
        
		
