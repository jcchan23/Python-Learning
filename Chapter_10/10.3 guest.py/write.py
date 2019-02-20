filename = r'Chapter 10\10.3 guest.py\guest.txt'

name = input("please input your name: ")

with open(filename , 'w') as file_object:
    file_object.write(name)