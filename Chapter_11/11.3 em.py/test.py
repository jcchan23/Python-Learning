import unittest
from employee import Employee

class TestAnonymousEmployee(unittest.TestCase):

    def setUp(self):
        self.my_em = Employee('Chen','Jian Wen',6000)
    
    def test_give_default_raise(self):
        self.my_em.give_raise()
        self.assertEqual(self.my_em.year_money,11000)
    
    def test_give_custom_raise(self):
        self.my_em.give_raise(6000)
        self.assertEqual(self.my_em.year_money,12000)

unittest.main()