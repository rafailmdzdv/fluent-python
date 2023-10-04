def some_function() -> tuple[int, 4]:
    print(1, 2, 3, 4)
    return (1, 2, 3, 4)


def some_function2() -> tuple[int, 4]:
    print(112, 113, 114, 115)
    return (112, 113, 114, 115)


def some_function3() -> tuple[int, 4]:
    print(116, 117, 118, 119)
    return (116, 117, 118, 119)


def some_function4() -> tuple[int, 4]:
    print(120, 220, 320, 420)
    return (120, 220, 320, 420)


def some_function5() -> tuple[int, 4]:
    print(330, 440, 550, 600)
    return (330, 440, 550, 600)


def some_function6() -> tuple[int, 4]:
    print(600, 780, 800, 900)
    return (600, 780, 800, 900)


def some_function7() -> tuple[int, 4]:
    print(1100, 1200, 1300, 1400)
    return (1100, 1200, 1300, 1400)


def some_function8() -> None:
    for name, function in globals().items():
        if name.startswith('some') and not name.endswith('function8'):
            print(f'Executing function with name: {name}', function())


# some_function8()
