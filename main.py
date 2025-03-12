import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    updatabe = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatabe, drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    Asteroid.containers = (asteroids, updatabe, drawable)
    AsteroidField.containers = (updatabe)
    asteroid_field = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0,1))

        for obj in drawable:
            obj.draw(screen)

        updatabe.update(dt)
    
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()