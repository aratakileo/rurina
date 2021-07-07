from math import sqrt


def distance(x0, y0, x1, y1) -> float:
    return sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)


def move_negativity(num1, num2):
    if (num2 < 0 and num1 < 0) or (num2 > 0 and num1 > 0) or (num2 == 0):
        return num1

    return -num1


def num_in_interval(num, min, max) -> bool:
    return min <= num <= max


def num_by_interval(num, min, max) -> float:
    if num < min:
        return min

    if num > max:
        return max

    return num


__all__ = [
    'distance',
    'move_negativity',
    'num_in_interval',
    'num_by_interval'
]

if __name__ == '__main__':
    print(move_negativity(30, -4))
