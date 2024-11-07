import pygame
import constants


def main():
    pygame.init()
    print(f'Starting asteroids!\nScreen width: {constants.SCREEN_WIDTH} \
          \nScreen height: {constants.SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
    
    
if __name__ == '__main__':
    main()