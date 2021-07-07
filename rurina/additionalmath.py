from math import sqrt


def distance(x0, y0, x1, y1):
    return sqrt(
        (x0 - x1) ** 2
        +
        (y0 - y1) ** 2
    )


__all__ = ['distance']
