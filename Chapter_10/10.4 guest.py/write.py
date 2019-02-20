filename = r'Chapter 10\10.4 guest.py\guest_book.txt'

name = ""
while name != 'q':
    name = input("please input your name(input q to exit): ")
    if name != 'q':
        print("Hello, my friend " + name)
        with open(filename , 'a') as file_object:
            file_object.write(name + "\n")