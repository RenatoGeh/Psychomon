from Test_Pokebattle import TestPokebattle
from Test_Pokedata import TestPokedata
from Test_Pokedex import TestPokedex
from Test_Pokemon import TestPokemon
from Test_XMLManager import TestXMLManager

def runTest(class_name):
	print('%s Failures: %d' % (class_name, len(eval('Test%s()' % class_name).run().failures)))

"Funcao que executa todos os testes do exercicio programa"
def main():
	for test in ('Pokebattle', 'Pokedata', 'Pokedex', 'Pokemon', 'XMLManager'):
		runTest(test)
    
main()
