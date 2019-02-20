class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print("the restaurant name is " + self.name)
        print("the restaurant type is " + self.type)

    def open_restaurant(self):
        print("the restaurant is opening!")

class IceCreamStand(Restaurant):
    
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['apple','pear','watermelon','grape']

    def show_flavors(self):
        for flavor in self.flavors:
            print("We have " + flavor +"'s icecream! ")
