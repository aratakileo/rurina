from pygame.key import key_code as _keycode, get_pressed as _get_keyspressed
from pygame.mouse import get_pressed as _get_buttons_pressed
from pygame import constants
from typing import Union


keys = {
    constants.K_ESCAPE: 'escape'
    , constants.K_F1: 'f1'
    , constants.K_F2: 'f2'
    , constants.K_F3: 'f3'
    , constants.K_F4: 'f4'
    , constants.K_F5: 'f5'
    , constants.K_F6: 'f6'
    , constants.K_F7: 'f7'
    , constants.K_F8: 'f8'
    , constants.K_F9: 'f9'
    , constants.K_F10: 'f10'
    , constants.K_F11: 'f11'
    , constants.K_F12: 'f12'
    , constants.K_PRINTSCREEN: 'print screen'
    , constants.K_PRINT: 'print'
    , constants.K_SYSREQ: 'system request'
    , constants.K_SCROLLLOCK: 'scroll lock'
    , constants.K_PAUSE: 'pause'
    , constants.K_BREAK: 'break'
    , constants.K_BACKQUOTE: 'backquote'
    , 126: 'tilda'
    , constants.K_1: '1'
    , constants.K_2: '2'
    , constants.K_3: '3'
    , constants.K_4: '4'
    , constants.K_5: '5'
    , constants.K_6: '6'
    , constants.K_7: '7'
    , constants.K_8: '8'
    , constants.K_9: '9'
    , constants.K_0: '0'
    , constants.K_MINUS: 'minus'
    , constants.K_EQUALS: 'equals'
    , constants.K_PLUS: 'plus'
    , constants.K_UNDERSCORE: 'underscore'
    , constants.K_BACKSPACE: 'backspace'
    , constants.K_EXCLAIM: 'exclaim'
    , constants.K_AT: 'at'
    , constants.K_HASH: 'hash'
    , constants.K_DOLLAR: 'dollar'
    , constants.K_PERCENT: 'percent'
    , constants.K_CARET: 'caret'
    , constants.K_AMPERSAND: 'ampersand'
    , constants.K_ASTERISK: 'asterisk'
    , constants.K_LEFTPAREN: 'paren left'
    , constants.K_RIGHTPAREN: 'paren right'
    , constants.K_INSERT: 'insert'
    , constants.K_HOME: 'home'
    , constants.K_PAGEUP: 'page up'
    , constants.K_PAGEDOWN: 'page down'
    , constants.K_DELETE: 'delete'
    , constants.K_END: 'end'
    , constants.K_NUMLOCK: 'num lock'
    , constants.K_NUMLOCKCLEAR: 'num lock clear'
    , constants.K_TAB: 'tab'
    , constants.K_q: 'q'
    , constants.K_w: 'w'
    , constants.K_e: 'e'
    , constants.K_r: 'r'
    , constants.K_t: 't'
    , constants.K_y: 'y'
    , constants.K_u: 'u'
    , constants.K_i: 'i'
    , constants.K_o: 'o'
    , constants.K_p: 'p'
    , constants.K_a: 'a'
    , constants.K_s: 's'
    , constants.K_d: 'd'
    , constants.K_f: 'f'
    , constants.K_g: 'g'
    , constants.K_h: 'h'
    , constants.K_j: 'j'
    , constants.K_k: 'k'
    , constants.K_l: 'l'
    , constants.K_z: 'z'
    , constants.K_x: 'x'
    , constants.K_c: 'c'
    , constants.K_v: 'v'
    , constants.K_b: 'b'
    , constants.K_n: 'n'
    , constants.K_m: 'm'
    , constants.K_SPACE: 'space'
    , constants.K_RETURN: 'enter'
    , constants.K_SLASH: 'slash'
    , constants.K_BACKSLASH: 'backslash'
    , 124: 'pipe'
    , constants.K_LEFTBRACKET: 'bracket left'
    , constants.K_RIGHTBRACKET: 'bracket right'
    , constants.K_COLON: 'colon'
    , constants.K_SEMICOLON: 'semicolon'
    , constants.K_QUOTE: 'quote'
    , constants.K_QUOTEDBL: 'quote double'
    , constants.K_LESS: 'less'
    , constants.K_COMMA: 'comma'
    , constants.K_PERIOD: 'period'
    , constants.K_QUESTION: 'question'
    , constants.K_CAPSLOCK: 'caps lock'
    , constants.K_LSHIFT: 'shift left'
    , constants.K_RSHIFT: 'shift right'
    , constants.K_LCTRL: 'ctrl left'
    , constants.K_RCTRL: 'ctrl right'
    , constants.K_LGUI: 'gui left'
    , constants.K_RGUI: 'gui right'
    , constants.K_LALT: 'alt left'
    , constants.K_RALT: 'alt right'
    , constants.K_LMETA: 'meta left'
    , constants.K_RMETA: 'meta right'
    , constants.K_LSUPER: 'super left'
    , constants.K_RSUPER: 'super right'
    , 1073741925: 'menu'
    , constants.K_LEFT: 'arrow left'
    , constants.K_UP: 'arrow up'
    , constants.K_RIGHT: 'arrow right'
    , constants.K_DOWN: 'arrow down'
    , 1073742093: 'homepage'
    , 1073742089: 'email'
    , 1073742094: 'move left'
    , 1073742095: 'move right'
    , 1073742085: 'play'
    , 1073742084: 'stop'
    , 1073741952: 'volume up'
    , 1073741953: 'volume down'
    , 1073741908: 'numpad slash'
    , 1073741909: 'numpad asterisk'
    , 1073741910: 'numpad minus'
    , 1073741911: 'numpad plus'
    , 1073741912: 'numpad enter'
    , 1073741913: 'numpad 0'
    , 1073741914: 'numpad 1'
    , 1073741915: 'numpad 2'
    , 1073741916: 'numpad 3'
    , 1073741917: 'numpad 4'
    , 1073741918: 'numpad 5'
    , 1073741919: 'numpad 6'
    , 1073741920: 'numpad 7'
    , 1073741921: 'numpad 8'
    , 1073741922: 'numpad 9'
    , 1073741923: 'numpad 10'
}
buttons = {
    constants.BUTTON_LEFT: 'left',
    constants.BUTTON_RIGHT: 'right',
    constants.BUTTON_WHEELUP: 'wheel up',
    constants.BUTTON_WHEELDOWN: 'wheel down',
    constants.BUTTON_X1: 'x1',
    constants.BUTTON_X2: 'x2',
}

