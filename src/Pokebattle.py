from Pokemon import Pokemon

class Pokebattle:
    "Pokebattle class constructor."
    def __init__(self, pok1, pok2):
        #Makes pokemon1 the faster pokemon. 
        if pok1.spd >= pok2.spd:
            self.pokemon1 = pok1
            self.pokemon2 = pok2
        else:
            self.pokemon1 = pok2
            self.pokemon2 = pok1
    
    "Starts the battle between two pokemons."
    def fight(self):
        # Begins the fight starting with the faster pokemon (pokemon1).'
        cur_pok = self.pokemon1 #current active pokemon
        cur_opp = self.pokemon2 #current opponent pokemon

        while(not cur_pok.hp or not cur_opp.hp):
            print(cur_pok.name + ', it\'s your turn!\nHP:' + str(cur_pok.current_atts.hp) + '/' + str(cur_pok.atts.hp) + '\nAvailable moves:')

            # Checks if the current pokemon can use any move.
            no_move = True

            for i in range (0, len(cur_pok.atks)):
                if cur_pok.atks[i].ppc:
                    no_move = False
            if not no_move:        
                for i in range (0, len(cur_pok.atks)):
                    # Prints each moves the pokemon has along with the correspondent pp.
                    print(str(i) + '. ' + cur_pok.atks[i].name + '--pp:' + str(cur_pok.atks[i].ppc) + '/' + str(cur_pok.atks[i].ppi))

                x = input('Type the number of your desired move:')
                while not cur_pok.atks[x].ppc:
                    print('You can\'t use that move!')
                    x = input('Type the number of your desired move:')
                cur_pok.attack(cur_opp, x-1)
                    
            # If pokemon has no move with pp left, he must use struggle
            else:
                print('You can\'t use any move!')
                cur_pok.attack(cur_opp, Pokemon.STRUGGLE)
                
            # Changes who is the current pokemon so it\'s the next pokemon turn.   
            cur_pok, cur_opp = cur_opp, cur_pok
            
        if cur_pok.hp:
            print(cur_pok.name + ' fainted!')
            winner = cur_pok
        elif cur_opp.hp:
            print(pokemon1.name + ' fainted!') 
            winner = cur_opp
        else:
            print(cur_pok.name + ' and ' + cur_opp.name + ' fainted!\nIt\'s a draw!')
            winner = None

        return winner
