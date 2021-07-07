from typing import Tuple, Union, Any
from pygame.cursors import Cursor


pos: Tuple[int, int]
x: int
y: int
cursor: Union[Cursor, int]
visible: bool
mode: int
rel: Tuple[int, int]
focused: bool


def __getitem__(item) -> Any:...
def flip() -> None:...
