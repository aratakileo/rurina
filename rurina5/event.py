from pygame import fastevent, constants, event
from utilities.virtkey import state, NUMLOCK
from utilities.string import camel_to_snake
from typing import List


def get(clear_queue: bool = True) -> List[event.Event]:
    if not fastevent.get_init():
        fastevent.init()

    event_buffer = fastevent.get()

    if not clear_queue:
        for e in event_buffer:
            fastevent.post(e)

    return event_buffer


def typename(_event: event.Event) -> str:
    name = 'unknown'
    if _event.type in (constants.MOUSEWHEEL, constants.MOUSEBUTTONDOWN, constants.MOUSEBUTTONUP, constants.MOUSEMOTION):
        name = 'mouse'

        if _event.type == constants.MOUSEWHEEL:
            name += ' wheel'

            if _event.y < 0:
                name += ' down'
            elif _event.y != 0:
                name += ' up'

            if _event.x < 0:
                name += ' right'
            elif _event.x != 0:
                name += ' left'
        elif _event.type == constants.MOUSEMOTION:
            name += ' motion'
        elif _event.type in (constants.MOUSEBUTTONDOWN, constants.MOUSEBUTTONUP):
            name += ' button'

            if _event.type == constants.MOUSEBUTTONDOWN:
                name += ' down'
            else:
                name += ' up'
    elif _event.type in (constants.KEYDOWN, constants.KEYUP):
        name = 'key'

        if _event.key in (
                1073741908,
                1073741909,
                1073741910,
                1073741919,
                1073741920,
                1073741921,
                1073741911,
                1073741916,
                1073741917,
                1073741918,
                1073741913,
                1073741914,
                1073741915,
                1073741912,
                1073741922,
                1073741923
        ):
            name += ' numpad'

        if _event.type == constants.KEYDOWN:
            name += ' down'
        else:
            name += ' up'
    elif _event.type in (constants.TEXTINPUT, constants.TEXTEDITING):
        name = 'text'

        if _event.type == constants.TEXTINPUT:
            name += ' input'
        else:
            name += ' editing'
    elif _event.type in (
            constants.WINDOWCLOSE,
            constants.WINDOWENTER,
            constants.WINDOWLEAVE,
            constants.WINDOWFOCUSGAINED,
            constants.WINDOWFOCUSLOST,
            constants.WINDOWHIDDEN,
            constants.WINDOWSHOWN,
            constants.WINDOWMAXIMIZED,
            constants.WINDOWMINIMIZED,
            constants.WINDOWSIZECHANGED,
            constants.WINDOWRESIZED,
            constants.WINDOWMOVED,
            constants.WINDOWRESTORED,
            constants.WINDOWTAKEFOCUS,
            constants.WINDOWHITTEST,
            constants.WINDOWEXPOSED,
    ):
        name = 'window'

        if _event.type == constants.WINDOWCLOSE:
            name += ' close'
        elif _event.type == constants.WINDOWENTER:
            name += ' enter'
        elif _event.type == constants.WINDOWLEAVE:
            name += ' leave'
        elif _event.type == constants.WINDOWFOCUSGAINED:
            name += ' focus gained'
        elif _event.type == constants.WINDOWFOCUSLOST:
            name += ' focus lost'
        elif _event.type == constants.WINDOWHIDDEN:
            name += ' hidden'
        elif _event.type == constants.WINDOWSHOWN:
            name += ' shown'
        elif _event.type == constants.WINDOWMAXIMIZED:
            name += ' maximized'
        elif _event.type == constants.WINDOWMINIMIZED:
            name += ' minimized'
        elif _event.type == constants.WINDOWSIZECHANGED:
            name += ' sizechanged'
        elif _event.type == constants.WINDOWRESIZED:
            name += ' resized'
        elif _event.type == constants.WINDOWMOVED:
            name += ' moved'
        elif _event.type == constants.WINDOWRESTORED:
            name += ' restored'
        elif _event.type == constants.WINDOWTAKEFOCUS:
            name += ' takefocus'
        elif _event.type == constants.WINDOWHITTEST:
            name += ' hittest'
        elif _event.type == constants.WINDOWEXPOSED:
            name += ' exposed'
    elif _event.type in (constants.VIDEOEXPOSE, constants.VIDEORESIZE):
        name = 'video'

        if _event.type == constants.VIDEOEXPOSE:
            name += ' expose'
        else:
            name += ' resize'
    elif _event.type == constants.NOEVENT:
        name = 'none'
    elif _event.type == constants.USEREVENT:
        name = 'user'
    elif _event.type in (constants.DROPBEGIN, constants.DROPCOMPLETE, constants.DROPFILE, constants.DROPTEXT):
        name = 'drop'

        if _event.type == constants.DROPBEGIN:
            name += ' begin'
        elif _event.type == constants.DROPCOMPLETE:
            name += ' complete'
        elif _event.type == constants.DROPFILE:
            name += ' file'
        else:
            name += ' text'
    elif _event.type in (constants.FINGERMOTION, constants.FINGERDOWN, constants.FINGERUP):
        name = 'finger'

        if _event.type == constants.FINGERMOTION:
            name += ' motion'
        elif _event.type == constants.FINGERDOWN:
            name += ' down'
        else:
            name += ' up'
    elif _event.type in (constants.MIDIIN, constants.MIDIOUT):
        name = 'midi'

        if _event.type == constants.MIDIIN:
            name += ' in'
        else:
            name += ' out'
    elif _event.type in (
            constants.AUDIODEVICEADDED,
            constants.AUDIODEVICEREMOVED,
            constants.JOYDEVICEADDED,
            constants.JOYDEVICEREMOVED,
            constants.CONTROLLERDEVICEADDED,
            constants.CONTROLLERDEVICEREMOVED,
            constants.CONTROLLERDEVICEREMAPPED,
    ):
        name = 'device'

        if _event.type == constants.AUDIODEVICEADDED:
            name += 'added audio'
        elif _event.type == constants.AUDIODEVICEREMOVED:
            name += 'removed audio'
        elif _event.type == constants.JOYDEVICEADDED:
            name += 'added joy'
        elif _event.type == constants.JOYDEVICEREMOVED:
            name += 'removed joy'
        elif _event.type == constants.CONTROLLERDEVICEADDED:
            name += 'added controller'
        elif _event.type == constants.CONTROLLERDEVICEREMOVED:
            name += 'removed controller'
        elif _event.type == constants.CONTROLLERDEVICEREMAPPED:
            name += 'mapped controller'
    elif _event.type == constants.ACTIVEEVENT:
        name = 'active'
    elif _event.type == constants.QUIT:
        name = 'quit'

    return name


