from utilities.math import Vector2, _pyi_Vector2_item_type
from pygame.cursors import Cursor
from typing import Union, List


position: Vector2
cursor: Union[Cursor]
visible: bool
mode: int
relative: Vector2
focused: bool
left_pressed: bool
middle_pressed: bool
right_pressed: bool


def __getitem__(item: Union[slice, int]) -> Union[List[Union[float, int]], float, int]:...
def __setitem__(self, key: Union[slice, int], value: _pyi_Vector2_item_type):...
def flip() -> None:...
