import pygame
from circleshape import(CircleShape)
from constants import(PLAYER_RADIUS, ASTEROID_PLAYER_COLOUR)

# Player class
class player(CircleShape):
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
#		print(playerPosition)

