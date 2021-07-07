from pygame import display
from ctypes import windll


_show = windll.user32.MessageBoxW


TYPE_OK = 0x00000000
TYPE_OKCANCEL = 0x00000001
TYPE_ABORTRETRYIGNORE = 0x00000002
TYPE_YESNOCANCEL = 0x00000003
TYPE_YESNO = 0x00000004
TYPE_RETRYCANCEL = 0x00000005
TYPE_CANCELTRYCONTINUE = 0x00000006
TYPE_HELP = 0x00004000


ICON_NONE = 0x00000000
ICON_ERROR = 0x00000010
ICON_QUESTION = 0x00000020
ICON_WARNING = 0x00000030
ICON_INFORMATION = 0x00000040


MODE_DEFAULT = 0x00000000
MODE_RIGHT = 0x00080000
MODE_RTLREADING = 0x00100000
MODE_SERVICE_NOTIFICATION = 0x00200000


VALUE_ERROR = 0
VALUE_OK = 1
VALUE_CANCEL = 2
VALUE_ABORT = 3
VALUE_RETRY = 4
VALUE_IGNORE = 5
VALUE_YES = 6
VALUE_NO = 7
VALUE_TRYAGAIN = 10
VALUE_CONTINUE = 11


def show(
        title: str = ...,
        message: str = ...,
        type: int = TYPE_OK,
        icon: int = ICON_NONE,
        mode: int = MODE_DEFAULT,
        selected_button: int = 0
) -> int:
    if title in (None, ...):
        title = '' if len(display.get_caption()) == 0 else display.get_caption()[0]

    if message in (None, ...):
        message = ''

    selected_button = abs(selected_button)
    if selected_button == 1:
        selected_button = 0x00000100
    elif selected_button == 2:
        selected_button = 0x00000200
    elif selected_button == 3:
        selected_button = 0x00000300
    else:
        selected_button = 0x00000000

    return _show(0, message, title, type | icon | selected_button | mode)


def showinfo(title: str = ..., message: str = ..., *options, **koptions) -> int:
    return show(title, message, TYPE_OK, ICON_INFORMATION, *options, **koptions)


def showwarning(title: str = ..., message: str = ..., *options, **koptions) -> int:
    return show(title, message, TYPE_OK, ICON_WARNING, *options, **koptions)


def showerror(title: str = ..., message: str = ..., *options, **koptions) -> int:
    return show(title, message, TYPE_OK, ICON_ERROR, *options, **koptions)


def askquestion(title: str = ..., message: str = ..., *options, **koptions) -> int:
    return show(title, message, TYPE_YESNO, ICON_QUESTION, *options, **koptions)


def askokcancel(title: str = ..., message: str = ..., *options, **koptions) -> int:
    return show(title, message, TYPE_OKCANCEL, ICON_QUESTION, *options, **koptions)


def askyesno(title: str = ..., message: str = ..., *options, **koptions) -> int:
    return show(title, message, TYPE_YESNO, ICON_QUESTION, *options, **koptions)


def askyesnocancel(title: str = ..., message: str = ..., *options, **koptions) -> int:
    return show(title, message, TYPE_YESNOCANCEL, ICON_QUESTION, *options, **koptions)


def askretrycancel(title: str = ..., message: str = ..., *options, **koptions) -> int:
    return show(title, message, TYPE_RETRYCANCEL, ICON_WARNING, *options, **koptions)


__all__ = (
    'show',
    'showinfo',
    'showwarning',
    'showerror',
    'askquestion',
    'askokcancel',
    'askyesno',
    'askyesnocancel',
    'askretrycancel',
    'TYPE_OK',
    'TYPE_OKCANCEL',
    'TYPE_ABORTRETRYIGNORE',
    'TYPE_YESNOCANCEL',
    'TYPE_YESNO',
    'TYPE_RETRYCANCEL',
    'TYPE_CANCELTRYCONTINUE',
    'TYPE_HELP',
    'ICON_NONE',
    'ICON_ERROR',
    'ICON_QUESTION',
    'ICON_WARNING',
    'ICON_INFORMATION',
    'MODE_DEFAULT',
    'MODE_RIGHT',
    'MODE_RTLREADING',
    'MODE_SERVICE_NOTIFICATION',
    'VALUE_ERROR',
    'VALUE_OK',
    'VALUE_CANCEL',
    'VALUE_ABORT',
    'VALUE_RETRY',
    'VALUE_IGNORE',
    'VALUE_YES',
    'VALUE_NO',
    'VALUE_TRYAGAIN',
    'VALUE_CONTINUE'
)


if __name__ == "__main__":
    print("info", showinfo("Spam", "Egg Information"))
    print("warning", showwarning("Spam", "Egg Warning"))
    print("error", showerror("Spam", "Egg Alert"))
    print("question", askquestion("Spam", "Question?"))
    print("proceed", askokcancel("Spam", "Proceed?"))
    print("yes/no", askyesno("Spam", "Got it?"))
    print("yes/no/cancel", askyesnocancel("Spam", "Want it?"))
    print("try again", askretrycancel("Spam", "Try again?"))
