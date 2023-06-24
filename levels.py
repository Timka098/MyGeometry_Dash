from settings import*
from image import*

# маштаб (міняти в коли ви поміняли розширення екрана)
podilyty = 10


# поки в нас тільки 0 рівень для тесту
lvl_0 = [
    '',
    '',
    'DDDDDDDDDDDD',
    '                      ',
    '                      ',
    '                DD        ',
    '           ccDDDD DDDD33         33  f',
    'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD',
]
# рівень
game_lvl = lvl_0


# саме створеня рівня
lvl_obj = []
def make_lvl(game_lvl, lvl_obj):
    obj_x = 0
    obj_y = 0
    for row in game_lvl:
        for symbol in row:
            if symbol == 'D':
                lvl_obj.append(Image('images/block.png', obj_x, obj_y, WIN_SIZE[1]//podilyty, WIN_SIZE[1]//podilyty))
            elif symbol == '3':
                lvl_obj.append(Image('images/spike.png', obj_x, obj_y, WIN_SIZE[1]//podilyty, WIN_SIZE[1]//podilyty))
            elif symbol == 'c':
                lvl_obj.append(Image('images/coin.png', obj_x, obj_y, WIN_SIZE[1]//podilyty, WIN_SIZE[1]//podilyty))
            elif symbol == 'f':
                lvl_obj.append(Image('images/finish.png', obj_x, obj_y, 10, 10))
            
            obj_x += WIN_SIZE[1]//podilyty

        obj_y += WIN_SIZE[1]//podilyty
        obj_x = 0

make_lvl(game_lvl, lvl_obj)