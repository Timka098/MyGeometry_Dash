import pygame

class Box:
    def __init__(self, x, y, width, height, color, border_width, border_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.border_width = border_width
        self.border_color = border_color
    
    def show(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        if self.border_width != None:
            pygame.draw.rect(win, self.border_color, self.rect, self.border_width)
        
