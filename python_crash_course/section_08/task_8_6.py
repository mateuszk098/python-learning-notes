'''
Simple function. Return statement.
'''


def city_country(city: str, country: str) -> str:
    '''
    Returns city information.
    '''
    return f"{city.title()}, {country.title()}"


print(city_country('Warsaw', 'Poland'))
print(city_country('New York', 'United States'))
print(city_country('Paris', 'France'))
