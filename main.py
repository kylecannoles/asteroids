import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    black = pygame.Color(0,0,0)
    clock = pygame.time.Clock()
    dt = 0
    #game loop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        pygame.display.flip()
        dt = clock.tick(60)
        dt /= 1000 # convert ms to seconds

if __name__ == "__main__":
    main()
