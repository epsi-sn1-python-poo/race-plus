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

class Pilot:
	def __init__(self, level): #level in [0..100]
		self._level = level

	def get_level(self):
		return self._level

class PilotNone(Pilot):
	def __init__(self):
		super().__init__(0)


class Spaceship:
	
	def __init__(self, name, speed = 0, color = 'white', width = 0, height = 0, brand = 'none'):
		self._speed = speed
		self._name = name
		self._color = color
		self._width = width
		self._height = height
		self._brand = brand
		self._pilot = PilotNone()

	def add_pilot(self, pilot):
		self._pilot = pilot

	def get_color(self):
		return self._color

	def get_width(self):
		return self._width

	def get_height(self):
		return self._height

	def get_brand(self):
		return self._brand

	def get_speed(self):
		return round(self._speed * self._pilot.get_level() / 100, 2)

	def __repr__(self):
		return f'<<{self._name}: {self._speed} km/h ({self.get_speed()} km/h), {self._color}, {self._brand}, w: {self._width}, h: {self._height}>>'

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

class Cruiser(Spaceship):
	'''Cruiser decreseases the speed by 5%'''
	def __init__(self, name, speed = 0, color = 'white', width = 0, height = 0, brand = 'none'):
		super().__init__(name, round(speed * 0.95, 2), color, width, height, brand)

class Fighter(Spaceship):
	def __init__(self, name, speed = 0, color = 'white', width = 0, height = 0, brand = 'none'):
		super().__init__(name, round(speed * 1.05, 2), color, width, height, brand)
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

if __name__ == '__main__':
	track = Track(3000)
	spaceship_1 = Cruiser('s001', 10, color = 'red', width = 100, height = 50, brand = 'star1')
	spaceship_2 = Fighter('s002', 8, width = 100, height = 50, brand = 'star1')
	spaceship_3 = Cruiser('s003', 9, color = 'red', width = 100, height = 50, brand = 'star1')
	spaceship_4 = Cruiser('s004', 12, width = 100, height = 50, brand = 'star1')

	han_solo = Pilot(70)
	anakin = Pilot(90)
	chewbacca = Pilot(45)

	spaceship_1.add_pilot(han_solo)
	spaceship_2.add_pilot(anakin)
	spaceship_3.add_pilot(chewbacca)

	track.add_spaceship(spaceship_1)
	track.add_spaceship(spaceship_2)
	track.add_spaceship(spaceship_3)
	track.add_spaceship(spaceship_4)

	print(track)
	track.start_race()
	print(f'Winner is: {track.get_winner()}')

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
	print(Cruiser.__doc__)