def typename2(_event: event.Event) -> str:
    return camel_to_snake(event.event_name(_event.type)).replace('_', ' ')


def keyname(_event: event.Event) -> str:
    _type_name = typename(_event)
    name = 'unknown'

    if 'key' in _type_name:
        if _event.key == constants.K_ESCAPE:
            name = 'escape'
        elif _event.key == constants.K_F1:
            name = 'F1'
        elif _event.key == constants.K_F2:
            name = 'F2'
        elif _event.key == constants.K_F3:
            name = 'F3'
        elif _event.key == constants.K_F4:
            name = 'F4'
        elif _event.key == constants.K_F5:
            name = 'F5'
        elif _event.key == constants.K_F6:
            name = 'F6'
        elif _event.key == constants.K_F7:
            name = 'F7'
        elif _event.key == constants.K_F8:
            name = 'F8'
        elif _event.key == constants.K_F9:
            name = 'F9'
        elif _event.key == constants.K_F10:
            name = 'F10'
        elif _event.key == constants.K_F11:
            name = 'F11'
        elif _event.key == constants.K_F12:
            name = 'F12'
        elif _event.key == constants.K_BACKQUOTE:
            name = 'backquote'
        elif _event.key == constants.K_BACKSPACE:
            name = 'backspace'
        elif _event.key == constants.K_TAB:
            name = 'tab'
        elif _event.key == constants.K_CAPSLOCK:
            name = 'capslock'
        elif _event.key in (constants.K_RSHIFT, constants.K_LSHIFT):
            name = 'shift'

            if _event.key == constants.K_RSHIFT:
                name += ' right'
            else:
                name += ' left'
        elif _event.key in (constants.K_RGUI, constants.K_LGUI):
            name = 'GUI'

            if _event.key == constants.K_RGUI:
                name += ' right'
            else:
                name += ' left'
        elif _event.key in (constants.K_RCTRL, constants.K_LCTRL):
            name = 'ctrl'

            if _event.key == constants.K_RCTRL:
                name += ' right'
            else:
                name += ' left'
        elif _event.key in (constants.K_RALT, constants.K_LALT):
            name = 'alt'

            if _event.key == constants.K_RCTRL:
                name += ' right'
            else:
                name += ' left'
        elif _event.key in (constants.K_RETURN, 1073741912):
            name = 'enter'
        elif _event.key in (constants.K_SLASH, 1073741908):
            name = 'slash'
        elif _event.key in (constants.K_ASTERISK, 1073741909):
            name = 'asterisk'
        elif _event.key in (constants.K_MINUS, 1073741910):
            name = 'minus'
        elif _event.key in (constants.K_1, 1073741913):
            name = '1' if state(NUMLOCK) else 'end'
        elif _event.key in (constants.K_2, 1073741914):
            name = '2' if state(NUMLOCK) else 'arrow down'
        elif _event.key in (constants.K_3, 1073741915):
            name = '3' if state(NUMLOCK) else 'page down'
        elif _event.key in (constants.K_4, 1073741916):
            name = '4' if state(NUMLOCK) else 'arrow left'
        elif _event.key in (constants.K_5, 1073741917):
            name = '5' if state(NUMLOCK) else 'void'
        elif _event.key in (constants.K_6, 1073741918):
            name = '6' if state(NUMLOCK) else 'arrow right'
        elif _event.key in (constants.K_7, 1073741919):
            name = '7' if state(NUMLOCK) else 'home'
        elif _event.key in (constants.K_8, 1073741920):
            name = '8' if state(NUMLOCK) else 'arrow up'
        elif _event.key in (constants.K_9, 1073741921):
            name = '9' if state(NUMLOCK) else 'page up'
        elif _event.key in (constants.K_0, 1073741922):
            name = '0' if state(NUMLOCK) else 'insert'
        elif _event.key in (constants.K_PLUS, 1073741911):
            name = 'plus'
        elif _event.key == 1073741923:
            name = 'dot' if state(NUMLOCK) else 'delete'
        elif _event.key == constants.K_BACKSLASH:
            name = 'backslash'
        elif _event.key == constants.K_SPACE:
            name = 'space'
        elif _event.key == constants.K_q:
            name = 'q'
        elif _event.key == constants.K_w:
            name = 'w'
        elif _event.key == constants.K_e:
            name = 'e'
        elif _event.key == constants.K_r:
            name = 'r'
        elif _event.key == constants.K_t:
            name = 't'
        elif _event.key == constants.K_y:
            name = 'y'
        elif _event.key == constants.K_u:
            name = 'u'
        elif _event.key == constants.K_i:
            name = 'i'
        elif _event.key == constants.K_o:
            name = 'o'
        elif _event.key == constants.K_a:
            name = 'a'
        elif _event.key == constants.K_s:
            name = 's'
        elif _event.key == constants.K_d:
            name = 'd'
        elif _event.key == constants.K_f:
            name = 'f'
        elif _event.key == constants.K_g:
            name = 'g'
        elif _event.key == constants.K_h:
            name = 'h'
        elif _event.key == constants.K_j:
            name = 'j'
        elif _event.key == constants.K_k:
            name = 'k'
        elif _event.key == constants.K_l:
            name = 'l'
        elif _event.key == constants.K_z:
            name = 'z'
        elif _event.key == constants.K_x:
            name = 'x'
        elif _event.key == constants.K_c:
            name = 'c'
        elif _event.key == constants.K_v:
            name = 'v'
        elif _event.key == constants.K_b:
            name = 'b'
        elif _event.key == constants.K_n:
            name = 'n'
        elif _event.key == constants.K_m:
            name = 'm'
        elif _event.key in (constants.K_RIGHTBRACKET, constants.K_LEFTBRACKET):
            name = 'bracket'

            if _event.key == constants.K_RIGHTBRACKET:
                name += ' right'
            else:
                name += ' left'
        elif _event.key in (constants.K_RIGHTPAREN, constants.K_LEFTPAREN):
            name = 'paren'

            if _event.key == constants.K_RIGHTPAREN:
                name += ' right'
            else:
                name += ' left'
        elif _event.key == constants.K_QUOTE:
            name = 'quote'
        elif _event.key == constants.K_QUESTION:
            name = 'question'
        elif _event.key == constants.K_SEMICOLON:
            name = 'semicolon'
        elif _event.key == constants.K_COLON:
            name = 'colon'
        elif _event.key == constants.K_EQUALS:
            name = 'equals'
        elif _event.key in (constants.K_RIGHT, constants.K_LEFT, constants.K_DOWN, constants.K_UP):
            name = 'arrow'

            if _event.key == constants.K_RIGHT:
                name += ' right'
            elif _event.key == constants.K_LEFT:
                name += ' left'
            elif _event.key == constants.K_DOWN:
                name += ' down'
            else:
                name += ' up'
        elif _event.key == constants.K_INSERT:
            name = 'insert'
        elif _event.key == constants.K_HOME:
            name = 'home'
        elif _event.key in (constants.K_PAGEUP, constants.K_PAGEDOWN):
            name = 'page'

            if _event.key == constants.K_PAGEUP:
                name += ' up'
            else:
                name += ' down'
        elif _event.key == constants.K_DELETE:
            name = 'delete'
        elif _event.key == constants.K_END:
            name = 'end'
        elif _event.key == constants.K_SYSREQ:
            name = 'sysreq'
        elif _event.key == constants.K_SCROLLLOCK:
            name = 'scrolllock'
        elif _event.key == constants.K_NUMLOCK:
            name = 'numlock'
        elif _event.key == constants.K_NUMLOCKCLEAR:
            name = 'numlockclear'
        elif _event.key == constants.K_PERIOD:
            name = 'period'
        elif _event.key == constants.K_COMMA:
            name = 'comma'
        elif _event.key == 1073741925:
            name = 'menu'
    elif 'mouse button' in _type_name:
        if _event.button == constants.BUTTON_LEFT:
            name = 'left'
        elif _event.button == constants.BUTTON_RIGHT:
            name = 'right'
        elif _event.button == constants.BUTTON_MIDDLE:
            name = 'middle'
        elif _event.button == constants.BUTTON_WHEELUP:
            name = 'wheel up'
        elif _event.button == constants.BUTTON_WHEELDOWN:
            name = 'wheel down'
    else:
        name = ''

    return name


def fullname(_event: event.Event) -> str:
    return f'{typename(_event)} {keyname(_event)} '


__all__ = (
    'get',
    'typename',
    'keyname',
    'fullname',
)
