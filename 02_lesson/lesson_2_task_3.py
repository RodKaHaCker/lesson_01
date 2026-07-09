import math


def square(side):
    area = side * side
    if side % 1 != 0:
        return math.ceil(area)
    return area


print(square(5))
print(square(2.5))
print(square(3.3))
print(square(4.0))
