from random import randint

class Die():

    def __init__(self,size):
        self.size = size
    
    def roll_die(self):
        counter = 1
        while counter <= 10:
            x = randint(1,self.size)
            print(x)
            counter += 1

my_counter = Die(20)
my_counter.roll_die()
    