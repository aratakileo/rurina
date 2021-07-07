from typing import Union, List, Dict
from error import ActionError
import event


def get_list(value):
    if isinstance(value, str):
        value = [value]

    for i in range(len(value)):
        value[i] = value[i]\
            .replace('mouse button down', 'mouse button')\
            .replace('mouse button up', 'mouse button')\
            .replace('key down', 'key')\
            .replace('key up', 'key')

    return value


actions = {
    'quit': ['key escape']
}


data = {
    # ['action_name', action_index]: [True, False]
}


def set_action(action_name: Union[str, int], action: Union[str, List[str]]) -> None:
    if isinstance(action_name, (str, int)):
        if isinstance(action, (str, list)):
            actions[str(action_name)] = get_list(str(action))
        else:
            raise TypeError(f'argument 2 must be \'str\' or \'list\', not \'{action.__class__.__name__}\'')
    else:
        raise TypeError(f'argument 1 must be \'int\' or \'str\', not \'{action_name.__class__.__name__}\'')


def append_action(action_name: Union[str, int], action: Union[str, List[str]]) -> None:
    if isinstance(action_name, (str, int)):
        if isinstance(action, (str, list)):
            action_name = str(action_name)
            if action_name in actions:
                actions[action_name] = actions[action_name] + get_list(action)
            else:
                raise ActionError(f'action \'{action_name}\' is not defined')
        else:
            raise TypeError(f'argument 2 must be \'str\' or \'list\', not \'{action.__class__.__name__}\'')
    else:
        raise TypeError(f'argument 1 must be \'int\' or \'str\', not \'{action_name.__class__.__name__}\'')


def remove_action(action_name: Union[str, int]) -> None:
    if isinstance(action_name, (str, int)):
            action_name = str(action_name)
            if action_name in actions:
                del actions[action_name]
            else:
                raise ActionError(f'action \'{action_name}\' is not defined')
    else:
        raise TypeError(f'argument must be \'int\' or \'str\', not \'{action_name.__class__.__name__}\'')


def get_actions() -> Dict[str, List[str]]:
    return actions.copy()


def input():
    pass


__all__ = [
    'set_action',
    'append_action',
    'remove_action',
    'get_actions'
]
