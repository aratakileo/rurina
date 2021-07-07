from widgets.widget import _Widget, WidgetByShape
from prefabs.rmath import move_negativity
import prefabs.animator as animator
from base_node import get_surface
from prefabs.surface import blit
from prefabs.inputter import *
from widgets.text import Text
from shape import *
import pygame


class _Button(_Widget):
    hovered = pressed = released = selected = False

    def __init__(self, *args, color=pygame.Color('green'), **kwargs):
        super().__init__(*args, **kwargs)

        self.color = color

    def input(self, event) -> None:
        if self.enabled:
            super().input(event)

            released(self)
            selected(self)

            try:
                w, h = get_size(self.shape)
            except AttributeError:
                w, h = get_size(self.rect)

            animator.hovered(self, self.hovered)
            animator.pressed(
                self,
                self.pressed,
                (
                    move_negativity(self.rscalex, 5 / w),
                    move_negativity(self.rscaley, 5 / h)
                )
            )


class Button(Text, _Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self, surface: pygame.Surface = ...) -> None:
        if self.can_be_drawn:
            surface = get_surface(surface)

            if self.sprite.texture is None:
                bg = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32)
                pygame.draw.rect(bg, self.color, (0, 0, *self.rect.size), 0, 5)

                if self.selected:
                    pygame.draw.rect(bg, (0, 0, 0), (0, 0, *self.rect.size), 2, 5)

                blit(surface, bg, self.rect.rpos, self.ralpha, self.rscale)
            else:
                self.sprite.draw(surface)

            super().draw(surface)


class DraggableButton(WidgetByShape, _Button):
    dragged = False

    def __init__(
            self,
            *args,
            by_x: bool = True,
            by_y: bool = True,
            area_shape=None,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.by_x, self.by_y = by_x, by_y
        self.area_shape = area_shape

    def input(self, event) -> None:
        if self.enabled:
            super().input(event)

            dragged(self, self.by_x, self.by_y, self.area_shape)
            selected(self)

            w, h = get_size(self.shape)

            animator.hovered(self, self.hovered)
            animator.pressed(
                self,
                self.pressed,
                (
                    move_negativity(self.rscalex, 5 / w),
                    move_negativity(self.rscaley, 5 / h)
                )
            )

    def draw(self, surface: pygame.Surface = ...) -> None:
        if self.can_be_drawn:
            surface = get_surface(surface)

            w, h = get_size(self.shape)

            if self.sprite.texture is None:
                bg = pygame.Surface((w, h), pygame.SRCALPHA, 32)
                pygame.draw.circle(bg, self.color, get_offset(self.shape), w // 2)

                if self.selected:
                    pygame.draw.circle(bg, (0, 0, 0), get_offset(self.shape), w // 2, 2)

                blit(surface, bg, get_rpos(self.shape), self.ralpha, self.rscale)
            else:
                self.sprite.draw(surface)

            super().draw(surface)


__all__ = [
    'Button',
    'DraggableButton'
]
