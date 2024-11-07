# asteroids/circleshape.py


import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius
        
    def draw(self, screen):
        #here for subclasses to override
        pass
    
    def update(self, dt):
        #here for subclasses to override
        pass
    
    def get_collision(self, other):
        distance_between = pygame.math.Vector2.distance_to(self.position, other.position)      
        if distance_between <= (self.radius + other.radius):
            return True       