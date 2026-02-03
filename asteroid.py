import circleshape
import pygame
import random
from logger import log_event
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__(self, x,y,radius):
        super().__init__(x,y,radius)
        
    def draw(self, screen):
        white = (255,255,255)
        pygame.draw.circle(screen, white, self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt  

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        randomvalue = random.uniform(20,50)
        _velocity = self.velocity.rotate(randomvalue)
        _velocity2 = self.velocity.rotate(-randomvalue)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        _asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        _asteroid1.velocity = _velocity * 1.2
        _asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        _asteroid2.velocity = _velocity2 * 1.2