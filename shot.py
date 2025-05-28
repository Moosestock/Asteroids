#Shot class

import pygame
from circleshape import(CircleShape)
from constants import(ASTEROID_PLAYER_COLOUR)

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_PLAYER_COLOUR, (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

