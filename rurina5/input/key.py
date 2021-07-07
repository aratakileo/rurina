from constants import key_long_press_duration, key_long_press_timeout_duration
from utilities.time import timer_passed, remove_timer
import input.map as inputmap
from typing import Tuple
import sys


def _events(keyname: str, numpad: bool = False) -> Tuple[str, str]:
    pressable = True

    if keyname.startswith('mouse'):
        typename = 'mouse button'
        keyname = keyname[6:]
    elif keyname in ['wheel up', 'wheel down', 'wheel right', 'wheel left']:
        pressable = False
        typename = 'mouse'
    else:
        typename = 'key'

        if numpad:
            typename += ' numpad'

    return (typename + ' down ' + keyname, typename + ' up ' + keyname) if pressable\
        else (typename + ' ' + keyname, typename + ' ' + keyname)


def _key(keyname: str, numpad: bool = False):
    keynames = keyname.split('+')

    event_fullnames = []
    inverse_event_fullnames = []

    for keyname in keynames:
        events = _events(keyname.strip(' '), numpad)
        event_fullnames.append(events[0].rstrip(' '))
        inverse_event_fullnames.append(events[1].rstrip(' '))

    return event_fullnames, inverse_event_fullnames


def setkey(action_name: str, keyname: str, numpad: bool = False):
    inputmap.setevent(action_name, *_key(keyname, numpad))


def removekey(action_name: str, keyname: str, numpad: bool = False):
    inputmap.remove_event(action_name, _key(keyname, numpad)[0])


def havekey(action_name: str, keyname: str, numpad: bool = False) -> bool:
    return inputmap.have_event(action_name, _key(keyname, numpad)[0])


def keystatus(action_name: str, keyname: str, numpad: bool = False) -> bool:
    return inputmap.eventstatus(action_name, _key(keyname, numpad)[0])


def last_keystatus(action_name: str, keyname: str, numpad: bool = False) -> bool:
    return inputmap.last_eventstatus(action_name, _key(keyname, numpad)[0])


def is_action_pressed(name: str) -> bool:
    return inputmap.actionstatus(name)


def is_action_released(name: str) -> bool:
    return not inputmap.actionstatus(name) and inputmap.last_actionstatus(name)


def is_action_just_pressed(name: str) -> bool:
    return inputmap.actionstatus(name) and not inputmap.last_actionstatus(name)


def is_action_just_long_pressed(
        name: str,
        timer_name: str = ...,
        secs: float = key_long_press_duration,
        timeout_secs: float = key_long_press_timeout_duration
) -> bool:
    if is_action_just_pressed(name):
        return True

    timer_name = f'{id(sys.modules[__name__])}:is_action_just_long_pressed:{name}:{timer_name}'

    if is_action_pressed(name):
        return timer_passed(secs, timer_name, False) and \
               (True if timeout_secs <= 0 else timer_passed(timeout_secs, timer_name + ':timeout'))

    remove_timer(timer_name)
    remove_timer(timer_name + ':timeout')

    return False


__all__ = (
    'setkey',
    'removekey',
    'havekey',
    'keystatus',
    'last_keystatus',
    'is_action_pressed',
    'is_action_released',
    'is_action_just_pressed',
    'is_action_just_long_pressed',
)
