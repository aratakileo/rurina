from input import *
import pygame

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)


# set('ui_copy', ['key down ctrl', 'key down c'], ['key up ctrl', 'key up c'])
setkey('ui_copy', 'ctrl+c')
setkey('ui_mouse', 'mouse+arrow')


while True:
    screen.fill((255, 255, 255))

    flip()

    # print(actionstatus('ui_copy'))
    # print('is_action_pressed', is_action_pressed('ui_copy'))
    # print('is_action_released', is_action_released('ui_copy'))
    # print('is_action_just_pressed', is_action_just_pressed('ui_copy'))

    # if is_action_just_pressed('ui_copy'):
    #     exit()

    # print(is_action_pressed('ui_copy'), is_action_just_long_pressed('ui_copy', '1'))
    print(keystatus('ui_mouse', 'mouse+arrow'))

    for e in pygame.event.get():
        pass
        # print(e)

    pygame.display.flip()
