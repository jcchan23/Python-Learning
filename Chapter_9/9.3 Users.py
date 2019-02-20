class Users():
    def __init__(self,first_name,last_name,age,major):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.major = major

    def describe_user(self):
        print("My name is " + self.first_name + " " + self.last_name)
        print("I am " + self.age + " years old.")
        print("My major is " + self.major)  
    
    def greet_user(self):
        full_name = self.first_name + self.last_name
        print("Hello my friend " + full_name)

my_user = Users('Chen','Jian Wen','23','Maths')
my_user.describe_user()
my_user.greet_user()