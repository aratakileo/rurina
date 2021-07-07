from constants import STYLE_NORMAL, STYLE_BOLD, STYLE_ITALIC
from pygame import Surface, font
from typing import Tuple


font.init()


class Font:
    def __init__(self, name: str = None, size: int = 20, style: int = STYLE_NORMAL, system: bool = True):
        self.name, self.size, self.system, self.style = name, size, system, style

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.__reimport__()

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int):
        self._size = value
        self.__reimport__()

    @property
    def style(self) -> int:
        return self._style

    @style.setter
    def style(self, value: int):
        self._style = value
        self._font.set_bold(self._style & STYLE_BOLD)
        self._font.set_italic(self._style & STYLE_ITALIC)

    @property
    def system(self) -> bool:
        return self._system

    @system.setter
    def system(self, value: bool):
        self._system = value
        self.__reimport__()

    @property
    def height(self) -> int:
        return self._font.get_height()

    def __reimport__(self):
        _dir = self.__dir__()

        if '_name' in _dir and '_size' in _dir and '_system' in _dir:
            self._font = font.Font(self._name, self._size)\
                if self._system else\
                font.SysFont(self._name, self._size)

            if '_style' in _dir:
                self.style = self.style

    def get_size(self, value: str) -> Tuple[int, int]:
        return self._font.size(value)

    def render(self, value: str, color=(255, 255, 255)) -> Surface:
        return self._font.render(value, True, color)


__all__ = (
    'Font',
)
