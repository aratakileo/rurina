from main_nodes import Sprite, CollisionShape, draw
from shape import Rect, Circle
from node import Node
import pygame


class _Widget(Node):
    def __init__(
            self,
            *args,
            gravity: int = 0,
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.sprite = Sprite(parent=self, auto_draw=False)

        self.gravity = gravity


class WidgetByRect(_Widget):
    def __init__(
            self,
            *args,
            rect=None,
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.rect = rect

    @property
    def rect(self) -> Rect:
        return self.sprite.region_rect

    @rect.setter
    def rect(self, value):
        self.sprite.region_rect = value

    def collide(self, widget):
        return self.rect.collide(widget.rect)

    def collide_point(self, x, y):
        return self.rect.collide_point(x, y)


class WidgetByShape(_Widget):
    def __init__(
            self,
            *args,
            shape=None,
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.shape = shape

    @property
    def shape(self) -> any:
        return self.__shape__

    @shape.setter
    def shape(self, value):
        if value in [None, ...]:
            value = Circle(0, 0, 25)

        value.node = self

        try:
            if id(value) != id(self.__shape__):
                self.__shape__.node = None
        except AttributeError:
            pass

        self.__shape__ = value

    def collide(self, widget):
        return self.shape.collide(widget.rect)

    def collide_point(self, x, y):
        return self.shape.collide_point(x, y)


__all__ = [
    '_Widget',
    'WidgetByRect',
    'WidgetByShape'
]
