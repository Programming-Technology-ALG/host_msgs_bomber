try:
	from pymouse import PyMouse
	from pykeyboard import PyKeyboard
except ImportError:
	import pip
	pip.main(['install', 'PyUserInput'])
	from pymouse import PyMouse
	from pykeyboard import PyKeyboard

import time
import random
import sys

if len(sys.argv) < 2:
	print("Run the script with arguments: repeats message_1 message_2 ...")
	print("Example: python3 name.py 5 Hello Sun Green")
	sys.exit(0)

MOUSE_DEVICE = PyMouse()
KEYBOARD_DEVICE = PyKeyboard()
x_dim, y_dim = MOUSE_DEVICE.screen_size()

if sys.argv[1].isnumeric():
	total_messages = int(sys.argv[1])
else: 
	print("Error: first parameter MUST be integer!")
	sys.exit(0)

teg_list = []
for i in range(2, len(sys.argv)):
	teg_list.append(sys.argv[i])

print("Script is started...\nTo stop press cntr + C")

for i in range(total_messages):
	word_printed = random.choice(teg_list)		# Choose the word to print

	MOUSE_DEVICE.click(150,y_dim-100,1)			# Activate input line
	KEYBOARD_DEVICE.type_string(word_printed)	# Type word
	print(f"{i + 1}: {word_printed}")			# Log output

	#time.sleep(random.randint(0, 1))
	MOUSE_DEVICE.click(350,y_dim-100,1)			# Send message
	MOUSE_DEVICE.click(400,y_dim-100,1)			# Activate console

	if (i + 1) % 15 == 0:
		print("Pause. Press cntr + C to stop")
		time.sleep(random.randint(2, 3))
	else:
		time.sleep(random.randint(1, 3))
