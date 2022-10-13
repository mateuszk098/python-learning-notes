'''
Simple function. Default values
'''


def describe_city(city: str, country: str = 'Poland') -> None:
    '''
    Print informations about city.
    '''
    print(f"City: {city}, Country: {country}")


describe_city('Wrocław')
describe_city(city='Warsaw')
describe_city(city='Barcelona', country='Spain')
describe_city('Berlin', 'Germany')
