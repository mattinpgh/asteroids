# asteroids/shot.py

import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius=SHOT_RADIUS)
        self.x = x
        self.y = y
        self.position = pygame.Vector2(self.x, self.y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = SHOT_RADIUS
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
        