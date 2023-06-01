import pygame, os
# создаєм клас звуків
class Sound:
    
    def __init__(self, path, volume=1):
        self.ABSOLUTE_PATH = os.path.join(os.path.abspath(__file__ +'/..'), path)
        self.SOUND = pygame.mixer.Sound(self.ABSOLUTE_PATH)
        self.SOUND.set_volume(volume)
    
    def play(self, start=0):
        self.SOUND.play(0, start, 0)
