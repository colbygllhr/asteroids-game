# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def print_intro():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


def main():
    print_intro()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    Shot.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updateable:
            thing.update(dt)
            
        
        for asteroid in asteroids:
            if(asteroid.detect_collision(player) == True):
                print("Game over!")
                exit()
        
        screen.fill((0, 0, 0))

        for thing in drawable:
            thing.draw(screen)


        pygame.display.flip() #display update
        dt = clock.tick(60) / 1000

    
if __name__ == "__main__":
    main()