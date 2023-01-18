from track import Track
from pilot import Pilot
from garage import Garage
from spaceship import Spaceship, Cruiser, Fighter

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