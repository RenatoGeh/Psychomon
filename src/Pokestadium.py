import Pokemon
import Pokebattle

class Pokestadium:
    
    "Manages the creation of a new pokebattle."
    def new_battle(self):
        pok1 = raw_input('enter the name of the first pokemon:')
        pok2 = raw_input('enter the name of the second pokemon:')
        
        Pokebattle = Pokebattle(self.pok1,self.pok2)
        winner = Pokebattle.fight()
        
        
        
