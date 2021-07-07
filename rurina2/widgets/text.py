from constants import STYLE_NORMAL, STYLE_BOLD, STYLE_ITALIC
from prefabs.text import write_autoline
from widgets.widget import WidgetByRect
from base_node import get_surface
from prefabs.surface import blit
from shape import Rect
import pygame


class Text(WidgetByRect):
    def __init__(
            self,
            font: pygame.font.Font,
            value: str = '',
            text_color=pygame.Color('white'),
            linespacing: int = 0,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.font = font
        self.value = value
        self.text_color = text_color
        self.linespacing = linespacing

        self.sprite.region_enabled = True

    @property
    def can_be_drawn(self):
        return self.visible and self.alpha > 0 and self.scale != 0 and len(self.value) > 0

    @property
    def style(self) -> int:
        __style = STYLE_NORMAL

        if self.font.get_bold():
            __style |= STYLE_BOLD

        if self.font.get_italic():
            __style |= STYLE_ITALIC

        return __style

    @style.setter
    def style(self, value):
        self.font.set_bold(value & STYLE_BOLD)
        self.font.set_italic(value & STYLE_ITALIC)

    def draw(self, surface: pygame.Surface = ...) -> None:
        if self.can_be_drawn:
            surface = get_surface(surface)

            self.sprite.draw(surface)

            blit(
                surface,
                write_autoline(
                    self.value,
                    self.font,
                    Rect(0, 0, *self.rect.size),
                    self.text_color,
                    self.gravity,
                    pygame.Surface(self.rect.size, pygame.SRCALPHA, 32),
                    self.linespacing
                ),
                self.rect.rpos,
                self.ralpha,
                self.rscale
            )

            super().draw(surface)


__all__ = [
    'Text'
]
