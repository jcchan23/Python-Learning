import json
filename = 'Chapter 10/10.13 remember.py/username.json'
def get_stored_username():
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(name):
    with open(filename,'a') as f_obj:
        json.dump(name , f_obj)
    return name

def greet_user():
    name = input("please input your user name? ")
    username = get_stored_username()
    if username == name:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username(name)
        print("We’ll remember you when you come back, " + username + "!")

greet_user()