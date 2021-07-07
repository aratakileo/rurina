from base_node import get_surface
from prefabs.surface import blit
from widgets.bar import Bar
import pygame


class HProgressBar(Bar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self, surface: pygame.Surface = ...) -> None:
        if self.can_be_drawn:
            surface = get_surface(surface)

            bg = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32)
            pygame.draw.rect(bg, self.color, (0, 0, *self.rect.size), 0, 5)
            pygame.draw.rect(bg, self.progress_color, (2, 2, int(self.value_width) - 4, self.rect.height - 4), 0, 5)
            blit(surface, bg, self.rpos, self.ralpha, self.rscale)

            super().draw(surface)


__all__ = [
    'HProgressBar'
]
