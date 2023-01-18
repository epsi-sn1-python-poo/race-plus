class Track:
	
	def __init__(self, distance):
		self._distance = distance
		self._spaceships = []
		self._winner = None
	
	def add_spaceship(self, spaceship):
		self._spaceships.append(spaceship)

	def start_race(self):
		self._winner = sorted(self._spaceships, key=lambda item: item.get_speed())[-1:]

	def get_winner(self):
		return self._winner

class Spaceship:
	
	def __init__(self, name, speed):
		self._speed = speed
		self._name = name

	def get_speed(self):
		return self._speed

	def __repr__(self):
		return f'{self._name}: {self._speed} km/h'

track = Track(3000)
spaceship_1 = Spaceship('s001', 10)
spaceship_2 = Spaceship('s002', 8)
spaceship_3 = Spaceship('s003', 9)
spaceship_4 = Spaceship('s004', 12)

track.add_spaceship(spaceship_1)
track.add_spaceship(spaceship_2)
track.add_spaceship(spaceship_3)
track.add_spaceship(spaceship_4)

track.start_race()
print(track.get_winner())