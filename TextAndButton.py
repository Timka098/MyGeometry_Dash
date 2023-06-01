import pygame
from text import Text
from settings import *
from box import Box
from InputField import InputField

try:
    if LANGUAGE == 'english':
        words = ['registration',
                'login',
                'back to menu',
                'game name',
                'register an account',
                'login an account',
                'name',
                'password',
                 "error, incorrect name or password.",
                ]
    elif LANGUAGE == 'ukraine':
        words = ['РЕГІСТРАЦІЯ',
                 'УВІЙТИ',
                 'ДО МЕНЮ',
                 'ІМ\'Я ГРИ',
                 'ЗАРЕЄСТРУВАТИСЬ',
                 'УВІЙТИ В АККАУНТ',
                 'ІМ\'Я',
                 'ПАРОЛЬ',
                 ]

    else:
        raise ValueError(f'Unsupported language: {LANGUAGE}')
    
    reg_text = Text(10, 10, words[0], 24, MAIN_FONT, MAIN_TEXT_COLOR)
    log_text = Text(10, 30, words[1], 24, MAIN_FONT, MAIN_TEXT_COLOR)
    back_text = Text(10, 800, words[2], 48, MAIN_FONT, MAIN_TEXT_COLOR)
    game_name = Text(10, 70, words[3], 140, MAIN_FONT, MAIN_TEXT_COLOR)
    reg_title = Text(10, 70, words[4], 140, MAIN_FONT, MAIN_TEXT_COLOR)
    log_title = Text(10, 70, words[5], 140, MAIN_FONT, MAIN_TEXT_COLOR)
    log_button = Text(10, 320, words[1], 48, MAIN_FONT, MAIN_TEXT_COLOR)
    reg_button = Text(10, 320, words[0], 48, MAIN_FONT, MAIN_TEXT_COLOR)
    input_field_list = [InputField(10, 200, 500, 50, MAIN_TEXT_COLOR, None, (0,0,0),
                           words[6], 48, MAIN_FONT, INPUT_MAIN_TEXT_COLOR),
                        InputField(10, 260, 500, 50, MAIN_TEXT_COLOR, None, (0,0,0),
                           words[7], 48, MAIN_FONT, INPUT_MAIN_TEXT_COLOR)
                           ]

except NameError:
    print("LANGUAGE variable is not defined. Please check your settings.py file.")


