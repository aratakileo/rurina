from textwrap import dedent
import traceback
import re


def camel_to_snake(value: str) -> str:
    """
    camel_to_snake("CamelToSnake") # camel_to_snake
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def snake_to_camel(value: str) -> str:
    """
    snake_to_camel("snake_to_camel") # SnakeToCamel
    """
    words = value.split('_')
    value = ''
    for w in words:
        value += w.title()
    return value


def replace(old: str, _dict: dict) -> str:
    """
    Given a string and a dict, replaces occurrences of the dict keys found in the
    string, with their corresponding values. The replacements will occur in "one pass",
    i.e. there should be no clashes.
    :param str old: string to perform replacements on
    :param dict _dict: replacement dictionary {str_to_find: str_to_replace_with}
    :rtype: str the replaced string
    """
    for key in _dict:
        old = old.replace(key, _dict[key])

    return old


def printvar(var):
    print(traceback.extract_stack(limit=2)[0][3][9:][:-1], "=", var)


def printwarning(*args, **kwargs):
    if len(args) > 0:
        args = list(args)
        args[0] = '\033[93m' + str(args[0])
        args[-1] = str(args[-1]) + '\033[0m'
    print(*args, **kwargs)


def printerror(*args, **kwargs):
    if len(args) > 0:
        args = list(args)
        args[0] = '\033[91m' + str(args[0])
        args[-1] = str(args[-1]) + '\033[0m'
    print(*args, **kwargs)


__all__ = (
    'camel_to_snake',
    'snake_to_camel',
    'replace',
    'printvar',
    'printwarning',
    'printerror',
    'dedent'
)


if __name__ == '__main__':
    print(camel_to_snake('CamelToSnake'))
    print(snake_to_camel('snake_to_camel'))

    var = 'test'
    printvar(var)
    printwarning('Warning')
    printerror('Error')

    print(replace('three two five four six', {'three': 'one', 'five': 'three', 'six': 'five'}))

    text = '''\
    hello
     word
    '''
    print(repr(text))
    print(repr(dedent(text)))
