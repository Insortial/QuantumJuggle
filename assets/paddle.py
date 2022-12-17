import pygame

from . import globals

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x_pos=0, y_pos=0):
        super().__init__()

        self.image = pygame.Surface([globals.PADDLE_WIDTH, globals.WIDTH_UNIT])
        self.image.fill(globals.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

class QuantumPaddles:
    def __init__(self, y_pos):
        self.paddles = []
        for i in range(2**globals.NUM_QUBITS):
            self.paddles.append(Paddle(i*globals.PADDLE_WIDTH + (globals.WINDOW_WIDTH - globals.FIELD_WIDTH)/2, y_pos))
