import pygame
from settings import*
from text import Text
#from TextAndButton import*
from box import Box

#клас
class InputField(Box):
    def __init__(self, x, y, width, height, color, border_width, border_color,
                 content, text_size, text_font, text_color):
        
        super().__init__(x, y, width, height, color, border_width, border_color)
        self.text = Text(self.rect.x+10, self.rect.y+1, content, text_size, text_font, text_color)

    def show(self, win):
        super().show(win)
        self.text.show(win)