from pilot import PilotNone

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

