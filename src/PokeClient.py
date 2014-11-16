import requests
import XMLManager
from Pokestadium import Pokestadium
import lxml.etree as ET
from Pokebattle import Pokebattle

def _full_ip(ip):
    return 'http://' + ip + ':8080/'

def _get_xml(pok1, pok2 = None):
    return ET.tostring(XMLManager.get_xml(pok1, pok2), pretty_print = True).decode('utf-8')

def start_client():
    print('----- Modo Cliente -----\n')
    ip = input('Digite o ip desejado: ')
    pok = Pokestadium.choose_pokemon()
    req = requests.post(_full_ip(ip) + 'battle', data = _get_xml(pok))
    try:
        assert(req.status_code != 423)
        xml = ET.fromstring(req.text)
        assert(XMLManager.check_xml(xml))
        pok1 = XMLManager.get_pokemon(xml[0])
        pok2 = XMLManager.get_pokemon(xml[1])
        while not Pokebattle.is_battle_over(pok1, pok2):
            Pokebattle.show_less_info(pok1, pok2)
            i = Pokebattle.get_attack_id(pok1)
            req = requests.post(_full_ip(ip) + 'battle/attack/' + str(i + 1), data = req.text)
            assert(req.status_code != 423)
            xml = ET.fromstring(req.text)
            assert(XMLManager.check_xml(xml))
            pok1 = XMLManager.get_pokemon(xml[0])
            pok2 = XMLManager.get_pokemon(xml[1])
        w = Pokebattle.finish_battle(pok1, pok2)
        print('%s venceu.\n' % w.name)
    except ET.XMLSyntaxError:
        print('Recebido XML com erro')
    except AssertionError:
        if req.status_code == 423:
            print('Server disse que eu estou errado :(')
        else:
            print('XML não aceito')
