import pygame
from assets.circuit_grid import CircuitGrid
from assets import globals, ui, paddle

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('myGame')
clock = pygame.time.Clock()

def main():
    #Init Game
    circuit_grid = CircuitGrid(5, globals.FIELD_HEIGHT)
    quantumPaddle = paddle.QuantumPaddles(globals.FIELD_HEIGHT - globals.WIDTH_UNIT * 2)
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(quantumPaddle.paddles)

    exit = False
    while not exit:
        #Update Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)

        #Draw Game
        ui.draw_statevector_grid(screen)
        ui.draw_score(screen, 3)
        moving_sprites.draw(screen)
        circuit_grid.draw(screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == '__main__':
    main()