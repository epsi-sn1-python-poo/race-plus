class Garage:
	def __init__(self, max_size):
		self._max_size = max_size
		self._spaceships = []
	
	def add_spaceship(self, spaceship):
		'''Add spaceship until max size is reached'''
		if len(self._spaceships) < self._max_size:
			self._spaceships.append(spaceship)

	def search(self, spaceship_wanted):
		result = []
		for spaceship in self._spaceships:
			if spaceship == spaceship_wanted:
				result.append(spaceship)
		return result