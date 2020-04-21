from time import sleep
import main
from keyboard import is_presses as ip



def initialize():
	print('Preparing to run program. Do you want to continue? (Y/N)')
	check2 = input()
	if check2.casefold() == 'n':
		return(False)
	elif check2.casefold() == 'y':
		return(True)
	else:
		print('Invalid input, please try again')

def commands():
	if ip('~'):
		print('Paused, press any key to continue recording')
		input()
	elif ip('|'):
		break
	else:
		main()

check = True
while(check):
	init = initialize()
	if init:
		print('Set frequency by inputing the number of minites between retreivals:')
		period_min = input()
		print(f'Freqency set to {round(60/period_min)} retreivals from FB per hour')
		print('To start/pause recording, press "~" (shift + key above tab). To quit recording press "|" (shift + key above enter).')
		commands()
		print('Ending program and recording')
		break
	elif not init:
		print("Then why'd you run the program?? Ugh, shutting down...")
	else:
		break

