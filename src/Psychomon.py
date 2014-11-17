from Pokedex import Pokedex
from Pokestadium import Pokestadium
import PokeServer
import PokeClient

"Main function"
def main():
    print('  -- Welcome to Psychomon v0.1.2 --  \n')
    # Menu Principal
    while True:
        print('\nOptions:\n[1] Read pokémon\n[2] List pokémon\n[3] Battle!\n[4] Open Server\n[5] Open Client\n[6] Quit\n\n')
        try:
            opt = int(input('>: '))
        except ValueError:
            print('Invalid option\n')
            continue
        except EOFError:
            break

        if opt == 1:
            n = input('How many pokémon to read? ')
            try:
                n = int(n)
                assert(n >= 0)
            except ValueError:
                n = 1
            for i in range(n):
                print('\nEnter your pokémon:')
                Pokedex.read_pokemon()
        elif opt == 2:
            print("\nPokémon:")
            for poke in Pokedex.get_pokemons():
                print("  %s" % poke.name)
        elif opt == 3:
            Pokestadium.new_battle()
        elif opt == 4:
            PokeServer.start_server()
        elif opt == 5:
            PokeClient.start_client()
        elif opt == 6:
            break
        else:
            print('Invalid option\n')
    print(' -- Farewell --  ')


main()
