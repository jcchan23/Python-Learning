names = ['JCChan','Jack','John','Tom','admin']
if names:
    for name in names:
        if name == 'admin':
            print("Hello " + str(name) + ", would you like to see a status report?")
        else:
            print("Hello " + str(name) + ", thank you for logging in again")
else:
    print("We need to find some users!")
    