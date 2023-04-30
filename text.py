import pygame
pygame.init()

class Text:
    def __init__(self, x, y, content, size, font, color):
        self.font = pygame.font.SysFont(font, size)
        self.text = self.font.render(content, True, color)
        self.rect = self.text.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self, win):
        win.blit(self.text, self.rect)






