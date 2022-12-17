import pygame
import threading
from assets.circuit_grid import CircuitGrid
from assets import globals, ui, paddle, ball, computer, scene

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('quantumJuggle')
clock = pygame.time.Clock()

def main():
    sceneManager = scene.SceneManager()
    sceneManager.push(scene.GameScene())

    while not sceneManager.exit:
        sceneManager.update()
        sceneManager.draw(screen)
        clock.tick(60)

if __name__ == '__main__':
    main()