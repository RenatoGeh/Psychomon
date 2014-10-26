from Pokemon import Pokemon

class Pokebattle:
    "Pokebattle class constructor."
    def __init__(self, pok1, pok2):
        # Sorts pokemons by speed
        if pok2.current_atts.spd > pok1.current_atts.spd:
            pok1, pok2 = pok2, pok1
        self.pokemon1 = pok1
        self.pokemon2 = pok2

    def get_attack_id(self, pokemon):
        while True:
            x = input('\nEnter the desired attack: ')
            print()
            try:
                x = int(x)
                assert(x > 0)
                assert(x < len(pokemon.atks))
                assert(pokemon.atks[x - 1].ppc > 0)
                return x - 1
            except (ValueError, AssertionError):
                print('You can\'t use that move!')
    
    "Starts the battle between two pokemons."
    def fight(self):
        # The fastest pokemon starts
        cur_pok = self.pokemon1 # Current active pokemon
        cur_opp = self.pokemon2 # Current opponent pokemon

        while(cur_pok.current_atts.hp > 0 and cur_opp.current_atts.hp > 0):
            print('\n%s, it\'s your turn!\n\nHP: %d/%d\nAvailable moves:' % (cur_pok.name, cur_pok.current_atts.hp, cur_pok.atts.hp))

            # Checks if the current pokemon can use any move.
            no_move = True

            basic_atks = cur_pok.atks[0 : -1]
            for atk in basic_atks:
                if atk.ppc:
                    no_move = False
                    break
            if no_move:
                # If a pokemon has no moves left, it must use struggle
                print('You can\'t use any move!')
                cur_pok.attack(cur_opp, Pokemon.STRUGGLE)
            else:
                for i, atk in enumerate(basic_atks):
                    # Prints each moves the pokemon has along with the corresponding pp.
                    print(' %d - %s (%d/%d)' % (i + 1, atk.name, atk.ppc, atk.ppi))

                cur_pok.attack(cur_opp, self.get_attack_id(cur_pok))
                    
                
            # Changes the current pokemon
            cur_pok, cur_opp = cur_opp, cur_pok
            
        if cur_pok.current_atts.hp > 0:
            print(cur_opp.name + ' fainted!')
            winner = cur_pok
        elif cur_opp.current_atts.hp > 0:
            print(cur_pok.name + ' fainted!')
            winner = cur_opp
        else:
            print(cur_pok.name + ' and ' + cur_opp.name + ' fainted!\nIt\'s a draw!')
            winner = None

        return winner
