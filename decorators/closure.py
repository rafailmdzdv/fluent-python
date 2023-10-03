from typing import Callable


def closure() -> Callable[[], str]:
    string1 = 'World'

    def wrapper() -> str:
        string2 = 'Hello'
        return f'{string2}, {string1}'

    return wrapper


clos = closure()
print(clos.__code__.co_varnames)  # Variables from `wrapper`
print(clos.__code__.co_freevars)  # Variables from `closure` body which are using in `wrapper` body
# Variables from `closure` whore are using in `wrapper` body; value of this variable
print(clos.__closure__, clos.__closure__[0].cell_contents)  # type: ignore

