from utilities.time import passed, remove_passed
from pygame import Surface, draw, display
from utilities.clipboard import paste
from input import is_action_pressed
from widget.text import Text
from typing import List
from event import Event


class EditText(Text):
    def __init__(self, *args, selectable: bool = True, **kwargs):
        super().__init__(*args, selectable=selectable, **kwargs)
        self._cursor_display = True

    def input(self, event: List[Event]):
        if self.enabled:
            super().input(event)

            inputted = False
            insert = ''
            lines = self.lines

            if self.selected and lines > 0:
                y0, x0 = self._selected[0]
                y1, x1 = self._selected[1]

                value_before = '\n'.join(self._lines[:y0])
                value_before += '\n' + self._lines[:y0 + 1][-1][:x0]
                pos_before = y0, x0

                value_after = self._lines[y1:][-1][x1:]
                value_after += '\n'.join(self._lines[y1 + 1:])
            else:
                value_before = '\n'.join(self._lines[:self._selection_anchor[0]])
                value_before += '\n' + self._lines[:self._selection_anchor[0] + 1][-1][:self._selection_anchor[1]]
                pos_before = self._selection_anchor

                value_after = '\n'.join(self._lines)[len(value_before):]

            if is_action_pressed('ui_paste') and passed(0.04, f'{id(self)}:ui_paste'):
                insert = paste()
            else:
                for e in event:
                    if 'key down' in e and 'ctrl' not in e:
                        insert = e.unicode

            if insert != '':
                self.value = value_before + insert + value_after
                inputted = True

            if is_action_pressed('ui_backspace') and passed(0.04, f'{id(self)}:ui_backspace'):
                self.value = value_before[:-1] + value_after
                inputted = True

            if inputted:
                self._selection_anchor = pos_before[0] + self.lines - lines, len(self._lines[self.lines - 1])
                # self._selection_anchor = (self.lines - 1, len(self._lines[self.lines - 1]))

            if not self.hovered:
                remove_passed(f'{id(self)}:ui_backspace')
                remove_passed(f'{id(self)}:ui_paste')

            if len(self._value) > 0 and self.released:
                remove_passed(f'{id(self)}:_cursor_display')
                self._cursor_display = True

    def draw(self, surface: Surface = ..., draw_nodes: bool = True):
        if self.visible:
            super().draw(surface, False)

            if len(self._value) > 0:
                if passed(0.5, f'{id(self)}:_cursor_display'):
                    self._cursor_display = not self._cursor_display

                if self._cursor_display:
                    if surface in (None, ...):
                        surface = display.get_surface()

                    cursorx, cursory = self._lines_positions[self._selection_anchor[0]]
                    # print((cursorx, cursory), self._selection_anchor)
                    cursorx += self.font.get_size(self._lines[self._selection_anchor[0]][:self._selection_anchor[1]])[0]
                    # print(cursorx)

                    draw.line(surface, (255, 255, 255), (cursorx, cursory), (cursorx, cursory + self.font.height), 2)

            if draw_nodes:
                self.draw_nodes(surface)
