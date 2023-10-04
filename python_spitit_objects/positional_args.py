class Cat:

    __match_args__ = ('name',)

    def __init__(self, name: str) -> None:
        self.__name: str = name

    @property
    def name(self) -> str:
        return self.__name

    def __hash__(self) -> hash:
        return hash(self.__name)

    def __repr__(self) -> str:
        return f'Cat({self.__name})'

    def __eq__(self, cat) -> bool:
        return self.__name == cat.name


patriciy = Cat('Patriciy')
gustav = Cat('Gustav')
match Cat('Jorik'):
    case Cat('Patriciy'):
        print('Patriciy!')
    case Cat('Gustav'):
        print('Not Patriciy! Gustav!')
    case Cat(_):
        print('Unknown cat?...')
    case _:
        print('Wtf? Who is it?')
