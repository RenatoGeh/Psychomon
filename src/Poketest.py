from Test_Pokebattle import TestPokebattle
from Test_Pokedata import TestPokedata
from Test_Pokedex import TestPokedex
from Test_Pokemon import TestPokemon

"Funcao que executa todos os testes do exercicio programa"
def main():
    print('\nPokebattle Failures: %d\nPokedata Failures: %d\nPokedex Failures: %d\nPokemon Failures: %d' % 
    	(len(TestPokebattle().run().failures), len(TestPokedata().run().failures), len(TestPokedex().run().failures),
    		len(TestPokemon().run().failures)))
    
main()
