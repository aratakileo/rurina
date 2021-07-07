from pygame import event, constants
from typing import List, Union
from copy import copy


class Event:
    def __init__(self, code: str, type: int, **kwargs):
        _event = event.Event(type, **kwargs)
        self.__dict__ = _event.__dict__
        self.type = type
        self.code = code

    def __str__(self):
        _dict = self.__dict__.copy()
        del _dict['type'], _dict['code']
        return f'<{self.__class__.__name__}(' \
               f'{self.code} => {self.type}-{event.event_name(self.type)} {_dict}' \
               f')>'

    __repr__ = __str__

    def __eq__(self, other: Union[str, 'Event']):
        if isinstance(other, str):
            return self.code.lower().strip(' ') == other.lower().strip(' ')
        elif isinstance(other, Event):
            return self.code.lower().strip(' ') == other.code.lower().strip(' ')

        return False

    def __contains__(self, other: Union[str, 'Event']):
        if isinstance(other, str):
            return other.lower() in self.code.lower()
        elif isinstance(other, Event):
            return other.code.lower() in self.code.lower()

        return False

    def copy(self):
        return copy(self)


events = []


def get(clear_buffer: bool = True) -> List[Event]:
    _events = events.copy()

    if clear_buffer:
        clear()

    return _events


def post(event):
    events.append(event)


def clear():
    event.clear()
    events.clear()


