from os import path as _path
from typing import List


def file_exists(path: str, types: List[str] = [], without_type: bool = True) -> bool:
    path = _path.abspath(path)
    name = _path.basename(path)
    if without_type and _path.isfile(path):
        return True

    if '.' in name:
        end = name.split('.')[-1]
        if end in types:
            return _path.isfile(path)

    for _ in types:
        __path = path + '.' + _
        if _path.isfile(__path):
            return True

    return False


def file_path(path: str, types: List[str] = [], without_type: bool = True) -> str:
    path = _path.abspath(path)
    if not file_exists(path, types, without_type):
        raise FileNotFoundError(f'No such file or directory: \'{path}\'')

    name = _path.basename(path)
    if '.' in name:
        end = name.split('.')[-1]
        if end in types and _path.isfile(path):
            return path

    for _ in types:
        __path = path + '.' + _
        if _path.isfile(__path):
            return __path

    return path


__all__ = (
    'file_exists',
    'file_path'
)
