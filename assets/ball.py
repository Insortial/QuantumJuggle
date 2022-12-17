import random

import pygame

from . import globals

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([globals.WIDTH_UNIT, globals.WIDTH_UNIT])
        self.image.fill(globals.WHITE)
        self.rect = self.image.get_rect()
        self.velocity = [1,2]
        self.initial_speed = 2
        self.bounced = False
        self.acceleration = .5
        self.reset(direction=1)

    def update(self, lives):
        self.rect.x += self.velocity[0] + self.acceleration
        self.rect.y += self.velocity[1] + self.acceleration

        if self.bounced == True and self.rect.y <= 200:
            self.velocity[1] = -self.velocity[1] * .75

        if self.rect.y > globals.FIELD_HEIGHT - globals.WIDTH_UNIT:
            lives -= 1
            self.reset(direction=1)
        
        if self.rect.x <= (globals.WINDOW_WIDTH - globals.FIELD_WIDTH)/2:
            self.velocity[0] = .2
        elif self.rect.x >= (globals.WINDOW_WIDTH - globals.FIELD_WIDTH)/2 + 700:
            self.velocity[0] = -.2

    def bounce(self):
        # ball is sped up 50% after each bounce
        self.velocity[0] = -self.velocity[0] * 1.15
        self.velocity[1] = -self.velocity[1] * 1.15      

    def reset(self, direction):
        self.rect.centerx = globals.WINDOW_WIDTH / 2
        self.rect.centery = 20
        self.bounced = False

        if direction > 0:
            self.velocity = [0, 3] * self.initial_speed
        else:
            self.velocity = [0, 3] * self.initial_speed