import pygame
import threading
from assets.circuit_grid import CircuitGrid
from assets import globals, ui, paddle, ball, computer

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('myGame')
clock = pygame.time.Clock()


def main():
    #Init Game
    lives = 3
    circuit_grid = CircuitGrid(5, globals.FIELD_HEIGHT)
    quantumPaddle = paddle.QuantumPaddles(globals.FIELD_HEIGHT - globals.WIDTH_UNIT * 3.45)
    quantumComputer = computer.QuantumComputer(quantumPaddle, circuit_grid)
    pongBall =  ball.Ball()
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(quantumPaddle.paddles)
    moving_sprites.add(pongBall)

    exit = False
    while not exit:
        #Update Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)

        pongBall.update(lives)
        quantumComputer.update(pongBall)

        #Draw Game
        screen.fill(globals.BLACK)
        ui.draw_statevector_grid(screen)
        ui.draw_score(screen, lives)
        moving_sprites.draw(screen)
        circuit_grid.draw(screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == '__main__':
    main()