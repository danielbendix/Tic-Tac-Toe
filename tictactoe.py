#! /usr/bin/env python

def wins(plate):
	wins = list()
	for i in range (0, 3):
		if plate[i][0] == plate[i][1] == plate[i][2] != 0:
			wins.append( [(i, 0), (i, 1), (i, 2)] )
		if plate[0][i] == plate[1][i] == plate[2][i] != 0:
			wins.append( [(0, i), (1, i), (2, i)] )
	if plate[0][0] == plate[1][1] == plate[2][2] != 0:
		wins.append( [(0, 0), (1, 1), (2, 2)] )
	if plate[0][2] == plate[1][1] == plate[2][0] != 0:
		wins.append( [(0, 2), (1, 1), (2, 0)] )
	return wins

# Import the pygame library
import pygame

# Initialize pygame
pygame.init()

# Declare constants
pi = 3.1415926535
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Set the height and width of window
size = [550, 550]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Kryds og Bolle")

# Create a 2-dimensional list for storing crosses and circles
plate = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Define an integer to designate the starting player
player = 1

# Define a variable to hold the coordinates for the three in a row
win = list()

# Set the main loop control variable "done" to False
done = False

# Define a variable that tells whether or not the game state can be edited
editable = True

# Create a game clock for controlling frame rate
clock = pygame.time.Clock()

while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_BACKSPACE:
				plate = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
				player = 1
				editable = True
				win = list()
		if event.type == pygame.MOUSEBUTTONDOWN:
			x = -1
			y = -1
			mouse_coords = pygame.mouse.get_pos()
			
			if mouse_coords[0] >= 0 and mouse_coords[0] < 181:
				x = 0
			elif mouse_coords[0] > 185 and mouse_coords[0] < 365:
				x = 1
			elif mouse_coords[0] > 370 and mouse_coords[0] <= 550:
				x = 2
			
			if mouse_coords[1] >= 0 and mouse_coords[1] < 181:
				y = 0
			elif mouse_coords[1] > 185 and mouse_coords[1] < 365:
				y = 1
			elif mouse_coords[1] > 370 and mouse_coords[1] <= 550:
				y = 2
				
			if (x + 1) and (y + 1):
				if editable and not plate[x][y]:
					plate[x][y] = player
					if player == 1:
						player = 2
					elif player == 2:
						player = 1
				win = wins(plate)
				if win:
					editable = False
			
			
	# Drawing initial game UI		
	screen.fill(white)
	pygame.draw.line(screen, black, [183, 0], [183, 550], 5)
	pygame.draw.line(screen, black, [366, 0], [366, 550], 5)
	pygame.draw.line(screen, black, [0, 183], [550, 183], 5)
	pygame.draw.line(screen, black, [0, 367], [550, 367], 5)
	
	for x in range (0, 3):
		for y in range (0, 3):
			if plate[x][y] == 1:
				pygame.draw.line(screen, black, [20 + 185 * x, 20 + 185 * y], [160 + 185 * x, 160 + 185 * y], 10)
				pygame.draw.line(screen, black, [160 + 185 * x, 20 + 185 * y], [20 + 185 * x, 160 + 185 * y], 10)
			if plate[x][y] == 2:
				pygame.draw.circle(screen, black, [90 + x * 185, 90 + y * 185], 70, 10)
				
	for i in win:
		pygame.draw.line(screen, red, [90 + 185 * i[0][0], 90 + 185 * i[0][1]], [90 + 185 * i[2][0], 90 + 185 * i[2][1]], 5)
	
			
	pygame.display.flip()
	clock.tick(20)