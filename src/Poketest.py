from tests import Test_Pokebattle
from tests import Test_Pokedata
from tests import Test_Pokedex
from tests import Test_Pokemon
from tests import Test_XMLManager
from tests import Test_Pokenetwork

import unittest

def runTest(class_name):
    print('*********** Running %s Tests ***********' % class_name)
    suite = unittest.TestSuite()
    cl = eval('Test_' + class_name + '.Test' + class_name)
    for method in dir(cl):
       if method.startswith("test"):
          suite.addTest(cl(method))
    unittest.TextTestRunner().run(suite)
    print('************************************************\n')

"Runs all the tests available"
def main():
    for test in ('Pokebattle', 'Pokedata', 'Pokedex', 'Pokemon', 'XMLManager', 'Pokenetwork'):
        runTest(test)
    
main()
