import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shoot import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    updatabe = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updatabe, drawable)
    Asteroid.containers = (asteroids, updatabe, drawable)
    AsteroidField.containers = updatabe
    Shoot.containers = (bullets, updatabe, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatabe.update(dt)

        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.detect_collision(bullet):
                    asteroid.split()
                    bullet.kill()
                    score += asteroid.score()

        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print(f"Game Over!")
                print(f"Score: {score}")
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
    
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()