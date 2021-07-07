from typing import Union, List
import pygame

supported_types = Union[str, 'Event']
events: List['Event'] = []


class Event:
    def __init__(self, name: str, pygame_event: Union[pygame.event.Event, int]):
        if not isinstance(name, str):
            raise TypeError(f'argument 1 must be \'str\', not \'{name.__class__.__name__}\'')

        if pygame_event.__class__.__name__ == 'Event' and not isinstance(pygame_event, Event):
            self.__dict__ = pygame_event.__dict__
        elif isinstance(pygame_event, int):
            self.__dict__ = pygame.event.Event(pygame_event, {}).__dict__
        else:
            raise TypeError(f'argument 2 must be \'pygame.event.Event\' or \'int\', not \'{name.__class__.__name__}\'')

        self.__name__ = name
    
    @property
    def name(self):
        return self.__name__
    
    def __str__(self):
        return f'<Event({self.name} {self.__dict__})>'
    
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other: supported_types):
        if isinstance(other, str):
            return other.lower() == self.name.lower()
        elif isinstance(other, Event):
            return other.name.lower() == self.name.lower()
        elif other.__class__.__name__ == 'Event' and not isinstance(other, Event):
            __dict__ = self.__dict__
            __dict__.update(other.__dict__)
            return self.__dict__ == __dict__
        else:
            raise TypeError(f'unsupported operand type(s) for ==:'
                            f' \'{self.__class__.__name__}\' and \'{other.__class__.__name__}\'')

    def __contains__(self, other: supported_types):
        if isinstance(other, str):
            return other.lower() in self.name.lower()
        elif isinstance(other, Event):
            return other.name.lower() in self.name.lower()
        elif other.__class__.__name__ == 'Event' and not isinstance(other, Event):
            return self == other
        else:
            raise TypeError(f'unsupported operand type(s) for ==:'
                            f' \'{self.__class__.__name__}\' and \'{other.__class__.__name__}\'')


