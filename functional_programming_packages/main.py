from operator import attrgetter, itemgetter
from typing import NamedTuple

print(all([]))
print(any([]))

countries = ((1, 'USA'), (2, 'South Korea'), (3, 'Kazakhstan'))
print(sorted(countries, key=itemgetter(1)))


class Capital(NamedTuple):
    id: int
    name: str


class Country(NamedTuple):
    name: str
    capital: Capital


countries = [
    Country(**{'name': 'USA', 'capital': Capital(1, 'Washington')}),
    Country(**{'name': 'South Korea', 'capital': Capital(2, 'Seoul')})
]
country_capital_names = attrgetter('name', 'capital.name')  # Attributes which will be get of countries
for country in sorted(countries, key=attrgetter('capital.name')):
    print(country_capital_names(country))  # Get required attributes by passing `Country` object
