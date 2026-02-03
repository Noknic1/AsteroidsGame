import pygame
import player
from asteroid import Asteroid
import sys
from asteroidsfield import AsteroidField
from shot import Shot
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from logger import log_event

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    gametime = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()    
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    _asteroidField = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    _player = player.Player(x, y)
  
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                 
      
        updatable.update(dt)

        for colliders in asteroids:
            for bullet in shots:
                if(colliders.collides_with(bullet)):
                    log_event("asteroid_shot")
                    bullet.kill()
                    colliders.split()

            if(colliders.collides_with(_player)):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        Black = (0,0,0)
        screen.fill(Black)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        delta_time = gametime.tick(60)
        dt = delta_time/ 1000
        
if __name__ == "__main__":
    main()
