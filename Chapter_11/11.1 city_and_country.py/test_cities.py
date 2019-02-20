import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_name = city_country('santiago','chile')
        self.assertEqual(formatted_name,'Santiago,Chile')

unittest.main()