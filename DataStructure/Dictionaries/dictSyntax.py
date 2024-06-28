'''Dict comprehensions (dictComps) build an instance by taking key:value pairs
from any iterable'''

dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (91, 'India'),
    (1, 'USA')
]
country_dial = {country: code for code, country in dial_codes}
print(country_dial)