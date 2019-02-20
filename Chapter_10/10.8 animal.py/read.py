filepath = 'Chapter 10/10.8 animal.py/'
filename = input("input your filename: ")

try:
    with open(filepath+filename) as file_object:
        contents = file_object.read()
        print(contents)
except FileNotFoundError:
    print("This file is not exist!")