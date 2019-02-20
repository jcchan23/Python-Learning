from users import Users
class Admin(Users):
    
    def __init__(self,first_name,last_name,age,major):
        super().__init__(first_name,last_name,age,major)
        self.privileges = Privileges(['can add post',
        'can delete post','can ban users'])

class Privileges():
    def __init__(self,privileges_lists):
        self.privileges = privileges_lists

    def show_privileges(self):
        for privilege in self.privileges:
            print("Admin " + privilege)