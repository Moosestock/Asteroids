# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import(Player)
from asteroid import(Asteroid)
from asteroidfield import(AsteroidField)
from shot import(Shot)

def getInputs():
	pass

def updateGameWorld(clock, updatableCont, asteroidCont, player, bullets, dt):
	dt = clock.tick(60) / 1000
	updatableCont.update(dt)
	for asteroid in asteroidCont:
		if asteroid.collision(player):
			sys.exit("Game over!")
		for bullet in bullets:
			if asteroid.collision(bullet):
				asteroid.split()
				bullet.kill()

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
	Player.containers = (updatable, drawable)

	claude = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroidfield = AsteroidField()

	bullets = pygame.sprite.Group()
	Shot.containers = (bullets, updatable, drawable)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		getInputs()

		updateGameWorld(clock, updatable, asteroids, claude, bullets, dt)

		drawGameScreen(screen, drawable)


if __name__ == "__main__":
	main()
