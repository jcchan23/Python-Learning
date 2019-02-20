age = 1
while age:
    age = input("please tell me your age:(input 0 to exit)")
    age = int(age)
    if age == 0:
        break
    elif age <= 3:
        print("you have no pay!")
    elif age <= 12:
        print("you have to pay $10!")
    else:
        print("you have to pay $15!")