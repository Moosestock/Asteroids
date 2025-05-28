# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import(player)

def getInputs():
	pass

def updateGameWorld(clock, updatableCont, dt):
	dt = clock.tick(60) / 1000
	updatableCont.update(dt)

def drawGameScreen(screen, drawableCont):
	#clear the screen...
	screen.fill(ASTEROID_BACKGROUND_COLOUR)
	#draw shit...
	for shit in drawableCont:
		shit.draw(screen)
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

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	player.containers = (updatable, drawable)

	claude = player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		getInputs()

		updateGameWorld(clock, updatable, dt)

		drawGameScreen(screen, drawable)


if __name__ == "__main__":
	main()
