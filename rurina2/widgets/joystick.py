from widgets.button import DraggableButton
from widgets.widget import WidgetByShape
from prefabs.rmath import distance
from base_node import get_surface
from prefabs.surface import blit
from prefabs.inputter import *
from shape import *
import pygame


class Joystick(WidgetByShape):
    pressed: bool = False

    def __init__(self, *args, color=(0, 0, 0), thumb_color=pygame.Color('green'), **kwargs):
        super().__init__(*args, color=color, **kwargs)
        self.thumb = DraggableButton(
            parent=self,
            color=thumb_color,
            shape=Circle(0, 0, 10),
            auto_draw=False,
            area_shape=self.shape
        )

    def input(self, event) -> None:
        if self.enabled:
            super().input(event)

            pressed(self, _hovered=False)

            size = Rect(0, 0, *get_size(self.shape))
            set_size(self.thumb.shape, size.width // 2, size.height // 2)
            self.thumb.area_shape.pos = (size.width / 2, size.height / 2)

            if self.pressed:
                self.thumb.pos = pygame.mouse.get_pos()
                self.thumb.hovered = True
            elif not self.thumb.pressed:
                self.thumb.pos = size.width / 2, size.height / 2

    def draw(self, surface: pygame.Surface = ...) -> None:
        if self.can_be_drawn:
            surface = get_surface(surface)

            size = Rect(0, 0, *get_size(self.shape))

            bg = pygame.Surface(size.size, pygame.SRCALPHA, 32)
            pygame.draw.circle(bg, self.color, (size.width / 2, size.height / 2), size.width // 2)
            blit(surface, bg, self.rpos, self.ralpha, self.rscale)

            self.thumb.draw(surface)

            for node in self.nodes:
                if node.auto_draw:
                    node.draw(surface)


__all__ = [
    'Joystick'
]
