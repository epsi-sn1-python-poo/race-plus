class Pilot:
	def __init__(self, level): #level in [0..100]
		self._level = level

	def get_level(self):
		return self._level

class PilotNone(Pilot):
	def __init__(self):
		super().__init__(0)
