from Pokebattle import Pokebattle

class Pokestadium:
    
    "Manages the creation of a new pokebattle."
    def new_battle(self, pokedex):
        poke1 = None
        while poke1 == None:
            poke1 = pokedex.get(input('Nome do primeiro pokemon: '))
        poke2 = None
        while poke2 == None:
            poke2 = pokedex.get(input('Nome do segundo pokemon: '))
        print('\n\n -- The Battle Begins -- ')
        battle = Pokebattle(poke1, poke2)
        return battle.fight()        
        
