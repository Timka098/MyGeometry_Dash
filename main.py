
from settings import *
from text import Text
from TextAndButton import*
import pygame
pygame.init()

win = pygame.display.set_mode(WIN_SIZE, pygame.FULLSCREEN)
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()
scene = 'reg_log_menu'

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
            if log_text.rect.collidepoint(mouse_x, mouse_y) and scene == 'reg_log_menu':
                scene = 'log'
            if back_text.rect.collidepoint(mouse_x, mouse_y) and (scene == 'reg' or scene == 'log'):
                scene = 'reg_log_menu'
    if scene == 'reg_log_menu':
        reg_text.show(win)
        log_text.show(win)
        game_name.show(win)
    
    if scene == 'reg':
        reg_title.show(win)
        back_text.show(win)
    if scene == 'log':
        back_text.show(win)
        log_title.show(win)