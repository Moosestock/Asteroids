# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def getInputs():
	pass

def updateGameWorld():
	pass

def drawGameScreen(screen):
	screen.fill(ASTEROID_BACKGROUND_COLOUR)
	pygame.display.flip()

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		getInputs()

		updateGameWorld()

		drawGameScreen(screen)


if __name__ == "__main__":
	main()
