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

class Admin(Users):
    
    def __init__(self,first_name,last_name,age,major):
        super().__init__(first_name,last_name,age,major)
        self.privileges = ['can add post','can delete post','can ban users']

    def show_privileges(self):
        for privilege in self.privileges:
            print("Admin " + privilege)

my_user = Admin('Chen','Jian Wen','23','Maths')
my_user.describe_user()
my_user.greet_user()
my_user.show_privileges()