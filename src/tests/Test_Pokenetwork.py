import unittest
import requests

from threading import Timer

import PokeClient
import PokeServer

class TestPokenetwork(unittest.TestCase):
    def setUp(self):
        self.ip = 'http://' + PokeServer.get_ip() + ':' + str(PokeServer.get_port()) + '/'

    def _req(self):
        return requests.post(self.ip + 'shutdown')

    def test_shutdown(self):
        try:
            t = Timer(0.25, self._req)
            t.start()
            PokeServer.start_server()
        except exc:
            self.fail('Server shutdown failed by raising an unexpected exception!')
            sys.exit(0)

if __name__ == '__main__':
    unittest.main() 
        
