import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity*dt
    def split(self):
        velocity = self.velocity
        x = self.position[0]
        y = self.position[1]
        radius = self.radius
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        asteroid1 = Asteroid(x, y, radius-ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(x, y, radius-ASTEROID_MIN_RADIUS)
        split_direction = random.uniform(20, 50)
        
        asteroid1.velocity = 1.2*velocity.rotate(split_direction)
        asteroid2.velocity = 1.2*velocity.rotate(-1*split_direction)
