import Pokedata
import copy

class Pokemon:
	"Pokemon class constructor."
	def __init__(self, atts, atks, type1, type2="Blank"):
		self.atts = atts
		self.current_atts = copy.copy(atts)	# Current attribute takes into account ATT altering attacks.
		self.atks = atks
		self.types = (type1, type2)
	
	"This pokemon attacks target opponent pokemon with given attack."
	def attack(self, opponent, atk_index):
		self.atks[atk_index].attack(opponent)

		
