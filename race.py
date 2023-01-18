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

class Spaceship:
	
	def __init__(self, name, speed = 0, color = 'white', width = 0, height = 0, brand = 'none'):
		self._speed = speed
		self._name = name
		self._color = color
		self._width = width
		self._height = height
		self._brand = brand

	def get_color(self):
		return self._color

	def get_width(self):
		return self._width

	def get_height(self):
		return self._height

	def get_brand(self):
		return self._brand

	def get_speed(self):
		return self._speed

	def __repr__(self):
		return f'<<{self._name}: {self._speed} km/h, {self._color}, {self._brand}, w: {self._width}, h: {self._height}>>'

	def __eq__(self, other):
		if self._speed >= other._speed:
			return True
		if self._color == other._color:
			return True
		if self._width == other._width:
			return True
		if self._height == other._height:
			return True
		if self._brand == other._brand:
			return True
		return False

class Garage:
	def __init__(self, max_size):
		self._max_size = max_size
		self._spaceships = []
	
	def add_spaceship(self, spaceship):
		if len(self._spaceships) < self._max_size:
			self._spaceships.append(spaceship)

	def search(self, spaceship_wanted):
		result = []
		for spaceship in self._spaceships:
			if spaceship == spaceship_wanted:
				result.append(spaceship)
		return result

if __name__ == '__main__':
	track = Track(3000)
	spaceship_1 = Spaceship('s001', 10, color = 'red', width = 100, height = 50, brand = 'star1')
	spaceship_2 = Spaceship('s002', 8, width = 100, height = 50, brand = 'star1')
	spaceship_3 = Spaceship('s003', 9, color = 'red', width = 100, height = 50, brand = 'star1')
	spaceship_4 = Spaceship('s004', 12, width = 100, height = 50, brand = 'star1')

	track.add_spaceship(spaceship_1)
	track.add_spaceship(spaceship_2)
	track.add_spaceship(spaceship_3)
	track.add_spaceship(spaceship_4)

	garage = Garage(12)
	garage.add_spaceship(spaceship_1)
	garage.add_spaceship(spaceship_2)
	garage.add_spaceship(spaceship_3)
	garage.add_spaceship(spaceship_4)

	spaceship_wanted = Spaceship('', speed = 8, color = 'red')
	print(f'Spaceship wanted:\n{spaceship_wanted}')
	result = garage.search(spaceship_wanted)
	print('Spaceships found:')
	for item in result:
		print(item)