from functools import partial
from operator import mul


def multiplier(a):
    return partial(mul, a)


mul2 = multiplier(2)
print(mul2(3))
