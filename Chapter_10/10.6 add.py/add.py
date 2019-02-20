print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second_number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You should input a number!")
    else:
        print("the answer is " + str(answer))