# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()  # initialize the pygame library
    clock = pygame.time.Clock()  # create a clock to control the frame rate
    dt = 0  # delta time, used to control the speed of the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}"
          f"\nScreen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game Over!")
                sys.exit()


        screen.fill("black")

        for element in drawable:
            element.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0  # limit to 60 FPS


if __name__ == "__main__":
    main()