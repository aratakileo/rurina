from typing import Union, Sequence
import event


_actions = {}
"""_actions = {
    'action_name': {
        'event1event2': 
            {
                'event1': ...,
                'event2': ...
            }
    }
}"""


def addaction(name: str):
    if name not in _actions:
        _actions[name] = {}


def removeaction(name: str):
    if name in _actions:
        del _actions[name]


def haveaction(name: str) -> bool:
    return name in _actions


def _action_status(name: str, index: int) -> bool:
    if name not in _actions:
        return False

    returned_bool = False

    for hashable_event_fullname in _actions[name]:
        event_fullname = list(_actions[name][hashable_event_fullname].keys())
        returned_bool = returned_bool or _eventstatus(name, event_fullname, index)

        if returned_bool:
            return True

    return returned_bool


def actionstatus(name: str) -> bool:
    return _action_status(name, 1)


def last_actionstatus(name: str) -> bool:
    return _action_status(name, 2)


def _event(event_fullname: Union[Sequence[str], str]):
    if isinstance(event_fullname, str):
        event_fullname = [event_fullname]

    return event_fullname, ''.join(event_fullname)


def setevent(
        action_name: str,
        event_fullname: Union[Sequence[str], str],
        inverse_event_fullname: Union[Sequence[str], str] = None
):
    addaction(action_name)

    event_fullname, hashable_event_fullname = _event(event_fullname)

    if inverse_event_fullname is None or isinstance(inverse_event_fullname, str):
        inverse_event_fullname = [inverse_event_fullname] * len(event_fullname)

    if hashable_event_fullname not in _actions[action_name]:
        _actions[action_name][hashable_event_fullname] = {}

    for i in range(len(event_fullname)):
        _actions[action_name][hashable_event_fullname][event_fullname[i]] = [inverse_event_fullname[i], False, False]


def remove_event(action_name: str, event_fullname: Union[Sequence[str], str]):
    event_fullname, hashable_event_fullname = _event(event_fullname)

    for _event_fullname in event_fullname:
        if have_event(action_name, _event_fullname):
            del _actions[action_name][hashable_event_fullname][_event_fullname]


def have_event(action_name: str, event_fullname: Union[Sequence[str], str]) -> bool:
    event_fullname, hashable_event_fullname = _event(event_fullname)

    returned_bool = True

    for _event_fullname in event_fullname:
        returned_bool = returned_bool \
                        and action_name in _actions \
                        and hashable_event_fullname in _actions[action_name] \
                        and _event_fullname in _actions[action_name][hashable_event_fullname]

        if not returned_bool:
            return False

    return returned_bool


def _eventstatus(action_name: str, event_fullname: Union[Sequence[str], str], index: int) -> bool:
    event_fullname, hashable_event_fullname = _event(event_fullname)

    returned_bool = True

    for _event_fullname in event_fullname:
        returned_bool = returned_bool \
                        and have_event(action_name, event_fullname) \
                        and _actions[action_name][hashable_event_fullname][_event_fullname][index]

        if not returned_bool:
            return False

    return returned_bool


def eventstatus(action_name: str, event_fullname: Union[Sequence[str], str]) -> bool:
    return _eventstatus(action_name, event_fullname, 1)


def last_eventstatus(action_name: str, event_fullname: Union[Sequence[str], str]) -> bool:
    return _eventstatus(action_name, event_fullname, 2)


def flip():
    event_buffer = event.get(False)
    for action_name in _actions:
        for event_fullname in _actions[action_name]:
            hashable_event_fullname = ''.join(event_fullname)
            for _event_fullname in _actions[action_name][hashable_event_fullname]:
                action_event = _actions[action_name][hashable_event_fullname][_event_fullname]

                action_event[2] = action_event[1]

                if action_event[0] is None:
                    action_event[1] = False

                for e in event_buffer:
                    fullname = event.fullname(e)

                    if action_event[0] is None and (_event_fullname + ' ') in fullname:
                        action_event[1] = True
                    elif action_event[0] is not None:
                        if (_event_fullname + ' ') in fullname:
                            action_event[1] = True
                        elif (action_event[0] + ' ') in fullname:
                            action_event[1] = False


__all__ = (
    'addaction',
    'removeaction',
    'haveaction',
    'actionstatus',
    'last_actionstatus',
    'setevent',
    'remove_event',
    'have_event',
    'eventstatus',
    'last_eventstatus',
    'flip',
)
