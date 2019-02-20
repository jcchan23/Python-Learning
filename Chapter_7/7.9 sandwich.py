sandwich_orders = ['apple','pastrami','pear','grape','pastrami','watermelon','pastrami','orange']
finished_sandwiches = []

print("pastramis have been out of saled.")
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)