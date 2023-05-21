from settings import*
from image import*

podilyty = 10

lvl_0 = [
    'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD',
    '                                            ',
    '                                           3',
    '                                            ',
    '                                         D  ',
    '                                      D  D  ',
    '         3            33           D33D33D  ',
    'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD',
]
main_lvl = lvl_0
obj_x = 0
obj_y = 0
lvl_obj = []
for row in main_lvl:
    for symbol in row:
        if symbol == 'D':
            lvl_obj.append(Image('images/block.png', obj_x, obj_y, WIN_SIZE[1]//podilyty, WIN_SIZE[1]//podilyty))
        elif symbol == '3':
            lvl_obj.append(Image('images/spike.png', obj_x, obj_y, WIN_SIZE[1]//podilyty, WIN_SIZE[1]//podilyty))
        # elif symbol == ' ':
            
        
        
        obj_x += WIN_SIZE[1]//podilyty

    obj_y += WIN_SIZE[1]//podilyty
    obj_x = 0
        