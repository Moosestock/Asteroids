# Player class
import pygame
from circleshape import(CircleShape)
from shot import(Shot)
from constants import *

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0

	def triangle(self):
	    forward = pygame.Vector2(0, 1).rotate(self.rotation)
	    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
	    a = self.position + forward * self.radius
	    b = self.position - forward * self.radius - right
	    c = self.position - forward * self.radius + right
	    return [a, b, c]

	def draw(self, screen):
		trianglePoints = self.triangle()
		playerPosition = [tuple(point) for point in trianglePoints]

		pygame.draw.polygon(screen, ASTEROID_PLAYER_COLOUR, playerPosition, 2)

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def shoot(self):
		projectile = Shot(*self.position, SHOT_RADIUS)
		projectile.position = self.position.copy()
		projectile.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED

	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_SPACE]:
		    self.shoot()

