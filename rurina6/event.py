from pygame.event import Event, event_name, get as _get, post as _post
from utilities.string import camel_to_snake
from key import keyname, button_name
from typing import List


def typename(type: int) -> str:
    return camel_to_snake(event_name(type)).replace('_', ' ')


def fullname(event: Event) -> str:
    _typename = typename(event.type)

    if _typename.startswith('key'):
        return f'{_typename} {keyname(event.key)} '
    elif _typename.startswith('mouse button'):
        return f'{_typename} {button_name(event.button)} '

    return _typename + ' '


def get(clear_buffer: bool = True) -> List[Event]:
    event = _get()

    if not clear_buffer:
        for e in event:
            _post(e)

    return event


__all__ = (
    'typename',
    'fullname',
    'get',
)
