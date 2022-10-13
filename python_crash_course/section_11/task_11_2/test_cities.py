'''
Simple set of tests.
'''

import unittest
from city_functions import city_description


class CitiesTestCase(unittest.TestCase):
    ''' Simple tests for `city_description()`. '''

    def test_city_country(self) -> None:
        ''' Are city and country correct? '''
        formatted_desc: str = city_description(city='Warsaw', country='Poland')
        self.assertEqual(formatted_desc, 'Country: Poland, City: Warsaw')

    def test_city_country_population(self) -> None:
        ''' Are city, country and population correct? '''
        formatted_desc: str = city_description(
            city='Warsaw', country='Poland', population=1_750_000)
        self.assertEqual(formatted_desc, 'Country: Poland, City: Warsaw, Population: 1750000')


if __name__ == '__main__':
    unittest.main()
