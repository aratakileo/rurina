import shape
from event import flip, get
from widget import widget
from widget import Text, EditText
import pygame
from font import Font
from input.inputmap import flip as iflip
import mouse
import utilities.time as t

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
rect = shape.Rect(0, 0, 200, 400)
text = Text(value='Дорогой друг!                 \nПриветсвую тебя на бета-тесте движкового UI!\nСпасибо за бета-тест!', rect=rect, font=Font(None, 60), selectable=True, gravity=0, max_lines=None)
edittext = EditText(rect=rect, pos=(200, 0), value='abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz')
# print(text.max_lines)
# print(text.lines)


while True:
    screen.fill((255, 255, 255))
    flip()
    iflip()
    for e in get(False):
        if 'quit' in e:
            exit()

    widget.flip()
    mouse.flip()
    t.flip()

    text.input(get(False))
    edittext.input(get())
    shape.draw(rect, (40, 240, 40))
    shape.draw(pygame.Rect(*edittext.pos, *edittext.rect.size), (40, 40, 40))
    text.draw()
    edittext.draw()

    pygame.display.flip()
