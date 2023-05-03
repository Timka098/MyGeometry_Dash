from text import *
from settings import*
import pygame

if LANGUAGE == 'english':
    l_eng = ['REGISTRATION',
            'LOGIN',
            'BACK TO MENU',
            ]
if LANGUAGE == 'ukraine':
    l_eng = ['РЕГІСТРАЦІЯ',
                'УВІЙТИ',
                'ДО МЕНЮ',
            ]
reg_text = Text(10, 10, l_eng[0], 48, MAIN_FONT, MAIN_TEXT_COLOR)
log_text = Text(10, 50, l_eng[1], 48, MAIN_FONT, MAIN_TEXT_COLOR)
back_text = Text(10, 800, l_eng[2], 48, MAIN_FONT, MAIN_TEXT_COLOR)