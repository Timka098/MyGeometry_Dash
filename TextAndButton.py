import pygame
from text import Text
from settings import *

try:
    if LANGUAGE == 'english':
        words = ['REGISTRATION',
                 'LOGIN',
                 'BACK TO MENU',
                 'GAME NAME',
                 'REGISTER AN ACCOUNT',
                 'LOGIN AN ACCOUNT'
                ]
    elif LANGUAGE == 'ukraine':
        words = ['РЕГІСТРАЦІЯ',
                 'УВІЙТИ',
                 'ДО МЕНЮ',
                 'ІМ\'Я ГРИ',
                 'ЗАРЕЄСТРУВАТИСЬ',
                 'УВІЙТИ В АККАУНТ'
                ]
    elif LANGUAGE == 'french':
        words = ['INSCRIPTION',
                 'CONNEXION',
                 'RETOUR AU MENU',
                 'NOM DU JEU',
                 'CRÉER UN COMPTE',
                 'SE CONNECTER AU COMPTE'
                ]
    elif LANGUAGE == 'german':
        words = ['REGISTRIERUNG',
                 'ANMELDUNG',
                 'ZURÜCK ZUM MENÜ',
                 'SPIELNAME',
                 'KONTO REGISTRIEREN',
                 'KONTO ANMELDEN'
                ]
    elif LANGUAGE == 'spanish':
        words = ['REGISTRO',
                 'INICIAR SESIÓN',
                 'VOLVER AL MENÚ',
                 'NOMBRE DEL JUEGO',
                 'REGISTRAR UNA CUENTA',
                 'INICIAR SESIÓN EN UNA CUENTA'
                ]
    elif LANGUAGE == 'italian':
        words = ['REGISTRAZIONE',
                 'ACCESSO',
                 'TORNA AL MENU',
                 'NOME DEL GIOCO',
                 'REGISTRA UN ACCOUNT',
                 'ACCEDI A UN ACCOUNT'
                ]
    elif LANGUAGE == 'portuguese':
        words = ['REGISTRO',
                 'LOGIN',
                 'VOLTAR AO MENU',
                 'NOME DO JOGO',
                 'REGISTRE UMA CONTA',
                 'FAÇA LOGIN EM UMA CONTA'
                ]
    elif LANGUAGE == 'polish':
        words = ['REJESTRACJA',
                 'LOGOWANIE',
                 'POWRÓT DO MENU',
                 'NAZWA GRY',
                 'ZAREJESTRUJ KONTO',
                 'ZALOGUJ SIĘ NA KONTO'
                ]
    elif LANGUAGE == 'bulgarian':
        words = ['РЕГИСТРАЦИЯ',
                 'ВХОД',
                 'ОБРАТНО КЪМ МЕНЮТО',
                 'ИМЕ НА ИГРАТА',
                 'РЕГИСТРИРАЙТЕ СИ ПРОФИЛ',
                 'ВХОД В ПРОФИЛ'
                ]
    else:
        raise ValueError(f'Unsupported language: {LANGUAGE}')
    
    reg_text = Text(10, 10, words[0], 24, MAIN_FONT, MAIN_TEXT_COLOR)
    log_text = Text(10, 30, words[1], 24, MAIN_FONT, MAIN_TEXT_COLOR)
    back_text = Text(10, 800, words[2], 48, MAIN_FONT, MAIN_TEXT_COLOR)
    game_name = Text(10, 70, words[3], 140, MAIN_FONT, MAIN_TEXT_COLOR)
    reg_title = Text(10, 70, words[4], 140, MAIN_FONT, MAIN_TEXT_COLOR)
    log_title = Text(10, 70, words[5], 140, MAIN_FONT, MAIN_TEXT_COLOR)

except NameError:
    print("LANGUAGE variable is not defined. Please check your settings.py file.")


