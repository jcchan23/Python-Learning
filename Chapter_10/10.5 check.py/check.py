filename = "Chapter 10/10.5 check.py/reason.txt"

while True:
    with open(filename,'a') as file_object:
        reason = input("what is your reason for programing(input q to quit): ")
        if reason == 'q':
            break
        else:
            file_object.write(reason + "\n")