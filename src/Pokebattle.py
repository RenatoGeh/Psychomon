import Pokemon

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
        #Begins the fight starting with the faster pokemon (pokemon1).'
        cur_pok = pokemon1 #current active pokemon
        cur_opp = pokemon2 #current opponent pokemon
        while(not self.pokemon1.hp or not self.pokemon2.hp):
            s = repr(cur_pok.name) + ', it\'s your turn!\nHP:' + repr(cur_pok.current_atts.hp) + '/' + repr(cur_pok.atts.hp) + '\nAvailable moves:'  
            print(s)
            #Checks if the current pokemon can use any move.
            no_move = True
            for i in range (0, len(cur_pok.atks)):
                if cur_pok.atks[i].ppc:
                    no_move = False
            if not no_move:        
                for i in range (0, len(cur_pok.atks)):
                    #Prints each moves the pokemon has along with the correspondent pp.
                    s = repr(i) + '. ' + repr(cur_pok.atks[i].name) + '--pp:' + repr(cur_pok.atks[i].ppc) + '/' + repr(cur_pok.atks[i].ppi)
                    print(s)
                x = input('Type the number of your desired move:')
                while not cur_pok.atks[x].ppc:
                    print('You can\'t use that move!')
                    x = input('Type the number of your desired move:')
                cur_pok.attack(cur_opp, x-1)    
                    
            #If pokemon has no move with pp left, he must use struggle
            else:
                print('You can\'t use any move!')
                cur_pok.struggle.attack(cur_opp)
                
            #Changes who is the current pokemon so it\'s the next pokemon turn.   
            cur_pok, cur_opp = cur_opp, cur_pok
            
        if self.pokemon1.hp:
            s = repr(pokemon2.name) + ' fainted!' 
            print(s)
            winner = pokemon1
        elif self.pokemon2.hp:
            s = repr(pokemon1.name) + ' fainted!' 
            print(s)
            winner = pokemon2
        else:
            s = repr(pokemon1.name) + ' and ' + repr(pokemon2.name) + ' fainted!\nIt\'s a draw!' 
            print(s)
            winner = None

        return winner
