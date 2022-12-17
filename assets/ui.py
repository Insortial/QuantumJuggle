import pygame

from . import globals, resources

def draw_statevector_grid(screen):
    font = resources.Font()
    basis_states = ['|000>', '|001>', '|010>', '|011>', '|100>', '|101>', '|110>', '|111>']
    statevector_width = int(round(globals.FIELD_WIDTH / len(basis_states)))

    for i in range(len(basis_states)):
        text = font.vector_font.render(basis_states[i], 1, globals.WHITE)
        screen.blit(text, (i*statevector_width + (globals.WINDOW_WIDTH - globals.FIELD_WIDTH)/2,
                           globals.FIELD_HEIGHT - text.get_height()))

def draw_score(screen, lives):
    font = resources.Font()

    text = font.player_font.render("LIVES", 1, globals.GRAY)
    text_pos = text.get_rect(topright=(globals.WINDOW_WIDTH*0.95, globals.WIDTH_UNIT*2))
    screen.blit(text, text_pos)

    text = font.score_font.render(str(lives), 1, globals.GRAY)
    text_pos = text.get_rect(topright=(globals.WINDOW_WIDTH*0.95, globals.WIDTH_UNIT*8))
    screen.blit(text, text_pos)

def draw_dashed_line(screen):
    for i in range(10, globals.FIELD_HEIGHT, 2 * globals.WIDTH_UNIT): 
        pygame.draw.rect(
            screen,
            globals.GRAY,
            ((globals.WINDOW_WIDTH - globals.FIELD_WIDTH)/2, i, 0.5 * globals.WIDTH_UNIT, globals.WIDTH_UNIT),
            0,
        ) 

        pygame.draw.rect(
            screen,
            globals.GRAY,
            ((globals.WINDOW_WIDTH - globals.FIELD_WIDTH)/2 + 700, i, 0.5 * globals.WIDTH_UNIT, globals.WIDTH_UNIT),
            0,
        ) 
