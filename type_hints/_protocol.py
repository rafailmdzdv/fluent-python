from typing import Protocol, TypeVar


class Multipliable(Protocol):
    def __mul__(self, x):
        pass


class NonMultipliable:

    pass


MultiplyT = TypeVar('MultiplyT', bound=Multipliable)


def double(x: MultiplyT) -> MultiplyT:
    return x * 2


print(double(4))
print(double(4.5))
print(double('a'))
print(double(NonMultipliable()))  # Mypy throws an error
