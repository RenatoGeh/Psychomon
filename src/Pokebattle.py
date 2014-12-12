from Pokemon import Pokemon

class Pokebattle:
    "Pokebattle class constructor."
    def __init__(self, poke1, poke2):
        if poke2.current_atts.spd > poke1.current_atts.spd:
            poke1, poke2 = poke2, poke1
        self.poke1 = poke1
        self.poke2 = poke2

    @staticmethod 
    def is_valid_id(pokemon, i):
        return i > 0 and i < len(pokemon.atks) and pokemon.atks[i - 1].current_pp > 0

    @staticmethod
    def get_attack_id(pokemon, opp=None):
        if pokemon.has_moves():
            if opp == None:
                while True:
                    x = input('\nEnter the desired attack: ')
                    print()
                    try:
                        x = int(x)
                        assert(Pokebattle.is_valid_id(pokemon, x))
                        return x - 1
                    except (ValueError, AssertionError):
                        print('You can\'t use that move!')
            else:
                max_id = -1
                for i in range(0, len(pokemon.atks) - 1):
                    if pokemon.atks[i].current_pp > 0 and (max_id == -1 or 
                        pokemon.atks[i].get_average_damage(pokemon, opp) > pokemon.atks[max_id].get_average_damage(pokemon, opp)):
                        max_id = i
                print('You chose %s.' % pokemon.atks[max_id].name)
                return max_id
        else:
            # If a pokemon has no moves left, it must use struggle
            print('You can\'t use any move!')
            return Pokemon.STRUGGLE

    @staticmethod
    def is_battle_over(pok1, pok2):
        return pok1.current_atts.hp <= 0 or pok2.current_atts.hp <= 0

    @property
    def is_over(self):
        return Pokebattle.is_battle_over(self.poke1, self.poke2)

    @staticmethod
    def show_less_info(pok1, pok2):
        print('\n%s (%d HP) vs %s (%d HP)' % (pok1.name, pok1.current_atts.hp, pok2.name, pok2.current_atts.hp))
        print('\n%s, it\'s your turn!\n\nAvailable moves:' % pok1.name)
        for i, atk in enumerate(pok1.atks[0 : -1]):
            # Prints each moves the pokemon has along with the corresponding pp.
            print(' %d - %s (%d PP)' % (i + 1, atk.name, atk.current_pp))


    @staticmethod
    def show_info(pok1, pok2):
        print('\n%s (%d/%d HP) vs %s (%d/%d HP)' % ((pok1.name, pok1.current_atts.hp, pok1.atts.hp)
            + (pok2.name, pok2.current_atts.hp, pok2.atts.hp)))
        print('\n%s, it\'s your turn!\n\nHP: %d/%d\nAvailable moves:' % (pok1.name, pok1.current_atts.hp, pok1.atts.hp))
        for i, atk in enumerate(pok1.atks[0 : -1]):
            # Prints each moves the pokemon has along with the corresponding pp.
            print(' %d - %s (%d/%d)' % (i + 1, atk.name, atk.current_pp, atk.base_pp))

    @staticmethod
    def finish_battle(pok1, pok2):
        assert(Pokebattle.is_battle_over(pok1, pok2))
        winner = None
        if pok1.current_atts.hp > 0:
            print(pok2.name + ' fainted!')
            winner = pok1
        elif pok2.current_atts.hp > 0:
            print(pok1.name + ' fainted!')
            winner = pok2
        else:
            print(pok1.name + ' and ' + pok2.name + ' fainted!\nIt\'s a draw!')
            winner = None

        return winner


    def _finish_fight(self):
        return Pokebattle.finish_battle(self.poke1, self.poke2)
    
    "Starts the battle between two pokemons."
    def fight(self):
        # The fastest pokemon starts
        cur_pok = self.poke1 # Current active pokemon
        cur_opp = self.poke2 # Current opponent pokemon
        # Sorts pokemons by speed

        while not self.is_over:
            Pokebattle.show_info(cur_pok, cur_opp)

            cur_pok.attack(cur_opp, Pokebattle.get_attack_id(cur_pok))

            # Changes the current pokemon
            cur_pok, cur_opp = cur_opp, cur_pok
        return self._finish_fight()
            
