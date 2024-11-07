# asteroids/main.py


import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from circleshape import CircleShape


def main():
    pygame.init()
    print(f'Starting asteroids!\nScreen width: {SCREEN_WIDTH} \
          \nScreen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_model = Player((x, y))
    
    
    while True:
        screen.fill((0,0,0))
        player_model.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
    
    
if __name__ == '__main__':
    main()