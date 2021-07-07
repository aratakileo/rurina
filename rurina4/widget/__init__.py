from widget.edittext import EditText
from widget.widget import flip
from input.inputmap import add
from widget.text import Text


add('ui_copy', 'ctrl+c')
add('ui_paste', 'ctrl+v')
add('ui_select_all', 'ctrl+a')
add('ui_shift', 'shift')
add('ui_left', 'arrow left')
add('ui_right', 'arrow right')
add('ui_up', 'arrow up')
add('ui_down', 'arrow down')
add('ui_backspace', 'backspace')
add('ui_backspace', 'delete')
add('ui_page_up', 'page up')
add('ui_page_down', 'page down')


__all__ = (
    'Text',
    'EditText',
    'flip'
)
