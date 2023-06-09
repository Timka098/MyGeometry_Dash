import pygame, image, sound

class Sprite(image.Image, sound.Sound):
    def __init__(self, path, sound_path, x, y, width, height, gravity_speed):
        super().__init__(path, x, y, width, height)
        self.gravity_speed = gravity_speed#
        self.width = width# ширина куба
        self.height = height# висота куба
        self.jump_counter = 0# лічильник
        self.is_jumping = False# ми нажали на стрибок?
        self.can_jump = True# ми можем стрибати?
        self.jump_sound = sound.Sound(sound_path, 0.25)# звук при стрибку
        self.coin_sound = sound.Sound('sounds/coin_sound.wav', 0.25)# звук для монет
        self.first_pos = x, y# позиція
        self.game_over = False# гра закінчилась?
        self.taken_coins = 0# взято монет
        self.game_win = False# ми вийграли?
      
    # колізія
    def collision(self, list_obj):
        # перебираєм об"єкти
        for obj in list_obj:
            # якщо знизу це блок
            if "block.png" in obj.path:
                #перевірка на торкання
                if self.x+self.width >= obj.x and self.x <= obj.x+obj.width:
                    if self.y+self.height >= obj.y and self.y+self.height <= obj.y+self.gravity_speed:
                        # ми не литимо
                        self.jump_counter = 0
                        # ми можем стрибнути
                        self.can_jump = True
                        break

                    elif self.y+self.height >= obj.y and self.y <= obj.y+obj.height:
                        self.game_over = True
                        self.taken_coins = 0
                    

            # колізія для шипа
            elif 'spike.png' in obj.path:
                offset = (obj.x-self.x, obj.y-self.y)
                is_collision = self.mask.overlap(obj.mask, offset) 
                if is_collision != None:
                    self.game_over = True
                    self.taken_coins=0

            # колізія монети
            elif 'coin.png' in obj.path:
                if self.rect.colliderect(obj.rect):
                    self.coin_sound.play()
                    # self.removed_coins.append(obj)
                    list_obj.remove(obj)
                    self.taken_coins += 1
            
            # якщо ми дійшли до фініша
            elif 'finish.png' in obj.path:
                if self.x >= obj.x:
                    self.game_win = True
            
        else:
            # ми зараз падаєм тобто не можно стрибати
            self.can_jump = False
            # саме падіння
            self.y += self.gravity_speed
    # фун. стрибка
    def jump(self, WIN_SIZE, podilyty):
        # якщо ми не падаєм
        if self.jump_counter != 40 and self.is_jumping:
            # лічильник
            self.jump_counter += 1
            # сам стрибок
            self.y -= WIN_SIZE//podilyty*2/20
            ##self.jump_sound.play()
        # якщо ми не в повітрі
        else:
            # неможна стрибати
            self.is_jumping = False

        
        