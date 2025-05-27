# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import(player)

def getInputs():
	pass

def updateGameWorld():
	pass

def drawGameScreen(screen, player):
	#clear the screen...
	screen.fill(ASTEROID_BACKGROUND_COLOUR)
	#draw shit...
	player.draw(screen)
	#update the screen
	pygame.display.flip()


def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	claude = player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		getInputs()

		updateGameWorld()

		drawGameScreen(screen, claude)

		dt = clock.tick(60) / 1000
		


if __name__ == "__main__":
	main()
