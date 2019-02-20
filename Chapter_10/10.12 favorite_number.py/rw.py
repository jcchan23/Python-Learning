import json
filepath = r'Chapter 10\10.12 favorite_number.py\favorite_number.txt'
number = input("what is your favorite number: ")

try:
    with open(filepath) as file_object:
        test_number = json.load(file_object)
    if number == test_number:
        print("We have stored your favorite number! It's " + test_number)
except FileNotFoundError:
    with open(filepath,'a') as file_object:
        json.dump(number,file_object)
    print("We finish to store your favorite number!")