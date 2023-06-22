from settings import*
from image import*

podilyty = 10

lvl_0 = [
    'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD                        D                                                                                                              ',
    '                                                                    D                          DD   D    D     DD                                                                  ',
    '                                                                    D                         D     D    D    D                                                                    ',
    '         33333333333333                                                        D                         DD      DD      DD                                                                                              ',
    '                                                                                                                                                                                                                             ',
    'D                              ccccccccccccccccc                              f                                                                                                                   ccccccccccccccccccc        D'                                                                                                 ,
    'D                          cDDDDDDDDDD                                      D      D      D     D      D       c      D                                                                         f                         ',
    'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD',
]
game_lvl = lvl_0

#left_block_lvl = None


lvl_obj = []
def make_lvl(game_lvl, lvl_obj):
    obj_x = 0
    obj_y = 0
    for row in game_lvl:
        for symbol in row:
            if symbol == 'D':
                lvl_obj.append(Image('images/block.png', obj_x, obj_y, WIN_SIZE[1]//podilyty, WIN_SIZE[1]//podilyty))
                # if left_block_lvl == None:
                #     left_block_lvl = lvl_obj[-1]
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