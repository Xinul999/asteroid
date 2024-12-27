# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys

import pygame
from pygame import Color

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    flag_running = True
    clock = pygame.time.Clock()
    dt = 0


    while flag_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_running = False
                pygame.quit()
                sys.exit()

        #player.update(dt)
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                flag_running = False
            for shot in shots:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()

        screen.fill(Color(0, 0, 0))

        #player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
