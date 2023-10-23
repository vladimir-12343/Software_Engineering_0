import math


def SquareHeron(a, b, c):
    p = (a + b + c) / 2
    square = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return square
