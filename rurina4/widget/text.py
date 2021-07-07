from widget.widget import InteractiveRectWidget, is_interactive
from input import is_action_pressed, is_action_just_pressed
from pygame import Surface, SRCALPHA, display, mouse
from constants import GRAVITY_LEFT, GRAVITY_TOP
from text import write, lines, lines_gravity
from nodes.collisionshape import get_shape
from utilities.math import by_interval
from typing import List, Union, Tuple
from utilities.clipboard import copy
from event import Event
from font import Font


class Text(InteractiveRectWidget):
    def __init__(
            self,
            *args,
            value: str = '',
            color=(255, 255, 255),
            font: Font = Font(),
            gravity: int = GRAVITY_LEFT | GRAVITY_TOP,
            max_lines: int = None,
            linespacing: int = 0,
            selectable: bool = False,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.color = color
        self.font = font
        self.gravity = gravity
        self.max_lines = max_lines
        self.linespacing = linespacing
        self.selectable = selectable
        self.value = value

        self._selection_anchor = (0, 0)
        self._last_fixed = self._last_hovered = False

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, _value: str):
        self._value = _value
        self._lines = lines(_value, self.font, get_shape(self))
        self._lines_positions = lines_gravity(
            self._lines,
            self.font,
            get_shape(self),
            self.gravity,
            self.linespacing
        )

        self._selected = [(0, 0), (0, 0)]
        self.selected = False

        if self._max_lines not in (None, ...):
            self._lines = self._lines[:self._max_lines]
            self._lines_positions = self._lines_positions[:self._max_lines]

    @property
    def max_lines(self) -> int:
        return self._max_lines if self._max_lines not in (None, ...) else len(self._lines_positions)

    @max_lines.setter
    def max_lines(self, value: int):
        self._max_lines = value if value in (None, ...) else by_interval(abs(int(value)), 1)

    @property
    def lines(self) -> int:
        return len(self._lines_positions[:self.max_lines]) if len(self._value) > 0 else 0

    @property
    def selected(self) -> bool:
        return self._selected[0] != self._selected[1] and self.selectable

    @selected.setter
    def selected(self, value: bool):
        if not value:
            self._selection_anchor = (0, 0)
            self._selected = [(0, 0), (0, 0)]

    def input(self, event: List[Event]):
        if self.enabled:
            super().input(event)

            if self.selectable and self.lines > 0:
                if self.change_mousecursor and self.hovered:
                    mouse.set_cursor(1)
                elif self._last_hovered:
                    mouse.set_cursor(0)

                if self.pressed and self.hovered:
                    _x, y = mouse.get_pos()

                    y -= self.ry
                    y //= self.font.height
                    y = by_interval(int(y), max=self.lines - 1)

                    line = self._lines[y]

                    _x -= self._lines_positions[y][0]
                    x = _x
                    x //= self.font.get_size(line.strip(' '))[0] / len(line.strip(' '))
                    x = by_interval(int(x), max=len(line))

                    w = self.font.get_size(line[:x])[0]
                    w1 = self.font.get_size(line[:x + 1])[0]

                    if _x - w > 0 and _x - w > (w1 - w) / 2:
                        x += 1

                    if self._fixed and not self._last_fixed:
                        self._selection_anchor = y, x
                    elif self._selection_anchor[0] > y or\
                            (self._selection_anchor[0] == y and self._selection_anchor[1] > x):
                        self._selected = [(y, x), self._selection_anchor]
                    else:
                        self._selected = [self._selection_anchor, (y, x)]

                if self.selected:
                    if is_action_just_pressed('ui_copy'):
                        y0, x0 = self._selected[0]
                        y1, x1 = self._selected[1]

                        text = self._lines[y0:y1 + 1]
                        text[0] = text[0][x0:]

                        if y0 == y1:
                            text[-1] = text[-1][:x1 - x0]
                        else:
                            text[-1] = text[-1][:x1]

                        text = '\n'.join(text)
                        copy(text)
                bottom = self.lines - 1, len(self._lines[self.lines - 1])

                if self.hovered:
                    if is_action_just_pressed('ui_page_up'):
                        self._selection_anchor = 0, 0
                    if is_action_just_pressed('ui_page_down'):
                        self._selection_anchor = bottom
                    if is_action_just_pressed('ui_shift'):
                        pass

                if (self.hovered or self._fixed) and is_action_pressed('ui_select_all'):
                    self._selection_anchor = (0, 0)
                    self._selected = [(0, 0), bottom]

                self._last_fixed = self._fixed
                self._last_hovered = self.hovered

    def draw(self, surface: Surface = ..., draw_nodes: bool = True):
        if self.visible:
            if len(self._value) > 0:
                if surface in (None, ...):
                    surface = display.get_surface()

                y0, x0 = self._selected[0]
                y1, x1 = self._selected[1]
                if self.selectable and not (y0 == y1 and (x1 - x0) == 0):

                    _lines_positions = self._lines_positions[y0:y1 + 1]

                    if len(_lines_positions) > 0:
                        _surface = Surface(self.rect.size, SRCALPHA, 32)

                        _lines = self._lines[y0:y1 + 1]
                        _lines[0] = _lines[0][x0:]
                        if y0 == y1:
                            _lines[-1] = _lines[-1][:x1 - x0]
                        else:
                            _lines[-1] = _lines[-1][:x1]

                        _lines_positions[0] = _lines_positions[0][0] + self.font.get_size(self._lines[y0][:x0])[0], _lines_positions[0][1]

                        for i in range(len(_lines_positions)):
                            x, y = _lines_positions[i]
                            x -= self.rx
                            y -= self.ry
                            _surface.blit(self.font._font.render(_lines[i], False, (40, 40, 240), (40, 40, 240)), (x, y))

                        _surface.set_alpha(150)
                        surface.blit(_surface, self.rpos)

                for i in range(len(self._lines_positions[:self.max_lines])):
                    write(self._lines[i], self.font, self._lines_positions[i], self.color, surface)

            if draw_nodes:
                self.draw_nodes(surface)


def move_cursor_position(pos: Tuple[int, int], _object, step: int) -> Tuple[int, int]:
    pass


__all__ = (
    'Text',
)
