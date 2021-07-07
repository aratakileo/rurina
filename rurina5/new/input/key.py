from .map import setprocessing, PROCESSING_KEY, PROCESSING_BUTTON
from pygame.key import get_pressed as _get_pressed
from event import keycode as _keycode
from typing import Union


_last_status = {}


def setkey(action_name: str, name: str):
    setprocessing(action_name, name, type=PROCESSING_KEY)


def setbutton(action_name: str, name: str):
    setprocessing(action_name, name, type=PROCESSING_BUTTON)


def last_keystatus(key: Union[int, str]) -> bool:
    if isinstance(key, str):
        key = _keycode(key)

    if key not in _last_status:
        return False

    return _last_status[key]


def is_keypressed(key: Union[int, str]) -> bool:
    if isinstance(key, str):
        key = _keycode(key)

    returned_bool = bool(_get_pressed()[key])
    _last_status[key] = returned_bool

    return returned_bool


def is_keyreleased(key: Union[int, str]) -> bool:
    return not is_keypressed(key) and last_keystatus(key)


def is_just_keypressed(key: Union[int, str]) -> bool:
    return is_keypressed(key) and not last_keystatus(key)
