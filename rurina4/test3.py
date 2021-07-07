import shape
from event import flip, get
import pygame

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
rect = shape.Rect(0, 0, 400, 200)


while True:
    screen.fill((255, 255, 255))
    flip()

    shape.gradient(rect, [(120, 120, 120), (0, 0, 0), (200, 40, 40), (255, 255, 255), (40, 200, 40)])
    shape.draw(shape.Triangle())

    pygame.display.flip()
