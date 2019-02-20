def make_pizza(*fruits):
    for fruit in fruits:
        print(fruit + " had been added in sandwiches.")
    print(fruits)

make_pizza('apple','pear','watermelon')
make_pizza('tomato','potato')
make_pizza('pork','duck','cow','sheep')