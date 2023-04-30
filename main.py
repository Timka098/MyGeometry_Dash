import pygame
from settings import *
from text import Text
pygame.init()

win = pygame.display.set_mode(WIN_SIZE, pygame.FULLSCREEN)
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()
scene = 'reg_log_menu'
reg_text = Text(10, 360, 'REGISTRATION', 48, MAIN_FONT, MAIN_TEXT_COLOR)

while True:
    pygame.display.flip()
    clock.tick(FPS)
    win.fill(BG_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if reg_text.rect.collidepoint(mouse_x, mouse_y) and scene == 'reg_log_menu':
                scene = 'reg'

    if scene == 'reg_log_menu':
        reg_text.show(win)
    