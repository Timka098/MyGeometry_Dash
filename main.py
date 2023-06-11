from db import *
from settings import *
from text import Text
from TextAndButton import*
from image import*
from sprite import*
import pygame, utils, sqlite3

pygame.init()

win = pygame.display.set_mode(WIN_SIZE)

from levels import*

pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()
scene = 'game_lvl'
selected_input_field = None
cube = Sprite("images/cube.png", 'sounds/jump.ogg', 500, 400, WIN_SIZE[1]//podilyty, WIN_SIZE[1]//podilyty, 5)
number_error = None
create_db()
coin_counter = Text(10, 10, 'coin counter ', 24, MAIN_FONT, MAIN_TEXT_COLOR)
bg = Image('images/bg.png', 0, 0, WIN_SIZE[0], WIN_SIZE[1])

while True:
    pygame.display.flip()
    clock.tick(FPS)
    win.fill(BG_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            need_show_error = False
            # якщо ми в рівні і можемо стрибати
            if scene == 'game_lvl' and cube.can_jump == True:
                # тоді ми стрибаємо
                cube.is_jumping = True
                cube.jump_sound.play()


            mouse_x, mouse_y = event.pos
            if scene == 'reg' or 'log':
                # виділина кнопка
                selected_input_field = None
                #перебираєм список з кнопками
                for input_field in input_field_list:
                    # по займончуванем виділеної кнопки нема
                    input_field.border_width = None
                    #якщо ми натиснули на кнопку
                    if input_field.rect.collidepoint(mouse_x, mouse_y):
                        input_field.text.content = ''
                        #розмір виділення збільшити
                        input_field.border_width = 5
                        #кнопка на яку ми нажали = input_field
                        selected_input_field = input_field
                    
            if reg_text.rect.collidepoint(mouse_x, mouse_y) and scene == 'reg_log_menu':
                scene = 'reg'
            if log_text.rect.collidepoint(mouse_x, mouse_y) and scene == 'reg_log_menu':
                scene = 'log'
            if back_text.rect.collidepoint(mouse_x, mouse_y) and (scene == 'reg' or scene == 'log'):
                number_error = None
                scene = 'reg_log_menu'
            if reg_button.rect.collidepoint(mouse_x, mouse_y) and scene == 'reg':
                # conn = sqlite3.connect(utils.abspath('data_base.db'))
                
                # cur = conn.cursor()
                # cur.execute("SELECT user_name FROM user")
                # rows = cur.fetchall()


                # for row in rows:
                #     if row == input_field_list[0].text.content:
                #         need_show_error == True
                        
                #     else:
                if input_field_list[0].text.content != '' and input_field_list[1].text.content != '':
                    user_name = input_field_list[0].text.content
                    conn = sqlite3.connect(utils.abspath('data_base.db'))
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM user WHERE user_name = ?", (user_name,))

                    if cur.fetchone() == None:
                        create_user(input_field_list[0].text.content, input_field_list[1].text.content)
                        number_error = 10
                        
                    else:
                        number_error = 11
                    
                else:
                    number_error = 9
                

            if log_button.rect.collidepoint(mouse_x, mouse_y) and scene == 'log':
                if input_field_list[0].text.content != '' and input_field_list[1].text.content != '':

                    if user_login(input_field_list[0].text.content, input_field_list[1].text.content, win) == False:
                        number_error = 8

                    else:
                        scene = 'game_lvl'

                    
            
            # else:
            #     if selected_input_field != None:
                else:
                    number_error = 9

        
        if event.type == pygame.KEYDOWN:
            if scene == 'reg' or 'log':
                #!
                if selected_input_field != None:
                    # додати текст
                    if len(selected_input_field.text.content) < 20:
                        selected_input_field.text.content += event.unicode
                    if event.key == pygame.K_BACKSPACE:
                        selected_input_field.text.content = selected_input_field.text.content[:-2]
                    # оновити текст
                    selected_input_field.text.update()
    # if user_login(input_field_list[0].text.content, input_field_list[1].text.content, win) == False and selected_input_field != None:
    #     utils.show_error(words[8], 2, win)
    if number_error != None:
        utils.show_error(words[number_error], win)
        
    if scene == 'reg_log_menu':
        reg_text.show(win)
        log_text.show(win)
        game_name.show(win)
    
    if scene == 'reg':
        for input_field in input_field_list:
            input_field.show(win)
        reg_title.show(win)
        back_text.show(win)
        reg_button.show(win)
        
    if scene == 'log':
        log_button.show(win)
        for input_field in input_field_list:
            input_field.show(win)
        back_text.show(win)
        log_title.show(win)
    
    if scene == 'game_lvl':
        bg.show(win)
        for i in lvl_obj:
            i.show(win)
            i.x -= 5
        
        cube.collision(lvl_obj)
        cube.jump(WIN_SIZE[1], podilyty)

        # cube.collide_coin(coin)
        cube.show(win)

        coin_counter.show(win)