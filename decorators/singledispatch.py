import functools
from typing import Never


@functools.singledispatch
def base_converter(obj: object) -> str:
    string = str(obj)
    return string


@base_converter.register
def int_converter(num: int) -> str:
    string = str(num + 1)
    return string


@base_converter.register
def list_converter(lst: list) -> str:
    lst_copy = lst.copy()
    lst_copy.extend([5, 6])
    string = str(lst_copy)
    return string


print(base_converter(0))  # Handled by `int_converter`
print(base_converter([1, 3]))  # Handled by `list_converter`
print(base_converter((1, 9)))  # Handled by `base_converter` because it hasn't own and simillar type handler
