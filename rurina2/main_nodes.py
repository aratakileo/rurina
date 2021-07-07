from base_node import rootnode, get_surface
from prefabs.surface import blit
from shape import Rect
from node import *
import pygame


def _input(event):
    rootnode.input(event)

    return event


def draw(surface: pygame.Surface = ...):
    rootnode.draw(surface)


class Sprite(Node):
    def __init__(self, texture=None, region_enabled: bool = False, region_rect: Rect = ..., *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.texture = texture
        self.region_enabled = region_enabled
        self.region_rect = region_rect

    @property
    def region_enabled(self) -> bool:
        return self.__region_enabled__

    @region_enabled.setter
    def region_enabled(self, value):
        self.__region_enabled__ = value

        self.reimport_texture()

    @property
    def region_rect(self) -> Rect:
        return self.__region_rect__

    @region_rect.setter
    def region_rect(self, value):
        if value in [..., None]:
            value = Rect(0, 0, 50, 50)

        value.node = self

        try:
            if id(value) != id(self.__region_rect__):
                self.__region_rect__.node = None
        except AttributeError:
            pass

        self.__region_rect__ = value

        self.reimport_texture()

    def reimport_texture(self):
        if self.__original__ is not None:
            self.__texture__ = self.__original__

            if self.region_enabled:
                self.__texture__ = pygame.transform.scale(self.__original__, self.region_rect.size)

    @property
    def texture(self):
        return self.__texture__

    @texture.setter
    def texture(self, value):
        self.__texture__ = None
        self.__original__ = value

        if isinstance(self.__original__, str):
            self.__original__ = pygame.image.load(value).convert_alpha()

        self.reimport_texture()

    @property
    def size(self):
        return (0, 0) if self.texture is None else self.texture.get_size()

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    @property
    def right(self):
        return self.x + self.width

    @property
    def bottom(self):
        return self.y + self.height

    @property
    def fright(self):
        return self.fx + self.width

    @property
    def fbottom(self):
        return self.fy + self.height

    @property
    def rright(self):
        return self.rx + self.width

    @property
    def rbottom(self):
        return self.ry + self.height

    def draw(self, surface: pygame.Surface = ...) -> None:
        if self.can_be_drawn:
            surface = get_surface(surface)

            if self.texture is not None:
                blit(surface, self.texture, self.rpos, self.ralpha, self.rscale)

            super().draw(surface)


class CollisionShape(Node):
    def __init__(
            self,
            shape=None,
            collisiable: bool = True,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.shape = shape
        self.collisiable = collisiable

    @property
    def shape(self):
        return self.__shape__

    @shape.setter
    def shape(self, value):
        self.__shape__ = value

        if value is not None:
            value.node = self

    def collide(self, collision_shape, by_rpos: bool = True):
        if self.shape is not None:
            return self.shape.collide(collision_shape.rect, by_rpos=by_rpos)
        return False

    def collide_point(self, x, y, by_rpos: bool = True):
        if self.shape is not None:
            return self.shape.collide_point(x, y, by_rpos=by_rpos)
        return False


__all__ = [
    'Sprite',
    'CollisionShape',
    '_input',
    'draw',
]