_last_keys_status = {}
_last_buttons_status = {}


def button_name(buttoncode: int) -> str:
    if buttoncode in buttons:
        return buttons[buttoncode]

    return 'unknown'


def buttoncode(button_name: str) -> int:
    button_name = button_name.lower()

    if button_name in buttons.values():
        return list(buttons.keys())[list(buttons.values()).index(button_name)]

    return 0


def keyname(keycode: int) -> str:
    if keycode in keys:
        return keys[keycode]

    return 'unknown'


def keycode(keyname: str) -> int:
    keyname = keyname.lower()

    try:
        return _keycode(keyname)
    except ValueError: pass

    if keyname in keys.values():
        return list(keys.keys())[list(keys.values()).index(keyname)]

    return constants.K_UNKNOWN


def last_keystatus(key: Union[int, str]) -> bool:
    if isinstance(key, str):
        key = keycode(key)

    if key not in _last_keys_status:
        _last_keys_status[key] = False

    return _last_keys_status[key]


def is_keypressed(key: Union[int, str]) -> bool:
    if isinstance(key, str):
        key = keycode(key)

    return bool(_get_keyspressed()[key])


def is_keyreleased(key: Union[int, str]) -> bool:
    return last_keystatus(key) and not is_keypressed(key)


def is_just_keypressed(key: Union[int, str]) -> bool:
    return not last_keystatus(key) and is_keypressed(key)


def last_button_status(button: Union[int, str]) -> bool:
    if isinstance(button, str):
        button = buttoncode(button)

    if button not in _last_buttons_status:
        _last_buttons_status[button] = False

    return _last_buttons_status[button]


def is_button_pressed(button: Union[int, str]) -> bool:
    if isinstance(button, str):
        button = buttoncode(button)

    return bool(_get_buttons_pressed()[button - 1])


def is_button_released(button: Union[int, str]) -> bool:
    return last_button_status(button) and not is_button_pressed(button)


def is_just_button_pressed(button: Union[int, str]) -> bool:
    return not last_button_status(button) and is_button_pressed(button)


def flip():
    for key in _last_keys_status:
        _last_keys_status[key] = bool(_get_keyspressed()[key])

    for key in _last_buttons_status:
        _last_buttons_status[key] = bool(_get_buttons_pressed()[key - 1])


__all__ = (
    'keys',
    'buttons',
    'button_name',
    'buttoncode',
    'keyname',
    'keycode',
    'last_keystatus',
    'is_keypressed',
    'is_keyreleased',
    'is_just_keypressed',
    'last_button_status',
    'is_button_pressed',
    'is_button_released',
    'is_just_button_pressed',
    'flip'
)
