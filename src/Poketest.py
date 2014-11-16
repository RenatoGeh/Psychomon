from Test_Pokebattle import TestPokebattle
from Test_Pokedata import TestPokedata
from Test_Pokedex import TestPokedex
from Test_Pokemon import TestPokemon
from Test_XMLManager import TestXMLManager
import unittest

def runTest(class_name):
    print('*********** Running %s Tests ***********' % class_name)
    suite = unittest.TestSuite()
    cl = eval('Test%s' % class_name)
    for method in dir(cl):
       if method.startswith("test"):
          suite.addTest(cl(method))
    unittest.TextTestRunner().run(suite)
    print('************************************************\n')

"Funcao que executa todos os testes do exercicio programa"
def main():
    for test in ('Pokebattle', 'Pokedata', 'Pokedex', 'Pokemon', 'XMLManager'):
        runTest(test)
    
main()
