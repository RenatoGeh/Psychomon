from Pokemon import Pokemon

class Pokebattle:
    "Pokebattle class constructor."
    def __init__(self, pok1, pok2):
        # Sorts pokemons by speed
        if pok2.spd > pok1.spd:
            pok1, pok2 = pok2, pok1
        self.pokemon1 = pok1
        self.pokemon2 = pok2
    
    "Starts the battle between two pokemons."
    def fight(self):
        # The fastest pokemon starts
        cur_pok = self.pokemon1 # Current active pokemon
        cur_opp = self.pokemon2 # Current opponent pokemon

        while(cur_pok.hp > 0 and cur_opp.hp > 0):
            print(cur_pok.name + ', it\'s your turn!\nHP:' + str(cur_pok.current_atts.hp) + '/' + str(cur_pok.atts.hp) + '\nAvailable moves:')

            # Checks if the current pokemon can use any move.
            no_move = True

            for atk in cur_pok.atks:
                if atk.ppc:
                    no_move = False
                    break
            if no_move:
                # If a pokemon has no moves left, it must use struggle
                print('You can\'t use any move!')
                cur_pok.attack(cur_opp, Pokemon.STRUGGLE)
            else:
                for i, atk in enumerate(cur_pok.atks):
                    # Prints each moves the pokemon has along with the corresponding pp.
                    print(str(i + 1) + '. ' + atk.name + '--pp:' + str(atk.ppc) + '/' + str(atk.ppi))

                x = input('Type the number of your desired move:')
                while cur_pok.atks[x].ppc == 0:
                    print('You can\'t use that move!')
                    x = input('Type the number of your desired move:')
                cur_pok.attack(cur_opp, x - 1)
                    
                
            # Changes the current pokemon
            cur_pok, cur_opp = cur_opp, cur_pok
            
        if cur_pok.hp > 0:
            print(cur_opp.name + ' fainted!')
            winner = cur_pok
        elif cur_opp.hp > 0:
            print(cur_pok.name + ' fainted!')
            winner = cur_opp
        else:
            print(cur_pok.name + ' and ' + cur_opp.name + ' fainted!\nIt\'s a draw!')
            winner = None

        return winner
