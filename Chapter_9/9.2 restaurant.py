class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print("the restaurant name is " + self.name)
        print("the restaurant type is " + self.type)

    def open_restaurant(self):
        print("the restaurant is opening!")

my_restaurant = Restaurant('DaTong','Chinese')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant('Alcohol','England')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

he_restaurant = Restaurant('Fedora','France')
he_restaurant.describe_restaurant()
he_restaurant.open_restaurant()