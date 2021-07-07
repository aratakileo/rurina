from input import flip
from utilities.surface import *
import utilities.time as time
from nodes import Control, init
from shape import draw
import pygame
import pygame.key as key
from event import get, typename2
from input import map


screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
_mask = AlphaSurface((100, 100))
_gradient = gradient((0, 0, 100, 100), [(200, 20, 20), (20, 200, 20), (20, 20, 200)], surface=pygame.Surface((100, 100)), offset=1)
pygame.draw.circle(_mask, (40, 240, 40), (50, 50), 50)
_gradient = mask(_gradient, _mask)
init()
control = Control()
control.focused_cursor = 2


print(pygame.BUTTON_LEFT, pygame.BUTTON_MIDDLE, pygame.BUTTON_RIGHT)


while True:
    screen.fill((255, 255, 255))

    flip()
    time.flip()
    pygame.display.get_surface().blit(_gradient, (0, 0))
    draw(control.rect)
    control.input(get(False))

    # for e in get(False):
    #     print(typename2(e))

    # if control.pressed:
    #     print('actions:', map._actions)
    #     print('events:', get(False))
    #
    #     for e in get(False):
    #         if e.type == pygame.MOUSEBUTTONUP:
    #             if e.button == pygame.BUTTON_LEFT:
    #                 exit()

    pygame.event.get()
    pygame.display.flip()
    # print(time.dt)
    # print(time.fps)
