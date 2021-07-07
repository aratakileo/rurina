import pygame
import shape


screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)

circle = shape.Circle(radius=10)
rect = shape.Rect((300, 300), (100, 100))


while True:
    circle.position = pygame.mouse.get_pos()
    circle.position = rect.accommodate_point(circle.position, True)

    screen.fill((255, 255, 255))

    shape.draw(rect)
    shape.draw(circle, color=(20, 20, 200))

    pygame.event.get()
    pygame.display.flip()
