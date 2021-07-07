from .key import *
from .map import *


setevent('ui_quit', 'quit')
setkey('ui_quit', 'escape')


_flip = flip


def flip(_quit: bool = True):
    _flip()

    if _quit and actionstatus('ui_quit'):
        quit()
