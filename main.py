import pygame
import constants


def main():
    pygame.init()
    print(f'Starting asteroids!\nScreen width: {constants.SCREEN_WIDTH} \
          \nScreen height: {constants.SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    while True:
        screen.fill((0,0,0))
        pygame.display.flip()
        
    
    
if __name__ == '__main__':
    main()