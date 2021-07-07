from prefabs.rmath import distance
from shape import Circle, Rect
import pygame


events = [
    False,
    False,
    False
]

last_events = [*events]

active_inputs = [
    None,
    None,
    None
]


selected_widget = None
selectable_widgets = set()


def is_free_input(widget, input_index: int, set_input: bool = True):
    if id(widget) == id(active_inputs[input_index]):
        return True

    if active_inputs[input_index] is None:
        if set_input:
            active_inputs[input_index] = widget

        return True

    return False


def _input(event):
    global events, last_events, selected_widget, active_inputs

    last_events = [*events]

    events[0] = pygame.mouse.get_pressed()[0]

    for e in event:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_TAB:
                events[1] = True
            if e.key == pygame.K_RETURN:
                events[2] = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_TAB:
                events[1] = False
            if e.key == pygame.K_RETURN:
                events[2] = False

    if (pygame.mouse.get_rel() != (0.0, 0.0) or events[0]) and selected_widget is not None:
        events[0] = events[1] = events[2] = False
        selected_widget = active_inputs[0] = active_inputs[1] = active_inputs[2] = None

    return event


def hovered(widget, active: bool = True) -> bool:
    widget.hovered = False

    if widget.enabled:
        if is_free_input(widget, 0, active):
            mx, my = pygame.mouse.get_pos()

            if widget.collide_point(mx, my):
                widget.hovered = True
            else:
                active_inputs[0] = None

        # print(widget, widget.hovered, pygame.mouse.get_pos(), widget.rpos)

    return widget.hovered


def pressed(widget, active: bool = True, _hovered: bool = True) -> bool:
    hovered(widget, _hovered)

    widget.pressed = False

    if widget.enabled:
        try:
            widget.input_data = widget.input_data
        except AttributeError:
            widget.input_data = [False, False]

        if is_free_input(widget, 1, False):
            if events[0] and not widget.input_data[0]:
                if widget.hovered:
                    if active:
                        active_inputs[1] = widget
                    widget.input_data[1] = True
                elif not widget.input_data[1]:
                    widget.input_data[0] = True

                if widget.input_data[1]:
                    widget.pressed = True
            elif not events[0] and widget.input_data[0]:
                widget.input_data[0] = False
            else:
                widget.input_data[1] = False
                active_inputs[1] = None

        try:
            try:
                widget.input_data[3] = widget.input_data[3]
            except IndexError:
                if len(widget.input_data) < 3:
                    widget.input_data.append(False)

                widget.input_data.append(False)

            if is_free_input(widget, 2, False):
                if events[2]:
                    if widget.selected:
                        active_inputs[2] = widget
                        widget.input_data[3] = True

                    if widget.input_data[3]:
                        widget.pressed = True
                else:
                    widget.input_data[3] = False
                    active_inputs[2] = None
        except AttributeError:
            pass

    return widget.pressed


def released(widget) -> bool:
    hovered(widget)
    pressed(widget)

    widget.released = False

    if widget.enabled:
        try:
            widget.input_data[2] = widget.input_data[2]
        except IndexError:
            widget.input_data.append(False)

        if not widget.pressed and widget.input_data[2]:
            if widget.hovered:
                widget.released = True

            try:
                if widget.selected:
                    widget.released = True
            except AttributeError:
                pass

        widget.input_data[2] = widget.pressed

    return widget.released


def was_dragged(w, bx, by, a):
    start_pos = w.rpos
    mx, my = pygame.mouse.get_pos()

    if bx:
        w.rx = mx

    if by:
        w.ry = my

    if isinstance(a, Rect):
        if w.rx < a.x:
            w.rx = a.x

        if w.ry < a.y:
            w.ry = a.y

        if w.rx > a.right:
            w.rx = a.right

        if w.ry > a.bottom:
            w.ry = a.bottom
    elif isinstance(a, Circle):
        if a is not None:
            dx, dy = a.pos
            r = a.radius
            d = distance(dx, dy, *w.rpos)
            if d > r:
                w.rx = dx + (w.rx - dx) / d * r
                w.ry = dy + (w.ry - dy) / d * r

    if start_pos != w.rpos:
        w.dragged = True


def dragged(
        widget,
        by_x: bool = True,
        by_y: bool = True,
        area_shape=None
) -> bool:
    released(widget)

    widget.dragged = False

    if widget.enabled and widget.pressed:
        try:
            if not widget.selected:
                was_dragged(widget, by_x, by_y, area_shape)
        except AttributeError:
            was_dragged(widget, by_x, by_y, area_shape)

    return widget.dragged


def selected(widget) -> bool:
    global selectable_widgets

    widget.selected = False

    if widget.enabled:
        global selected_widget, events

        selectable_widgets.add(widget)

        if events[1] and not last_events[1]:
            events[1] = False

            if selected_widget is None:
                selected_widget = widget
            else:
                __selectable_widgets = list(selectable_widgets)
                index = __selectable_widgets.index(selected_widget)

                index = 0 if index == len(__selectable_widgets) - 1 else index + 1

                selected_widget = __selectable_widgets[index]

        if selected_widget is not None and id(selected_widget) == id(widget):
            widget.selected = True
    elif widget in selectable_widgets:
        selectable_widgets.remove(widget)

    return widget.selected


__all__ = [
    '_input',
    'hovered',
    'pressed',
    'released',
    'dragged',
    'selected'
]
