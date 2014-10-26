from Pokedex import Pokedex
from Pokestadium import Pokestadium

"Funcao central do exercicio programa"
def main():
    print('  -- Bem vindo ao Psychomon v0.1.2 --  \n')
    # Menu Principal
    while True:
        print('\nOpcoes:\n[1] Ler pokemon\n[2] Batalhar\n[3] Sair\n\n')
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
            Pokestadium.new_battle()
        elif opt == 3:
            break
        else:
            print('Opcao invalida\n')
    print(' -- Adeus --  ')    


main()
