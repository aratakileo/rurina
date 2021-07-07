from platform import system
from ctypes import WinDLL


_user32dll = WinDLL("User32.dll")


CAPITAL = 0x14
SCROLL = 0x91
NUMLOCK = 0x90


def state(key: int) -> bool:
    if system() != 'Windows':
        return False

    return _user32dll.GetKeyState(key) == 1


__all__ = (
    'state',
    'CAPITAL',
    'SCROLL',
    'NUMLOCK'
)
