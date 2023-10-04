import inspect

import globals


def some_function8() -> None:
    for name, function in inspect.getmembers(globals, inspect.isfunction):
        if not name.endswith('function8'):
            print(name)
            function()


some_function8()
