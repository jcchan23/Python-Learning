class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("the restaurant name is " + self.name)
        print("the restaurant type is " + self.type)
        print(str(self.number_served) + " people have been come to this restaurant!")

    def open_restaurant(self):
        print("the restaurant is opening!")

    def set_number_served(self,number):
        self.number_served = number 
    
    def increment_number_served(self,number):
        self.number_served += number

my_restaurant = Restaurant('DaTong','Chinese')
my_restaurant.describe_restaurant()

my_restaurant.number_served = 160
my_restaurant.describe_restaurant()

my_restaurant.set_number_served(320)
my_restaurant.describe_restaurant()

my_restaurant.increment_number_served(200)
my_restaurant.describe_restaurant()