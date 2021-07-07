import pygame
from font import Font
import text

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
# ln1 = shape.Line(200, 200, 400, 300)
# rect = shape.Rect(500, 500, 300, 300)
# circle = shape.Circle(0, 0, 50)
# circle2 = shape.Circle(50, 50, 50)
#
# while True:
#     screen.fill((255, 255, 255))
#     flip()
#     for e in get():
#         if 'quit' in e:
#             exit()
#
#         if 'drop file' in e:
#             if messagebox.askyesno('Переместить файл?', 'Ты точно хочешь переместить файл?') == messagebox.VALUE_YES:
#                 print(f'Перемещён файл: \'{e.file}\'')
#             else:
#                 print('Файл не был перемещён')
#
#     if pygame.mouse.get_pressed()[0]:
#         rect.center = pygame.mouse.get_pos()
#
#     if pygame.mouse.get_pressed()[1]:
#         circle.center = pygame.mouse.get_pos()
#
#     if pygame.mouse.get_pressed()[2]:
#         ln1.center = pygame.mouse.get_pos()
#
#     if ln1.collide(rect) or ln1.collide(circle) or rect.collide(circle) or circle.collide(circle2):
#         color = (240, 40, 40)
#     else:
#         color = (40, 240, 40)
#
#     shape.draw(rect, color)
#     shape.draw(ln1, color, antialiased=True)
#     shape.draw(circle, color)
#     shape.draw(circle2, color)
#
#     pygame.display.flip()

# pygame.font.init()
rect = [0, 0, 170, 200]
f = Font(None, 60)
height = f.height
txt = 'Дорогой дневник. Мне не описать словами, что я испытал!\n\nЗапись от хх.хх.20хх'


while True:
    screen.fill((0, 0, 0))
    for _ in pygame.event.get():
        if _.type == pygame.QUIT:
            exit()

    if pygame.mouse.get_pressed()[0]:
        rect[2] = pygame.mouse.get_pos()[0]
        # rect[3] = len(text.lines(txt, f, rect)) * f.get_height()

    pygame.draw.rect(screen, (0, 200, 50), rect)

    lines = text.lines(txt, f, rect)
    positions = text.lines_gravity(lines, f, rect, 1 | 2 | 8 | 4, 0)
    i = -1
    for pos in positions:
        i += 1
        text.write(lines[i].strip(' '), f, pos)

    pygame.display.flip()
