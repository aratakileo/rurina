from typing import Union, Sequence
from re import sub
import traceback


def class_output(
        object,
        name: str = None,
        hide_protected: bool = True,
        output_properties: Union[Sequence[str], str] = (),
        remove_attributes: Union[Sequence[str], str] = ()
) -> str:
    _dict = object.__dict__.copy()

    if hide_protected:
        for key in _dict.copy():
            if key.startswith('_'):
                del _dict[key]

    if isinstance(output_properties, str):
        output_properties = (output_properties, )

    for attr in output_properties:
        _dict[attr] = getattr(object, attr)

    if isinstance(remove_attributes, str):
        remove_attributes = (remove_attributes, )

    for attr in remove_attributes:
        del _dict[attr]

    name = f'{name} => ' if name not in (None, ..., '') else ''
    _dict = f'{_dict}' if len(_dict) > 0 or name != '' else ''

    return f'<{object.__class__.__name__}({name}{_dict})>'


def short_class_output(object, name: str = None) -> str:
    name = f'{name} => {{...}}' if name not in (None, ..., '') else '...'
    return f'<{object.__class__.__name__}({name})>'


def varname(var) -> str:
    _data = traceback.extract_stack(limit=2)[0][3]
    _data = _data[_data.index(f'{varname.__name__}(') + len(varname.__name__) + 1:]
    return _data[:_data.index(')')].strip(' ')


def camel_to_snake(value):
    s1 = sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
    return sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def snake_to_camel(value):
    camel = ''
    words = value.split('_')
    for w in words:
        camel += w.title()
    return camel


__all__ = (
    'class_output',
    'short_class_output',
    'varname',
    'camel_to_snake',
    'snake_to_camel',
)


if __name__ == '__main__':
    print(class_output(Sequence[tuple]))
    print(class_output(Sequence[list], 'Test'))
    print(short_class_output(''))
    print(short_class_output('', 'name'))
    abcdef = 0
    print(varname(abcdef))
    print(camel_to_snake('CamelToSnake'))
    print(snake_to_camel('snake_to_camel'))
