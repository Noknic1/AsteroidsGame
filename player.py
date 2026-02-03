
import circleshape
import pygame
import random
from constants import *
from shot import Shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.accuracy = PLAYER_ACCURACY + random.randrange(-20,20)
        self.numberofshots = PLAYER_NUMBER_SHOTS + random.randrange(0,10)
        self.currentvector = pygame.Vector2(0,0)

        # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        playercolor = (255,255,255)
        pygame.draw.polygon(screen, playercolor, self.triangle(), LINE_WIDTH)\
    
    def update(self, dt):
        self.shot_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(+dt)
        if keys[pygame.K_w]:
            self.move(+dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(self.numberofshots, self.accuracy)

        self.position += self.currentvector
        self.currentvector *= 0.98
        
    

    def rotate(self, value):     
        self.rotation += (value * PLAYER_TURN_SPEED)

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_ACCELERATION * dt
        currentspeed = self.currentvector.magnitude_squared()
        if(currentspeed < PLAYER_SPEED):
            self.currentvector += rotated_with_speed_vector
        
    def shoot(self, shotnumber, accuracy):
        if self.shot_cooldown > 0:
            return
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        
        for i in range(shotnumber):
            _shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            velocity = pygame.Vector2(0,1)
            accuracyrotation = 100 - accuracy
            rotatedvelocity = velocity.rotate(self.rotation + (random.randrange(- accuracyrotation, accuracyrotation)))
            rotatedspeed = rotatedvelocity * PLAYER_SHOOT_SPEED
            _shot.velocity = rotatedspeed
   