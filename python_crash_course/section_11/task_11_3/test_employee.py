'''
Simple test of the employee class.
'''

import unittest
from employee import Employee


class TestEmployeeClass(unittest.TestCase):
    ''' Simple test of the employee class. '''

    def setUp(self) -> None:
        self.my_emp: Employee = Employee('Wilhelmine', 'Bechtelar', 85_000)

    def test_give_default_raise(self) -> None:
        ''' Test of default raise. '''
        self.my_emp.give_raise()
        self.assertEqual(self.my_emp.get_raise(), 90_000)

    def test_give_raise(self) -> None:
        ''' Test of a raise. '''
        self.my_emp.give_raise(10_000)
        self.assertEqual(self.my_emp.get_raise(), 95_000)


if __name__ == '__main__':
    unittest.main()
