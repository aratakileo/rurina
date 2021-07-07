from widgets.button import DraggableButton
from prefabs.inputter import pressed
from base_node import get_surface
from widgets.progressbar import *
from prefabs.surface import blit
from shape import Circle
import pygame


class HSeekbar(HProgressBar):
    hovered = pressed = False

    def __init__(self, *args, thumb_color=pygame.Color('green'), **kwargs):
        self.thumb = DraggableButton(
            parent=self,
            color=thumb_color,
            shape=Circle(0, 0, 10),
            by_y=False,
            auto_draw=False
        )

        super().__init__(*args, **kwargs)
        self.thumb.area_shape = self.rect

    def fix_data(self):
        super().fix_data()
        if self.value_width != self.thumb.x:
            self.thumb.x = self.value_width

    def input(self, event) -> None:
        if self.enabled:
            super().input(event)

            pressed(self, _hovered=False)

            if self.pressed:
                self.thumb.x = pygame.mouse.get_pos()[0]
                self.thumb.hovered = True

            self.value_width = self.thumb.x
            self.thumb.shape.radius = int(self.rect.height / 3)
            self.thumb.y = (self.rect.height - self.rect.height / 3) / 2
            self.thumb.x = self.value_width

    def draw(self, surface: pygame.Surface = ...) -> None:
        if self.can_be_drawn:
            surface = get_surface(surface)

            divider = 3

            bg = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32)
            pygame.draw.rect(bg, self.color, (0, 0, self.rect.width, self.rect.height // 3), 0, 5)
            pygame.draw.rect(
                bg, self.progress_color, (2, 2, int(self.value_width) - 4, self.rect.height // 3 - 4), 0, 5
            )
            blit(surface, bg, (self.rx, self.thumb.ry - self.thumb.shape.radius / 2), self.ralpha, self.rscale)

            self.thumb.draw(surface)

            for node in self.nodes:
                if node.auto_draw:
                    node.draw(surface)


__all__ = [
    'HSeekbar'
]
