import Pokedata
import copy

class Pokemon:
	"Pokemon class constructor."
	def __init__(self, atts, atks, type1, type2="Blank"):
		self.atts = atts
		self.current_atts = copy.copy(atts)	# Current attribute takes into account ATT altering attacks.
		self.atks = atks
		self.types = (type1, type2)
		'The default struggle attack is present in all pokemon.'
		self.struggle = Pokedata.Attack('Struggle', 0, 100, 50, 100000)
	
	"This pokemon attacks target opponent pokemon with given attack."
	def attack(self, opponent, atk_index):
		self.atks[atk_index].attack(opponent)

		
