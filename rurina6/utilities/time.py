from time import time
import sys


_timers = {}
fps, _fps = 60, 0
dt = 0


def timer_passed(secs: float, name: str, auto_update: bool = True) -> bool:
    if name not in _timers:
        update_timer(name)
        return False

    if (time() - _timers[name]) >= secs:
        if auto_update: update_timer(name)
        return True

    return False


def update_timer(name: str):
    _timers[name] = time()


def remove_timer(name: str):
    if name in _timers:
        del _timers[name]


def flip():
    global _fps, fps, dt

    if timer_passed(1, f'{id(sys.modules[__name__])}:fps-counter'):
        fps = _fps + 1
        _fps = 0
    else:
        _fps += 1

    dt = 1 / fps * 10


__all__ = (
    'timer_passed',
    'update_timer',
    'remove_timer',
    'flip',
    'fps',
    'dt',
)
