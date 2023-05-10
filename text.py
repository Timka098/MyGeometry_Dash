import pygame
pygame.init()
#
class Text:
    def __init__(self, x, y, content, size, font, color):
        self.font = pygame.font.SysFont(font, size)
        self.text = self.font.render(content, True, color)
        self.rect = self.text.get_rect()
        self.content = content
        self.rect.x = x
        self.rect.y = y
        self.color = color
    def show(self, win):
        win.blit(self.text, self.rect)

    # оновити текст
    def update(self):
        self.text = self.font.render(self.content, True, self.color)




