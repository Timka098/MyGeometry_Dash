import pygame, os, time
from InputField import*
from settings import*

# повний шлях 
def abspath(path):
    return os.path.join(os.path.abspath(__file__ + '/..'), path)

def show_error(text_content, seconds, win):
    field = InputField(0, 0, WIN_SIZE[0]-10, 50,
                       INPUT_MAIN_TEXT_COLOR, 10, MAIN_TEXT_COLOR,
                       text_content, 24, MAIN_FONT, MAIN_TEXT_COLOR)
    field.show(win)
    
    