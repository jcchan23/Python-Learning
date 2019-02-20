fruits = []
message = ""
while message != 'quit':
    message = input("which fruit do you want to add? (input 'quit' to exit.)")
    if message != 'quit':
        fruits.append(message)
        print("we have added " + message + " in our pizza.\n")

print("\nnow we have these fruits in our pizza.")
print(fruits)
