pizzas = ['Pork','pepperoni','vegetable','beef']
friend_pizzas = pizzas[:]
pizzas.append('apple')
friend_pizzas.append('orange')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)