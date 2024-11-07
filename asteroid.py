# asteroids/asteroid.py
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.position = x, y
        self.velocity = pygame.Vector2(0,0)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def rotate(self, dt):
        self.rotation += dt * self.velocity
        
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        original_vector = self.velocity
        rotated_vector_1 = original_vector.rotate(angle)
        rotated_vector_2 = original_vector.rotate(-angle)
        print(f'The angle is {angle}')
        print(f'The original vector is {original_vector}')
        print(f'The rotated vector 1 is {rotated_vector_1}')
        print(f'The rotated vector 2 is {rotated_vector_2}')
        current_pos = self.position
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_roid_1 = Asteroid(current_pos[0], current_pos[1], new_radius)
        new_roid_2 = Asteroid(current_pos[0], current_pos[1], new_radius)
        new_roid_1.velocity = rotated_vector_1*1.2
        new_roid_2.velocity = rotated_vector_2*1.2
        