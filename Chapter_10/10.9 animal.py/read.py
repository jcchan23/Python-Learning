filepath = 'Chapter 10/10.9 animal.py/'
filename = input("input your filename: ")

try:
    with open(filepath+filename) as file_object:
        contents = file_object.read()
        print(contents)
except FileNotFoundError:
    pass