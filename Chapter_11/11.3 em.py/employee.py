class Employee():

    def __init__(self,first_name,last_name,year_money):
        self.first_name = first_name
        self.last_name = last_name
        self.year_money = year_money
    
    def give_raise(self,money = 5000):
        self.year_money += money