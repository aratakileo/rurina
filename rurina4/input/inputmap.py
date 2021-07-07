from event import get, code_combination, code_type
from typing import List


data = {}
saved_data = {}


# TODO: append data_type


def add_action(name: str):
    if name in data:
        return

    data[name] = []
    saved_data[name] = []


def remove_action(name: str):
    if name in data:
        return

    del data[name]
    del saved_data[name]


def have_action(name: str) -> bool:
    return name in data


def add(action_name: str, code: str):
    if action_name not in data:
        add_action(action_name)

    if have(action_name, code):
        return

    code = code_combination(code)

    data[action_name].append(code)
    saved_data[action_name].append([False] * len(code))


def remove(action_name: str, code: str):
    if not have(action_name, code):
        return

    code = code_combination(code)

    del saved_data[action_name][data[action_name].index(code)]
    data[action_name].remove(code)


def have(action_name: str, code: str) -> bool:
    return action_name in data and code_combination(code) in data[action_name]


def _status(_list: List[bool], _and: bool = False) -> bool:
    if _and:
        returned_bool = True

        for _ in _list:
            returned_bool = returned_bool and _

        return returned_bool

    returned_bool = False
    for _ in _list:
        returned_bool = returned_bool or (_status(_, True) if isinstance(_, list) else _)

    return returned_bool


def status(action_name: str, code: str = ...) -> bool:
    if code in (None, ...):
        return _status(saved_data[action_name])
    
    return _status(saved_data[action_name][data[action_name].index(code_combination(code))], True)


def flip():
    for key in data:
        for i in range(len(data[key])):
            action_code = data[key][i]
            for k in range(len(action_code)):
                for e in get(False):
                    if action_code[k] in e.code[len(code_type(e)) + 1:]:
                        saved_data[key][i][k] = 'key down' in e or 'key numpad down' in e or 'mouse button down' in e


__all__ = (
    'add_action',
    'remove_action',
    'have_action',
    'add',
    'remove',
    'have',
    'status',
    'flip'
)
