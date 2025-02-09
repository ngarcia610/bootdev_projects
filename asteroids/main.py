import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

'''
To-do
    Add a scoring system
    Implement multiple lives and respawning
    Add an explosion effect for the asteroids
    Add acceleration to the player movement
    Make the objects wrap around the screen instead of disappearing
    Add a background image
    Create different weapon types
    Make the asteroids lumpy instead of perfectly round
    Make the ship have a triangular hit box instead of a circular one
    Add a shield power-up
    Add a speed power-up
    Add bombs that can be dropped
'''

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    dt = 0

    while True:
        #Kills the process when the window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

