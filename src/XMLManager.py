import lxml.etree as ET

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
        _add_attr(atts, 'health', poke.atts.hp)
        _add_attr(atts, 'attack', poke.atts.atk)
        _add_attr(atts, 'defense', poke.atts.df)
        _add_attr(atts, 'speed', poke.atts.spd)
        _add_attr(atts, 'special', poke.atts.spc)

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
            _add_attr(atks, 'power_points', atk.base_pp)
    return bs
