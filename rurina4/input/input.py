from input.inputmap import status


data = {}


def is_action_pressed(name: str) -> bool:
    returned_bool = status(name)
    data[name] = returned_bool
    return returned_bool


def is_action_released(name: str) -> bool:
    last_status = status(name)
    returned_bool = name in data and data[name] and not last_status
    data[name] = last_status
    return returned_bool


def is_action_just_pressed(name: str) -> bool:
    last_status = status(name)
    returned_bool = name in data and not data[name] and last_status
    data[name] = last_status
    return returned_bool


__all__ = (
    'is_action_pressed',
    'is_action_released',
    'is_action_just_pressed'
)
