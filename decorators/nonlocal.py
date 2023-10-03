from typing import Callable


def closure_without_free_variable() -> Callable[[], str]:
    """
    Raises an error, because immutable
    type's variable cannot be a free variable
    """
    string1 = 'I am Bob!'

    def wrapper() -> str:
        string1 += ' How are you?'
        return string1

    return wrapper



def closure_with_free_variable() -> Callable[[], str]:
    """Wrapper can work with `string1` because it is non local variable"""
    string1 = 'I am Alice!'

    def wrapper() -> str:
        nonlocal string1
        string1 += ' How are you, Bob?'
        return string1

    return wrapper


try:
    print(closure_without_free_variable()())  # UnboundLocalError
except UnboundLocalError as _ex:
    print(_ex)

print(closure_with_free_variable()())  # Work's fine
