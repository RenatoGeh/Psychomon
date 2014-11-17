from flask import Flask, request
import XMLManager
import io
import lxml.etree as ET
from Pokebattle import Pokebattle
from Pokestadium import Pokestadium

_ip = '0.0.0.0'
_port = 8080
app = Flask(__name__)

def _get_xml(pok1, pok2 = None):
    return ET.tostring(XMLManager.get_xml(pok1, pok2)).decode('utf-8')

def _start_battle(poke1):
    print('A challenger approaches!\n')
    poke2 = Pokestadium.choose_pokemon('Choose your pokémon: ')
    print('The challenger sent out %s\n' % poke1.name)
    # if server's pokemon is the first, attack
    if poke2.current_atts.spd > poke1.current_atts.spd:
        Pokebattle.show_less_info(poke2, poke1)
        poke2.attack(poke1, Pokebattle.get_attack_id(poke2))
    return _get_xml(poke1, poke2), 200

@app.route('/battle', methods = ['POST'])
def _start_battle_request():
    try:
        xml = ET.fromstring(request.data)
        assert(XMLManager.check_xml(xml))
        pok1 = XMLManager.get_pokemon(xml[0])
        return _start_battle(pok1)
    except ET.XMLSyntaxError:
        print('Data not a correct XML')
        return 'Data not a correct XML', 423
    except AssertionError:
        print('Invalid XML')
        return 'Invalid XML', 423

def _battle_over(p1, p2):
    w = Pokebattle.finish_battle(p1, p2)
    print('%s won.\n\n' % w.name)
    return _get_xml(p1, p2), 200


@app.route('/battle/attack/<i>', methods = ['POST'])
def _process_attack(i):
    try:
        i = int(i)
        xml = ET.fromstring(request.data)
        assert(XMLManager.check_xml(xml))
        pok1 = XMLManager.get_pokemon(xml[0])
        pok2 = XMLManager.get_pokemon(xml[1])
        if pok1.has_moves():
            assert(Pokebattle.is_valid_id(pok1, i))
        else:
            assert(i == 0)
        pok1.attack(pok2, i - 1)
        if Pokebattle.is_battle_over(pok1, pok2):
            return _battle_over(pok1, pok2)
        Pokebattle.show_less_info(pok2, pok1)
        pok2.attack(pok1, Pokebattle.get_attack_id(pok2))
        if Pokebattle.is_battle_over(pok1, pok2):
            return _battle_over(pok1, pok2)
        else:
            return _get_xml(pok1, pok2), 200
    except ValueError:
        print('Attack id not integer')
        return 'Attack id not integer', 423
    except ET.XMLSyntaxError:
        print('Data not a correct XML')
        return 'Data not a correct XML', 423
    except AssertionError:
        print('Invalid XML or attack id')
        return 'Invalid XML or attack id', 423

@app.route('/shutdown', methods=['POST'])
def _shutdown():
    func = request.environ.get('werkzeug.server.shutdown')

    if func is None:
        raise RuntimeError('Werkzeug server error.')

    func()

    return 'Server shutting down...'

def get_ip():
    return _ip

def get_port():
    return _port

def start_server(ip = '0.0.0.0', p = 8080):
    global _ip
    global _port

    print('----- Server Mode -----\n')

    _ip = ip
    _port = p

    app.run(ip, port = p, debug = True, use_reloader = False)
