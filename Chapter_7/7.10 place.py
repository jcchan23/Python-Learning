result = {}
polling_active = True
while polling_active:
    name = input("\nwhat is your name? ")
    place = input("if you could visit one place in the world, where would you go? ")
    result[name] = place

    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name,place in result.items():
    print(name + " would like to go to " + place)