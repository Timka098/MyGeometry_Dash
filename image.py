import pygame, utils
pygame.init()
class Image:
    def __init__(self, path, x, y, width, height):
        self.x, self.y = x, y
        self.path = utils.abspath(path)
        self.image = pygame.image.load(self.path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.width = width
        self.height = height
    
    def show(self, win):
        win.blit(self.image, (self.x, self.y))