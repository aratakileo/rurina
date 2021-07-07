from pygame.mouse import get_pressed as get_buttonspressed
from pygame.key import get_pressed as get_keyspressed
from event import get, fullname, keycode, buttoncode
from typing import Sequence, Union, Tuple


actions = {}
"""actions = {
    'action_name': {
        'event1event2' : {
            'event1': [
                type: int,
                status: bool,
                last_status: bool,
                inverse_event: Union[str, None]
            ],
            'event2': [0, True, False, None]
        }
    }
}"""


PROCESSING_EVENT = 0
PROCESSING_KEY = 1
PROCESSING_BUTTON = 2


def addaction(name: str):
    if name not in actions:
        actions[name] = {}


def removeaction(name: str):
    if name in actions:
        del actions[name]


def haveaction(name: str) -> bool:
    return name in actions


def actionstatus(name: str) -> bool:
    if name not in actions:
        return False

    returned_bool = False

    for _ in actions[name]:
        returned_bool = returned_bool or processingstatus(name, _)

        if returned_bool:
            return True

    return returned_bool


def last_actionstatus(name: str) -> bool:
    if name not in actions:
        return False

    returned_bool = False

    for _ in actions[name]:
        returned_bool = returned_bool or last_processingstatus(name, _)

        if returned_bool:
            return True

    return returned_bool


def _processing(name: Union[Sequence[str], str]) -> Tuple[Sequence[str], str]:
    if isinstance(name, str):
        name = (name,)

    return name, ''.join(name)


def setprocessing(
        action_name: str,
        name: Union[Sequence[str], str],
        inverse_name: Union[Sequence[str], str] = None,
        type: int = PROCESSING_EVENT
):
    addaction(action_name)

    if isinstance(inverse_name, str) or inverse_name in (None, ...):
        inverse_name = (inverse_name, )

    name, hashable_name = _processing(name)

    actions[action_name][hashable_name] = {}

    for i in range(len(name)):
        actions[action_name][hashable_name][name[i]] = [type, False, False, inverse_name[i]]


def removeprocessing(action_name: str, name: Union[Sequence[str], str]):
    if haveprocessing(action_name, name):
        del actions[action_name][_processing(name)[1]]


def haveprocessing(action_name: str, name: Union[Sequence[str], str]) -> bool:
    return action_name in actions and _processing(name)[1] in actions[action_name]


def _processingstatus(action_name: str, name: Union[Sequence[str], str], index: int) -> bool:
    if not haveprocessing(action_name, name):
        return False

    name, hashable_name = _processing(name)
    returned_bool = True

    for _ in name:
        returned_bool = returned_bool and actions[action_name][hashable_name][_][index]

        if not returned_bool:
            return False

    return returned_bool


def processingstatus(action_name: str, name: Union[Sequence[str], str]) -> bool:
    return _processingstatus(action_name, name, 1)


def last_processingstatus(action_name: str, name: Union[Sequence[str], str]) -> bool:
    return _processingstatus(action_name, name, 2)


def setevent(action_name: str, name: Union[Sequence[str], str], inverse_name: Union[Sequence[str], str] = None):
    setprocessing(action_name, name, inverse_name)


def flip():
    event_buffer = get(False)

    for action_name in actions:
        for hashable_processingname in actions[action_name]:
            for processingname in actions[action_name][hashable_processingname]:
                processing = actions[action_name][hashable_processingname][processingname]

                processing[2] = processing[1]

                if processing[-1] in (None, ...):
                    processing[1] = False

                if processing[0] == PROCESSING_EVENT:
                    for e in event_buffer:
                        event_fullname = fullname(e)
                        if (processingname + ' ') in event_fullname or (str(processing[-1]) + ' ') in event_fullname:
                            if processing[-1] not in (None, ...):
                                if (processingname + ' ') in event_fullname:
                                    processing[1] = True

                                if (processing[-1] + ' ') in event_fullname:
                                    processing[1] = False
                            elif (processingname + ' ') in event_fullname:
                                processing[1] = True
                elif processing[0] == PROCESSING_KEY:
                    processing[1] = bool(get_keyspressed()[keycode(processingname)])
                elif processing[0] == PROCESSING_BUTTON:
                    processing[1] = bool(get_buttonspressed()[buttoncode(processingname) - 1])

                actions[action_name][hashable_processingname][processingname] = processing

    print(actions)


__all__ = (
    'addaction',
    'removeaction',
    'haveaction',
    'actionstatus',
    'last_actionstatus',
    'setprocessing',
    'removeprocessing',
    'haveprocessing',
    'processingstatus',
    'last_processingstatus',
    'setevent',
    'flip',
    'PROCESSING_EVENT',
    'PROCESSING_KEY',
    'PROCESSING_BUTTON'
)
