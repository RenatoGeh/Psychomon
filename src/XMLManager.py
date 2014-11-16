import lxml.etree as ET
from Pokemon import Pokemon
from Pokedata import Attribute, Attack

with open('resources/pokemon.xsd', 'r') as f:
    validator = ET.XMLSchema(ET.parse(f))

def check_xml(xml):
    return validator.validate(xml)

def _add_attr(node, name, value):
    ET.SubElement(node, name).text = str(value)

def get_xml(poke1, poke2=None):
    bs = ET.Element('battle_state')
    for poke in (poke1, poke2):
        if poke == None:
            continue
        pk = ET.SubElement(bs, 'pokemon')
        _add_attr(pk, 'name', poke.name)
        _add_attr(pk, 'level', poke.lvl)
        atts = ET.SubElement(pk, 'attributes')
        _add_attr(atts, 'health', 0 if poke.current_atts.hp < 0 else poke.current_atts.hp)
        _add_attr(atts, 'attack', poke.current_atts.atk)
        _add_attr(atts, 'defense', poke.current_atts.df)
        _add_attr(atts, 'speed', poke.current_atts.spd)
        _add_attr(atts, 'special', poke.current_atts.spc)

        _add_attr(pk, 'type', poke.types[0])
        _add_attr(pk, 'type', poke.types[1])
        for i, atk in enumerate(poke.atks):
            if atk.name == 'Struggle':
                continue
            atks = ET.SubElement(pk, 'attacks')
            _add_attr(atks, 'id', i + 1)
            _add_attr(atks, 'name', atk.name)
            _add_attr(atks, 'type', atk.typ)
            _add_attr(atks, 'power', atk.pwr)
            _add_attr(atks, 'accuracy', atk.acu)
            _add_attr(atks, 'power_points', atk.current_pp)
    return bs

def get_pokemon(p):
    at = p[2]
    attr = Attribute(int(at[0].text), int(at[1].text), int(at[2].text), int(at[3].text), int(at[4].text))
    atks = [None, None, None, None]
    i = 5
    while True:
        try:
            at = p[i]
            atks[int(at[0].text) - 1] = Attack(at[1].text, int(at[2].text), int(at[4].text), int(at[3].text), int(at[5].text))
            i += 1
        except IndexError:
            break
    while atks[-1] == None:
        atks.pop()
    return Pokemon(p[0].text, int(p[1].text), attr, atks, int(p[3].text), int(p[4].text))