'''
Simple test.
'''

import unittest
from city_functions import city_description


class CitiesTestCase(unittest.TestCase):
    ''' Simple tests for `city_description()`. '''

    def test_city_country(self) -> None:
        ''' Are city and country correct? '''
        formatted_desc: str = city_description(city='Warsaw', country='Poland')
        self.assertEqual(formatted_desc, 'Country: Poland, City: Warsaw')


if __name__ == '__main__':
    unittest.main()