def event_code(event) -> str:
    _event_code = 'unknown'
    if event.type in (constants.MOUSEWHEEL, constants.MOUSEBUTTONDOWN, constants.MOUSEBUTTONUP, constants.MOUSEMOTION):
        _event_code = 'mouse'

        if event.type == constants.MOUSEWHEEL:
            _event_code += ' wheel'

            if event.y < 0:
                _event_code += ' down'
            else:
                _event_code += ' up'
        elif event.type == constants.MOUSEMOTION:
            _event_code += ' motion'
        elif event.type in (constants.MOUSEBUTTONDOWN, constants.MOUSEBUTTONUP):
            _event_code += ' button'

            if event.type == constants.MOUSEBUTTONDOWN:
                _event_code += ' down'
            else:
                _event_code += ' up'

            if event.button == constants.BUTTON_LEFT:
                _event_code += ' left'
            elif event.button == constants.BUTTON_RIGHT:
                _event_code += ' right'
            elif event.button == constants.BUTTON_MIDDLE:
                _event_code += ' middle'
    elif event.type in (constants.KEYDOWN, constants.KEYUP):
        _event_code = 'key'

        if event.key in (
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
            _event_code += ' numpad'

        if event.type == constants.KEYDOWN:
            _event_code += ' down'
        else:
            _event_code += ' up'

        if event.key == constants.K_ESCAPE:
            _event_code += ' escape'
        elif event.key == constants.K_F1:
            _event_code += ' F1'
        elif event.key == constants.K_F2:
            _event_code += ' F2'
        elif event.key == constants.K_F3:
            _event_code += ' F3'
        elif event.key == constants.K_F4:
            _event_code += ' F4'
        elif event.key == constants.K_F5:
            _event_code += ' F5'
        elif event.key == constants.K_F6:
            _event_code += ' F6'
        elif event.key == constants.K_F7:
            _event_code += ' F7'
        elif event.key == constants.K_F8:
            _event_code += ' F8'
        elif event.key == constants.K_F9:
            _event_code += ' F9'
        elif event.key == constants.K_F10:
            _event_code += ' F10'
        elif event.key == constants.K_F11:
            _event_code += ' F11'
        elif event.key == constants.K_F12:
            _event_code += ' F12'
        elif event.key == constants.K_BACKQUOTE:
            _event_code += ' backquote'
        elif event.key == constants.K_BACKSPACE:
            _event_code += ' backspace'
        elif event.key == constants.K_TAB:
            _event_code += ' tab'
        elif event.key == constants.K_CAPSLOCK:
            _event_code += ' capslock'
        elif event.key in (constants.K_RSHIFT, constants.K_LSHIFT):
            _event_code += ' shift'

            if event.key == constants.K_RSHIFT:
                _event_code += ' right'
            else:
                _event_code += ' left'
        elif event.key in (constants.K_RGUI, constants.K_LGUI):
            _event_code += ' GUI'

            if event.key == constants.K_RGUI:
                _event_code += ' right'
            else:
                _event_code += ' left'
        elif event.key in (constants.K_RCTRL, constants.K_LCTRL):
            _event_code += ' ctrl'

            if event.key == constants.K_RCTRL:
                _event_code += ' right'
            else:
                _event_code += ' left'
        elif event.key in (constants.K_RALT, constants.K_LALT):
            _event_code += ' alt'

            if event.key == constants.K_RCTRL:
                _event_code += ' right'
            else:
                _event_code += ' left'
        elif event.key in (constants.K_RETURN, 1073741912):
            _event_code += ' enter'
        elif event.key in (constants.K_SLASH, 1073741908):
            _event_code += ' slash'
        elif event.key in (constants.K_ASTERISK, 1073741909):
            _event_code += ' asterisk'
        elif event.key in (constants.K_MINUS, 1073741910):
            _event_code += ' minus'
        elif event.key in (constants.K_1, 1073741913):
            _event_code += ' 1'
        elif event.key in (constants.K_2, 1073741914):
            _event_code += ' 2'
        elif event.key in (constants.K_3, 1073741915):
            _event_code += ' 3'
        elif event.key in (constants.K_4, 1073741916):
            _event_code += ' 4'
        elif event.key in (constants.K_5, 1073741917):
            _event_code += ' 5'
        elif event.key in (constants.K_6, 1073741918):
            _event_code += ' 6'
        elif event.key in (constants.K_7, 1073741919):
            _event_code += ' 7'
        elif event.key in (constants.K_8, 1073741920):
            _event_code += ' 8'
        elif event.key in (constants.K_9, 1073741921):
            _event_code += ' 9'
        elif event.key in (constants.K_0, 1073741922):
            _event_code += ' 0'
        elif event.key in (constants.K_PLUS, 1073741911):
            _event_code += ' plus'
        elif event.key == 1073741923:
            _event_code += ' dot'
        elif event.key == constants.K_BACKSLASH:
            _event_code += ' backslash'
        elif event.key == constants.K_SPACE:
            _event_code += ' space'
        elif event.key == constants.K_q:
            _event_code += ' q'
        elif event.key == constants.K_w:
            _event_code += ' w'
        elif event.key == constants.K_e:
            _event_code += ' e'
        elif event.key == constants.K_r:
            _event_code += ' r'
        elif event.key == constants.K_t:
            _event_code += ' t'
        elif event.key == constants.K_y:
            _event_code += ' y'
        elif event.key == constants.K_u:
            _event_code += ' u'
        elif event.key == constants.K_i:
            _event_code += ' i'
        elif event.key == constants.K_o:
            _event_code += ' o'
        elif event.key == constants.K_a:
            _event_code += ' a'
        elif event.key == constants.K_s:
            _event_code += ' s'
        elif event.key == constants.K_d:
            _event_code += ' d'
        elif event.key == constants.K_f:
            _event_code += ' f'
        elif event.key == constants.K_g:
            _event_code += ' g'
        elif event.key == constants.K_h:
            _event_code += ' h'
        elif event.key == constants.K_j:
            _event_code += ' j'
        elif event.key == constants.K_k:
            _event_code += ' k'
        elif event.key == constants.K_l:
            _event_code += ' l'
        elif event.key == constants.K_z:
            _event_code += ' z'
        elif event.key == constants.K_x:
            _event_code += ' x'
        elif event.key == constants.K_c:
            _event_code += ' c'
        elif event.key == constants.K_v:
            _event_code += ' v'
        elif event.key == constants.K_b:
            _event_code += ' b'
        elif event.key == constants.K_n:
            _event_code += ' n'
        elif event.key == constants.K_m:
            _event_code += ' m'
        elif event.key in (constants.K_RIGHTBRACKET, constants.K_LEFTBRACKET):
            _event_code += ' bracket'

            if event.key == constants.K_RIGHTBRACKET:
                _event_code += ' right'
            else:
                _event_code += ' left'
        elif event.key in (constants.K_RIGHTPAREN, constants.K_LEFTPAREN):
            _event_code += ' paren'

            if event.key == constants.K_RIGHTPAREN:
                _event_code += ' right'
            else:
                _event_code += ' left'
        elif event.key == constants.K_QUOTE:
            _event_code += ' quote'
        elif event.key == constants.K_QUESTION:
            _event_code += ' question'
        elif event.key == constants.K_SEMICOLON:
            _event_code += ' semicolon'
        elif event.key == constants.K_COLON:
            _event_code += ' colon'
        elif event.key == constants.K_EQUALS:
            _event_code += ' equals'
        elif event.key in (constants.K_RIGHT, constants.K_LEFT, constants.K_DOWN, constants.K_UP):
            _event_code += ' arrow'

            if event.key == constants.K_RIGHT:
                _event_code += ' right'
            elif event.key == constants.K_LEFT:
                _event_code += ' left'
            elif event.key == constants.K_DOWN:
                _event_code += ' down'
            else:
                _event_code += ' up'
        elif event.key == constants.K_INSERT:
            _event_code += ' insert'
        elif event.key == constants.K_HOME:
            _event_code += ' home'
        elif event.key in (constants.K_PAGEUP, constants.K_PAGEDOWN):
            _event_code += ' page'

            if event.key == constants.K_PAGEUP:
                _event_code += ' up'
            else:
                _event_code += ' down'
        elif event.key == constants.K_DELETE:
            _event_code += ' delete'
        elif event.key == constants.K_END:
            _event_code += ' end'
        elif event.key == constants.K_SYSREQ:
            _event_code += ' sysreq'
        elif event.key == constants.K_SCROLLLOCK:
            _event_code += ' scrolllock'
        elif event.key == constants.K_NUMLOCK:
            _event_code += ' numlock'
        elif event.key == constants.K_NUMLOCKCLEAR:
            _event_code += ' numlockclear'
        elif event.key == constants.K_PERIOD:
            _event_code += ' period'
        elif event.key == constants.K_COMMA:
            _event_code += ' comma'
        elif event.key == 1073741925:
            _event_code += ' menu'
    elif event.type in (constants.TEXTINPUT, constants.TEXTEDITING):
        _event_code = 'text'

        if event.type == constants.TEXTINPUT:
            _event_code += ' input'
        else:
            _event_code += ' editing'
    elif event.type in (
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
        _event_code = 'window'

        if event.type == constants.WINDOWCLOSE:
            _event_code += ' close'
        elif event.type == constants.WINDOWENTER:
            _event_code += ' enter'
        elif event.type == constants.WINDOWLEAVE:
            _event_code += ' leave'
        elif event.type == constants.WINDOWFOCUSGAINED:
            _event_code += ' focus gained'
        elif event.type == constants.WINDOWFOCUSLOST:
            _event_code += ' focus lost'
        elif event.type == constants.WINDOWHIDDEN:
            _event_code += ' hidden'
        elif event.type == constants.WINDOWSHOWN:
            _event_code += ' shown'
        elif event.type == constants.WINDOWMAXIMIZED:
            _event_code += ' maximized'
        elif event.type == constants.WINDOWMINIMIZED:
            _event_code += ' minimized'
        elif event.type == constants.WINDOWSIZECHANGED:
            _event_code += ' sizechanged'
        elif event.type == constants.WINDOWRESIZED:
            _event_code += ' resized'
        elif event.type == constants.WINDOWMOVED:
            _event_code += ' moved'
        elif event.type == constants.WINDOWRESTORED:
            _event_code += ' restored'
        elif event.type == constants.WINDOWTAKEFOCUS:
            _event_code += ' takefocus'
        elif event.type == constants.WINDOWHITTEST:
            _event_code += ' hittest'
        elif event.type == constants.WINDOWEXPOSED:
            _event_code += ' exposed'
    elif event.type in (constants.VIDEOEXPOSE, constants.VIDEORESIZE):
        _event_code = 'video'

        if event.type == constants.VIDEOEXPOSE:
            _event_code += ' expose'
        else:
            _event_code += ' resize'
    elif event.type == constants.NOEVENT:
        _event_code = 'none'
    elif event.type == constants.USEREVENT:
        _event_code = 'user'
    elif event.type in (constants.DROPBEGIN, constants.DROPCOMPLETE, constants.DROPFILE, constants.DROPTEXT):
        _event_code = 'drop'

        if event.type == constants.DROPBEGIN:
            _event_code += ' begin'
        elif event.type == constants.DROPCOMPLETE:
            _event_code += ' complete'
        elif event.type == constants.DROPFILE:
            _event_code += ' file'
        else:
            _event_code += ' text'
    elif event.type in (constants.FINGERMOTION, constants.FINGERDOWN, constants.FINGERUP):
        _event_code = 'finger'

        if event.type == constants.FINGERMOTION:
            _event_code += ' motion'
        elif event.type == constants.FINGERDOWN:
            _event_code += ' down'
        else:
            _event_code += ' up'
    elif event.type in (constants.MIDIIN, constants.MIDIOUT):
        _event_code = 'midi'

        if event.type == constants.MIDIIN:
            _event_code += ' in'
        else:
            _event_code += ' out'
    elif event.type in (
        constants.AUDIODEVICEADDED,
        constants.AUDIODEVICEREMOVED,
        constants.JOYDEVICEADDED,
        constants.JOYDEVICEREMOVED,
        constants.CONTROLLERDEVICEADDED,
        constants.CONTROLLERDEVICEREMOVED,
        constants.CONTROLLERDEVICEREMAPPED,
    ):
        _event_code = 'device'

        if event.type == constants.AUDIODEVICEADDED:
            _event_code += 'added audio'
        elif event.type == constants.AUDIODEVICEREMOVED:
            _event_code += 'removed audio'
        elif event.type == constants.JOYDEVICEADDED:
            _event_code += 'added joy'
        elif event.type == constants.JOYDEVICEREMOVED:
            _event_code += 'removed joy'
        elif event.type == constants.CONTROLLERDEVICEADDED:
            _event_code += 'added controller'
        elif event.type == constants.CONTROLLERDEVICEREMOVED:
            _event_code += 'removed controller'
        elif event.type == constants.CONTROLLERDEVICEREMAPPED:
            _event_code += 'mapped controller'
    elif event.type == constants.ACTIVEEVENT:
        _event_code = 'active'
    elif event.type == constants.QUIT:
        _event_code = 'quit'

    return _event_code


def _code(code: Union[str, Event]) -> str:
    return (code if isinstance(code, str) else code.code).strip(' ')


def code_combination(code: Union[str, Event]) -> List[str]:
    code = _code(code)

    if '+' in code:
        code = code.split('+')

        for i in range(len(code)):
            code[i] = code[i].strip(' ')

        return code

    return [code.strip(' ')]


def code_type(code: Union[str, Event]) -> str:
    code = _code(code)

    if code.startswith('key numpad'):
        return 'key numpad'

    if code.startswith('key'):
        return 'key'

    if code.startswith('none'):
        return 'none'

    if code.startswith('user'):
        return 'user'

    if code.startswith('active'):
        return 'active'

    if code.startswith('quit'):
        return 'quit'

    if code.startswith('mouse') or code.startswith('text') or code.startswith('window') or code.startswith('video')\
            or code.startswith('drop') or code.startswith('finger') or code.startswith('midi')\
            or code.startswith('device'):
        return ' '.join(code.split(' ')[:2])

    return 'unknown'


def flip(auto_quit: bool = True):
    events.clear()
    for e in event.get():
        events.append(Event(event_code(e), e.type, **e.__dict__))

        if auto_quit and 'quit' in events[-1]:
            exit()

        event.post(e)


__all__ = (
    'Event',
    'get',
    'post',
    'clear',
    'event_code',
    'code_combination',
    'code_type',
    'flip'
)
