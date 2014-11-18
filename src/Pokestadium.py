from Pokebattle import Pokebattle
import Pokedex

"The latest Pokemon winner."  
winner = None

def choose_pokemon(text = 'Pokémon name: '):
    poke = None
    while poke == None:
        poke = Pokedex.get(input(text))
    return poke

"Manages the creation of a new pokebattle."
def new_battle():
    global winner

    poke1 = choose_pokemon('First pokémon name: ')
    poke2 = choose_pokemon('Second pokémon name:: ')
    print('\n\n -- The Battle Begins -- ')
    battle = Pokebattle(poke1, poke2)
    winner = battle.fight()

    return winner
    
