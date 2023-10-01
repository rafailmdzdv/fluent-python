from typing import Optional


def concat(string: Optional[str] = None, string2: Optional[str] = None) -> str:
    if not string:
        string = ''
    if not string2:
        return string
    return string + string2


print(concat('Hello', 'World'))
print(concat('Hello'))
print(concat(string2='World'))
