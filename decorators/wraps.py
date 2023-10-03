import functools
from typing import Callable


def decorator1(func: Callable[..., str]) -> Callable[..., str]:

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> str:
        """`Wraps` copying args from decorated func to closure"""
        print(f'{args}, {kwargs}')  # Prints args from `decorated_func`
        return func(*args, **kwargs)

    return wrapper


@decorator1
def decorated_func(*args: list, **kwargs: str) -> str:
    return 'Yo'

print(decorated_func(1, 2, 3, a=1, b=2))
