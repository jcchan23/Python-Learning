sandwich_orders = ['apple','pear','grape','watermelon','orange']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)