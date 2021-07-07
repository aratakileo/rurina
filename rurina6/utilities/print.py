from pygame.color import Color
from pygame import error


END = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
FILLED_BG = '\033[7m'
CROSSOUT = '\033[9m'
BOLD_UNDERLINE = '\033[21m'
HALF_BOLD = '\033[30m'
RED = '\033[31m'
LIGHT_GREEN = '\033[32m'
LIGHT_YELLOW = '\033[33m'
BLUE = '\033[34m'
LIGHT_PURPLE1 = '\033[35m'
TEAL = '\033[36m'
LIGHT_GREY = '\033[37m'
WHITE_BG = '\033[40m'
PINK1_BG = '\033[41m'
LIME1_BG = '\033[42m'
LIGHT_YELLOW_BG = '\033[43m'
CYAN_BG = '\033[44m'
LIGHT_PURPLE_BG = '\033[45m'
TEAL_BG = '\033[46m'
LIGHT_GREY_BG = '\033[47m'
BORDER = '\033[51m'
CIRCULAR_BORDER = '\033[52m'
GREY = '\033[90m'
PINK = '\033[91m'
LIME = '\033[92m'
YELLOW = '\033[93m'
CYAN1 = '\033[94m'
LIGHT_PURPLE = '\033[95m'
CYAN = '\033[96m'
DARK_GREY = '\033[97m'
GREY_BG = '\033[100m'
PINK_BG = '\033[101m'
LIME_BG = '\033[102m'
YELLOW_BG = '\033[103m'
LIGHT_CYAN1_BG = '\033[104m'
LIGHT_PINK_BG = '\033[105m'
LIGHT_CYAN_BG = '\033[106m'
DARK_GREY_BG = '\033[107m'


def rgb(r: int, g: int, b: int) -> str:
    return f'\033[38;2;{r};{g};{b}m'


def hex(_hex: str) -> str:
    if _hex.count('#') == 0:
        _hex = '#' + _hex

    if len(_hex) != 7:
        return END

    try:
        return rgb(*Color(_hex)[:3])
    except error:
        return END


def formatted_print(mode: str, *args, **kwargs):
    if len(args) > 0:
        args = list(args)
        args[0] = mode + str(args[0])
        args[-1] = str(args[-1]) + END
    print(*args, **kwargs)


def printwarning(*args, **kwargs):
    formatted_print(YELLOW, *args, **kwargs)


def printerror(*args, **kwargs):
    formatted_print(RED, *args, **kwargs)


__all__ = (
    'rgb',
    'hex',
    'formatted_print',
    'printwarning',
    'printerror',
    'END',
    'BOLD',
    'ITALIC',
    'UNDERLINE',
    'FILLED_BG',
    'CROSSOUT',
    'BOLD_UNDERLINE',
    'HALF_BOLD',
    'RED',
    'LIGHT_GREEN',
    'LIGHT_YELLOW',
    'BLUE',
    'LIGHT_PURPLE1',
    'TEAL',
    'LIGHT_GREY',
    'WHITE_BG',
    'PINK1_BG',
    'LIME1_BG',
    'LIGHT_YELLOW_BG',
    'CYAN_BG',
    'LIGHT_PURPLE_BG',
    'TEAL_BG',
    'LIGHT_GREY_BG',
    'BORDER',
    'CIRCULAR_BORDER',
    'GREY',
    'PINK',
    'LIME',
    'YELLOW',
    'CYAN1',
    'LIGHT_PURPLE',
    'CYAN',
    'DARK_GREY',
    'GREY_BG',
    'PINK_BG',
    'LIME_BG',
    'YELLOW_BG',
    'LIGHT_CYAN1_BG',
    'LIGHT_PINK_BG',
    'LIGHT_CYAN_BG',
    'DARK_GREY_BG',
)
