from time import time

_fps = 0
fps_last_time = 0


fps = 60
dt = 0


data = {}


def passed(secs: float, id: str) -> bool:
    if id not in data:
        data[id] = time()
        return False

    if (time() - data[id]) >= secs:
        data[id] = time()
        return True

    return False


def remove_passed(id: str):
    if id in data:
        del data[id]


def flip():
    global fps_last_time, fps, _fps, dt

    _fps += 1
    if time() - fps_last_time >= 1:
        fps = _fps
        _fps = 0
        fps_last_time = time()

    dt = 1 / fps * 10


__all__ = (
    'fps',
    'dt',
    'passed',
    'remove_passed',
    'flip'
)
