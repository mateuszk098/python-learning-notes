'''
Function to form city, country and population.
'''


def city_description(city: str, country: str, population: int | None = None) -> str:
    ''' Returns formatted city, country and population. '''
    if population is not None:
        return f"Country: {country}, City: {city}, Population: {population}"
    return f"Country: {country}, City: {city}"
