import time
import os
try: import keyboard
except:
	print("Please activate the virtual environment using 'env\\Scripts\\activate' and try again. That works I think.")
	exit()
import random

score = 0
side = 16
delay = .2
velocity = [1, 0]
buffer = []
body = []
head = [4, 8]
food = [8, 5]

running = True

def draw():
	os.system('cls')

	print((' ' * (side - 1)) + str(score))


	for y in range(side):
		for x in range(side):
			if [x, y] == head:
				print("█ ", end="")
			elif [x, y] in body:
				print("■ ", end="")
			elif [x, y] == food:
				print("♥ ", end="")
			else:
				print("· ", end="")
		print()

def changeDirection(event):
	if event.event_type != keyboard.KEY_DOWN:
		return
		
	if event.name == 'w':
		buffer.append([0, -1])
	elif event.name == 'a':
		buffer.append([-1, 0])
	elif event.name == 's':
		buffer.append([0, 1])
	elif event.name == 'd':
		buffer.append([1, 0])

	if len(buffer) > 2:
		if buffer[-1] == buffer[-2]:
			buffer.pop()

def mainLoop():
	global running
	global score
	global food
	global velocity
	global delay

	if buffer: 
		if buffer[0] == [-velocity[0], -velocity[1]]:
			buffer.pop(0)
		else:
			velocity = buffer.pop(0)

	head[0] += velocity[0]
	head[1] += velocity[1]

	if head in body:
		running = False
	elif head != [head[0] % side, head[1] % side]:
		running = False
	elif head == food:
		score += 1
		delay *= 0.95
		while food in body or food == head:
			food = [random.randrange(0, side), random.randrange(0, side)]

	body.append([head[0], head[1]])
	del (body[0:-(score+3)])


keyboard.on_press(changeDirection)

while running:
	draw()
	time.sleep(delay)
	mainLoop()