def input() -> None:
    events.clear()

    for e in pygame.event.get():
        pygame.event.post(e)

        event_code = 'unknown'
        if e.type in (pygame.MOUSEWHEEL, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
            event_code = 'mouse'

            if e.type == pygame.MOUSEWHEEL:
                event_code += ' wheel'

                if e.y < 0:
                    event_code += ' down'
                else:
                    event_code += ' up'
            elif e.type == pygame.MOUSEMOTION:
                event_code += ' motion'
            elif e.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
                event_code += ' button'

                if e.type == pygame.MOUSEBUTTONDOWN:
                    event_code += ' down'
                else:
                    event_code += ' up'

                if e.button == pygame.BUTTON_LEFT:
                    event_code += ' left'
                elif e.button == pygame.BUTTON_RIGHT:
                    event_code += ' right'
                elif e.button == pygame.BUTTON_MIDDLE:
                    event_code += ' middle'
        elif e.type == (pygame.KEYDOWN, pygame.KEYUP):
            event_code = 'key'

            if pygame.KEYDOWN:
                event_code += ' down'
            else:
                event_code += ' up'

            if e.key == pygame.K_ESCAPE:
                event_code += ' escape'
            elif e.key == pygame.K_F1:
                event_code += ' F1'
            elif e.key == pygame.K_F2:
                event_code += ' F2'
            elif e.key == pygame.K_F3:
                event_code += ' F3'
            elif e.key == pygame.K_F4:
                event_code += ' F4'
            elif e.key == pygame.K_F5:
                event_code += ' F5'
            elif e.key == pygame.K_F6:
                event_code += ' F6'
            elif e.key == pygame.K_F7:
                event_code += ' F7'
            elif e.key == pygame.K_F8:
                event_code += ' F8'
            elif e.key == pygame.K_F9:
                event_code += ' F9'
            elif e.key == pygame.K_F10:
                event_code += ' F10'
            elif e.key == pygame.K_F11:
                event_code += ' F11'
            elif e.key == pygame.K_F12:
                event_code += ' F12'
            elif e.key == pygame.K_1:
                event_code += ' 1'
            elif e.key == pygame.K_2:
                event_code += ' 2'
            elif e.key == pygame.K_3:
                event_code += ' 3'
            elif e.key == pygame.K_4:
                event_code += ' 4'
            elif e.key == pygame.K_5:
                event_code += ' 5'
            elif e.key == pygame.K_6:
                event_code += ' 6'
            elif e.key == pygame.K_7:
                event_code += ' 7'
            elif e.key == pygame.K_8:
                event_code += ' 8'
            elif e.key == pygame.K_9:
                event_code += ' 9'
            elif e.key == pygame.K_0:
                event_code += ' 0'
            elif e.key == pygame.K_BACKQUOTE:
                event_code += ' backquote'
            elif e.key == pygame.K_BACKSPACE:
                event_code += ' backspace'
            elif e.key == pygame.K_TAB:
                event_code += ' tab'
            elif e.key == pygame.K_CAPSLOCK:
                event_code += ' capslock'
            elif e.key in (pygame.K_RSHIFT, pygame.K_LSHIFT):
                event_code += ' shift'

                if e.key == pygame.K_RSHIFT:
                    event_code += ' right'
                else:
                    event_code += ' left'
            elif e.key in (pygame.K_RCTRL, pygame.K_LCTRL):
                event_code += ' ctrl'

                if e.key == pygame.K_RCTRL:
                    event_code += ' right'
                else:
                    event_code += ' left'
            elif e.key in (pygame.K_RALT, pygame.K_LALT):
                event_code += ' alt'

                if e.key == pygame.K_RCTRL:
                    event_code += ' right'
                else:
                    event_code += ' left'
            elif e.key == pygame.K_RETURN:
                event_code += ' enter'
            elif e.key == pygame.K_SLASH:
                event_code += ' slash'
            elif e.key == pygame.K_BACKSLASH:
                event_code += ' backslash'
            elif e.key == pygame.K_SPACE:
                event_code += ' space'
            elif e.key == pygame.K_q:
                event_code += ' q'
            elif e.key == pygame.K_w:
                event_code += ' w'
            elif e.key == pygame.K_e:
                event_code += ' e'
            elif e.key == pygame.K_r:
                event_code += ' r'
            elif e.key == pygame.K_t:
                event_code += ' t'
            elif e.key == pygame.K_y:
                event_code += ' y'
            elif e.key == pygame.K_u:
                event_code += ' u'
            elif e.key == pygame.K_i:
                event_code += ' i'
            elif e.key == pygame.K_o:
                event_code += ' o'
            elif e.key == pygame.K_a:
                event_code += ' a'
            elif e.key == pygame.K_s:
                event_code += ' s'
            elif e.key == pygame.K_d:
                event_code += ' d'
            elif e.key == pygame.K_f:
                event_code += ' f'
            elif e.key == pygame.K_g:
                event_code += ' g'
            elif e.key == pygame.K_h:
                event_code += ' h'
            elif e.key == pygame.K_j:
                event_code += ' j'
            elif e.key == pygame.K_k:
                event_code += ' k'
            elif e.key == pygame.K_l:
                event_code += ' l'
            elif e.key == pygame.K_z:
                event_code += ' z'
            elif e.key == pygame.K_x:
                event_code += ' x'
            elif e.key == pygame.K_c:
                event_code += ' c'
            elif e.key == pygame.K_v:
                event_code += ' v'
            elif e.key == pygame.K_b:
                event_code += ' b'
            elif e.key == pygame.K_n:
                event_code += ' n'
            elif e.key == pygame.K_m:
                event_code += ' m'
            elif e.key in (pygame.K_RIGHTBRACKET, pygame.K_LEFTBRACKET):
                event_code += ' bracket'

                if e.key == pygame.K_RIGHTBRACKET:
                    event_code += ' right'
                else:
                    event_code += ' left'
            elif e.key in (pygame.K_RIGHTPAREN, pygame.K_LEFTPAREN):
                event_code += ' paren'

                if e.key == pygame.K_RIGHTPAREN:
                    event_code += ' right'
                else:
                    event_code += ' left'
            elif e.key == pygame.K_QUOTE:
                event_code += ' quote'
            elif e.key == pygame.K_QUESTION:
                event_code += ' question'
            elif e.key == pygame.K_SEMICOLON:
                event_code += ' semicolon'
            elif e.key == pygame.K_COLON:
                event_code += ' colon'
            elif e.key == pygame.K_MINUS:
                event_code += ' minus'
            elif e.key == pygame.K_EQUALS:
                event_code += ' equals'
            elif e.key == pygame.K_PLUS:
                event_code += ' plus'
            elif e.key in (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP):
                event_code += ' arrow'

                if e.key == pygame.K_RIGHT:
                    event_code += ' right'
                elif e.key == pygame.K_LEFT:
                    event_code += ' left'
                elif e.key == pygame.K_DOWN:
                    event_code += ' down'
                else:
                    event_code += ' up'
            elif e.key == pygame.K_INSERT:
                event_code += ' insert'
            elif e.key == pygame.K_HOME:
                event_code += ' home'
            elif e.key in (pygame.K_PAGEUP, pygame.K_PAGEDOWN):
                event_code += ' page'

                if e.key == pygame.K_PAGEUP:
                    event_code += ' up'
                else:
                    event_code += ' down'
            elif e.key == pygame.K_DELETE:
                event_code += ' delete'
            elif e.key == pygame.K_END:
                event_code += ' end'
            elif e.key == pygame.K_SYSREQ:
                event_code += ' sysreq'
            elif e.key == pygame.K_SCROLLLOCK:
                event_code += ' scrolllock'
            elif e.key == pygame.K_NUMLOCK:
                event_code += ' numlock'
            elif e.key == pygame.K_NUMLOCKCLEAR:
                event_code += ' numlockclear'
        elif e.type in (pygame.TEXTINPUT, pygame.TEXTEDITING):
            event_code = 'text'

            if e.type == pygame.TEXTINPUT:
                event_code += ' input'
            else:
                event_code += ' editing'
        elif e.type == pygame.QUIT:
            event_code = 'quit'

        events.append(Event(event_code, e))


def post(event: Event) -> None:
    if isinstance(event, Event):
        events.append(event)
    else:
        raise TypeError(f'argument must be \'Event\', not \'{event.__class__.__name__}\'')


def get(event: supported_types = ...) -> List[Event]:
    if event is ... or isinstance(event, (str, Event)):
        if event is not ...:
            _events = []
            for e in events:
                if e == event:
                    _events.append(e)
            return _events

        return events
    else:
        raise TypeError(f'argument must be \'Event\' or \'str\', not \'{event.__class__.__name__}\'')


def inputed(event_code: str) -> bool:
    if isinstance(event_code, str):
        for e in events:
            if event_code in e:
                return True

        return False
    else:
        raise TypeError(f'argument must be \'str\', not \'{event_code.__class__.__name__}\'')


__all__ = [
    'Event',
    'input',
    'post',
    'get',
    'inputed'
]
