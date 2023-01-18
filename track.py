class Track:
	
	def __init__(self, distance): #dunder => double underscore
		self._distance = distance
		self._spaceships = []
		self._winner = None
	
	def add_spaceship(self, spaceship):
		self._spaceships.append(spaceship)

	def start_race(self):
		self._winner = sorted(self._spaceships, key=lambda item: item.get_speed())[-1:]

	def get_winner(self):
		return self._winner

	def __repr__(self):
		result = ""
		for spaceship in self._spaceships:
			result += str(spaceship) + "\n"
		return result
