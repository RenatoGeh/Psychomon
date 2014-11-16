from Pokedex import Pokedex
from Pokestadium import Pokestadium
import PokeServer
import PokeClient

"Funcao central do exercicio programa"
def main():
    print('  -- Bem vindo ao Psychomon v0.1.2 --  \n')
    # Menu Principal
    while True:
        print('\nOpcoes:\n[1] Ler pokemon\n[2] Listar Pokemons\n[3] Batalhar\n[4] Abrir Servidor\n[5] Abrir Cliente\n[6] Sair\n\n')
        try:
            opt = int(input('>: '))
        except ValueError:
            print('Opcao invalida\n')
            continue
        except EOFError:
            break

        if opt == 1:
            n = input('Quantos pokemos deseja ler? ')
            try:
                n = int(n)
                assert(n >= 0)
            except ValueError:
                n = 1
            for i in range(n):
                print('\nDigite o seu pokemon:')
                Pokedex.read_pokemon()
        elif opt == 2:
            print("\nPokemons:")
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
            print('Opcao invalida\n')
    print(' -- Adeus --  ')


main()
