import pygame
from text import Text
from settings import *
from box import Box
from InputField import InputField

#16
try:
    # тексти (поміняти мову можно в settings.py)
    if LANGUAGE == 'english':
        words = ['registration',
                'login',
                'back to menu',
                'MyGeometryDash',
                'register an account',
                'login an account',
                '',
                '',
                 "error, incorrect name or password.",
                 'please fill the field',
                 'successful registration',
                 'the name is already in the database',
                 'coins: ',
                 'level completed',
                 'play',
                 'P.S. there are settings in the game, you need to change what you need in settings.py'
                ]
    elif LANGUAGE == 'ukraine':
        words = ["реєстрація",
             "вхід",
             "назад до меню",
             "Мій Geometry Dash",
             "зареєструвати акаунт",
             "увійти в акаунт",
             "",
             "",
             "помилка, невірне ім'я або пароль.",
             "будь ласка, заповніть поле",
             "успішна реєстрація",
             "таке ім'я вже є в базі даних",
             "монети: ",
             "рівень пройдено",
             "грати",
             "P.S. в грі є налаштування, потрібно в settings.py змінити те що вам потрібно"
            ]

    else:
        raise ValueError(f'Unsupported language: {LANGUAGE}')
    
    # самі тексти (цей модуль я писав)
    reg_text = Text(10, 0, words[0], 24, MAIN_FONT, MAIN_TEXT_COLOR)
    log_text = Text(10, 20, words[1], 24, MAIN_FONT, MAIN_TEXT_COLOR)
    back_text = Text(10, 800, words[2], 48, MAIN_FONT, MAIN_TEXT_COLOR)
    game_name = Text(10, 50, words[3], 140, MAIN_FONT, MAIN_TEXT_COLOR)
    reg_title = Text(10, 70, words[4], 140, MAIN_FONT, MAIN_TEXT_COLOR)
    log_title = Text(10, 70, words[5], 140, MAIN_FONT, MAIN_TEXT_COLOR)
    log_button = Text(10, 320, words[1], 48, MAIN_FONT, MAIN_TEXT_COLOR)
    reg_button = Text(10, 320, words[0], 48, MAIN_FONT, MAIN_TEXT_COLOR)
    input_field_list = [InputField(10, 200, 500, 50, MAIN_TEXT_COLOR, None, MAIN_TEXT_COLOR,
                           words[6], 48, MAIN_FONT, INPUT_MAIN_TEXT_COLOR),
                        InputField(10, 260, 500, 50, MAIN_TEXT_COLOR, None, MAIN_TEXT_COLOR,
                           words[7], 48, MAIN_FONT, INPUT_MAIN_TEXT_COLOR)
                           ]
    completed_lvl_text = Text(450, 10, words[13], 124, MAIN_FONT, MAIN_TEXT_COLOR)
    play_text = Text(10, 200, words[14], 48, MAIN_FONT, MAIN_TEXT_COLOR)
    about_settings_text = Text(10, 800, words[15], 24, MAIN_FONT, MAIN_TEXT_COLOR)

# якщо ви не правильно введете мову, вам напишуть помилку
except NameError:
    print("LANGUAGE variable is not defined. Please check your settings.py file.")


