import Pokemon

class Pokebattle:
	"Pokebattle class constructor."
	def __init__(self, pok1, pok2):
		"Makes pokemon1 the faster pokemon." 
		if pok1.spd >= pok2.spd:
		    self.pokemon1 = pok1
		    self.pokemon2 = pok2
		else:
		    self.pokemon1 = pok2
		    self.pokemon2 = pok1
	
	"Starts the battle between two pokemons."	
    def fight(self):
        'Begins the fight starting with the faster pokemon (pokemon1).'
        while(not self.pokemon1.hp or not self.pokemon2.hp)
	        s = repr(pokemon1) + ', it\'s your turn!\nAvailable attacks:'  
	        print(s)
	        for i in range (0, length(pokemon1.atks[]):
                s = repr(i) + '. ' + pokemon.atks[i].name      	            
	            print(s)
	        
	        x = raw_input    
	    if self.pokemon1.hp:
	        winner = pokemon1
	    else:
	        winner = pokemon2
	        		
		return winner
