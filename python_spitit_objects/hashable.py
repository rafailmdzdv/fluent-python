class Cat:

    def __init__(self, name: str) -> None:
        self.__name: str = name

    @property
    def name(self) -> str:
        return self.__name

    def __hash__(self) -> hash:
        return hash(self.__name)

    def __repr__(self) -> str:
        return f'Cat({self.__name})'

patriciy = Cat('Patriciy')
print({patriciy})
print({patriciy: '1.5'})
