from constants import BAR_STEP, BAR_MIN_VALUE, BAR_MAX_VALUE, BAR_VALUE
from prefabs.inputter import *
from widgets.widget import WidgetByRect
import pygame


class Bar(WidgetByRect):
    def __init__(
            self,
            *args,
            step: float = 0.1,
            min_value: float = 0.0,
            max_value: float = 100.0,
            value: float = 0.0,
            color=(0, 0, 0),
            progress_color=pygame.Color('green'),
            **kwargs
    ):
        super().__init__(*args, color=color, **kwargs)
        self.__data__ = [1.0, 0.0, 100.0, 0.0]
        self.step = step
        self.min_value, self.max_value = min_value, max_value
        self.value = value
        self.progress_color = progress_color

    def __str__(self):
        return f'{self.name}: {self.absolute_value}/{self.min_to_max_value_difference} - {self.percent_value}%'

    def __repr__(self):
        return str(self)

    def fix_data(self):
        step = abs(self.__data__[BAR_STEP])
        min_value = self.__data__[BAR_MIN_VALUE]
        max_value = self.__data__[BAR_MAX_VALUE]
        value = self.__data__[BAR_VALUE]

        if min_value > max_value:
            min_value = max_value

        if step > max_value - min_value:
            step = max_value - min_value

        if value < min_value:
            value = min_value

        if value > max_value:
            value = max_value

        if step != 0 and value != 0:
            mod = value % step

            if mod != 0:
                value -= mod
                value += step if mod > step / 2 else 0

        self.__data__[BAR_STEP] = float(step)
        self.__data__[BAR_MIN_VALUE] = float(min_value)
        self.__data__[BAR_MAX_VALUE] = float(max_value)
        self.__data__[BAR_VALUE] = float(value)

    @property
    def step(self) -> float:
        return self.__data__[BAR_STEP]

    @step.setter
    def step(self, value):
        self.__data__[BAR_STEP] = value
        self.fix_data()

    @property
    def min_value(self) -> float:
        return self.__data__[BAR_MIN_VALUE]

    @min_value.setter
    def min_value(self, value):
        self.__data__[BAR_MIN_VALUE] = value
        self.fix_data()

    @property
    def max_value(self) -> float:
        return self.__data__[BAR_MAX_VALUE]

    @max_value.setter
    def max_value(self, value):
        self.__data__[BAR_MAX_VALUE] = value
        self.fix_data()

    @property
    def value(self) -> float:
        return self.__data__[BAR_VALUE]

    @value.setter
    def value(self, _value):
        self.__data__[BAR_VALUE] = _value
        self.fix_data()

    @property
    def absolute_value(self) -> float:
        return self.value - self.min_value

    @absolute_value.setter
    def absolute_value(self, value):
        self.value = value + self.min_value

    @property
    def min_to_max_value_difference(self) -> float:
        return self.max_value - self.min_value

    @min_to_max_value_difference.setter
    def min_to_max_value_difference(self, value):
        half = (self.min_to_max_value_difference - value) / 2
        self.min_value += half
        self.max_value -= half

    @property
    def percent_value(self) -> int:
        return int(self.absolute_value / self.min_to_max_value_difference * 100)

    @percent_value.setter
    def percent_value(self, value):
        self.absolute_value = self.min_to_max_value_difference * float(value) / 100.0

    @property
    def step_width(self) -> float:
        piece = self.min_to_max_value_difference

        if self.step > 0:
            piece /= self.step

        return self.rect.width / piece

    @property
    def value_width(self) -> float:
        if self.step > 0:
            return self.absolute_value / self.step * self.step_width

        return self.absolute_value * self.step_width

    @value_width.setter
    def value_width(self, value):
        self.absolute_value = value / self.rect.width * self.min_to_max_value_difference


__all__ = [
    'Bar'
]
