import Pokemon

class Pokeplayer:
	"Pokeplayer class constructor."
	def __init__(self, name, *args):
		self.name = name
		self.pokemons = args
		self.poke_index = 0

	"Updates Pokeplayer."
	def update(self):
		# Checks whether current pokemon has fainted. Prompts user for input and such.
		pass

	"I choose yooooouuuuu!"
	def choose(self):
		index = input("Select pokemon: ")
		self.poke_index = int(index)
	
	
		
