from constants import GRAVITY_RIGHT, GRAVITY_BOTTOM, GRAVITY_CENTER_VERTICAL, GRAVITY_CENTER_HORIZONTAL
from main_nodes import _input, draw, CollisionShape
from prefabs.inputter import _input as _input2
from prefabs.size_fixer import *
from widgets.progressbar import *
from widgets.joystick import *
from widgets.seekbar import *
from widgets.button import *
from widgets.text import *
from camera import Camera
from shape import *
import pygame

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.init()

font = pygame.font.SysFont('Robot', 30)

camera = Camera()

container = CollisionShape(shape=Rect(0, 0, 100, 100))
button1 = Button(font=font, value='Заполнить прогресс', gravity=GRAVITY_CENTER_HORIZONTAL | GRAVITY_CENTER_VERTICAL)
button2 = Button(font=font, value='Очистить прогресс', gravity=GRAVITY_CENTER_HORIZONTAL | GRAVITY_CENTER_VERTICAL, color=pygame.Color('red'))
progressbar1 = HProgressBar()
progressbar1_text = Text(font, gravity=GRAVITY_CENTER_HORIZONTAL | GRAVITY_CENTER_VERTICAL, rect=progressbar1.rect)
seekbar1 = HSeekbar()
text1 = Text(font, text_color=pygame.Color('purple'), gravity=GRAVITY_CENTER_HORIZONTAL | GRAVITY_CENTER_VERTICAL)
joystick1 = Joystick(shape=Circle(0, 0, 100))
joystick1.rpos = 40, 40
views = [button1, button2, progressbar1, seekbar1, text1]
off = 3

while True:
    container.shape.size = pygame.display.get_window_size()
    screen.fill((255, 255, 255))

    for e in _input(_input2(pygame.event.get())):
        if e.type == pygame.QUIT:
            exit()

    for view in views:
        fix_size(view, container, (1, 15), (150, 45))
        set_margin(view, view, (off, off, off, off))

    accommodate_by_vertical(views, container, off)

    if button1.released:
        seekbar1.percent_value = 100

    if button2.released:
        seekbar1.percent_value = 0

    progressbar1.absolute_value = seekbar1.absolute_value

    progressbar1_text.rpos = progressbar1.rpos
    progressbar1_text.value = f'{progressbar1.percent_value}%'
    text1.value = f'Прогресс: {progressbar1.absolute_value}/{progressbar1.min_to_max_value_difference}'

    draw()

    pygame.display.flip()
