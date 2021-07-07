from prefabs.inputter import _input as _input2
from widgets.text import *
from widgets.button import *
from camera import Camera
from main_nodes import _input, draw
from shape import *
from prefabs.rmath import move_negativity
from widgets.progressbar import *
from widgets.text import *
from widgets.seekbar import *
import pygame

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.init()

font = pygame.font.SysFont('Robot', 30)

camera = Camera()
camera.scalex = -1.0

btn1 = Button(font, 'btn1', gravity=4 | 8)
btn2 = Text(font, 'text', gravity=4 | 8)

texture = pygame.Surface((1, 1))
texture.fill(pygame.Color('red'))
btn2.sprite.texture = texture
btn2.sprite.region_enabled = True

btn3 = DraggableButton(pos=(400, 400))
# btn3.area_shape = Rect(200, 200, 400, 400)
btn3.area_shape = Circle(400, 400, 100)
# btn1.disable()
# btn2.disable()

pb = HProgressBar(rect=Rect(0, 0, 200, 50))
pb.absolute_value = 15

sb = HSeekbar(rect=Rect(0, 0, 200, 50), step=0.01)
pb.max_value = sb.max_value = 1000000
pb.step = sb.step = 0

pbt = Text(font=font, rect=pb.rect, gravity=4 | 8, parent=pb)

while True:
    bw, bh = pygame.display.get_window_size()
    bh //= 15

    if bh < 35:
        bh = 35

    bw -= 16
    btn1.x = btn2.x = pb.x = sb.x = 8

    btn1.rect.size = btn2.rect.size = pb.rect.size = sb.rect.size = bw, bh
    btn2.sprite.reimport_texture()
    btn1.y = 5
    btn2.y = bh + btn1.y + 5
    pb.y = btn2.y + bh + 5
    sb.y = bh + pb.y + 5

    pb.absolute_value = sb.absolute_value

    pbt.value = f'{pb.percent_value}%'
    btn2.value = f'Progress: {pb.absolute_value}/{pb.min_to_max_value_difference}'

    screen.fill((255, 255, 255))

    for e in _input(_input2(pygame.event.get())):
        if e.type == pygame.QUIT:
            exit()

    draw()

    pygame.display.flip()
