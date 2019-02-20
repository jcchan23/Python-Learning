rivers = {
    'nile':'egypt',
    'chang jiang river':'china',
    'ganges':'india'
}

for river_name,country in rivers.items():
    print("The" + river_name + "runs through" + country)

for river_name in rivers.keys():
    print("River name is " + river_name)

for country in rivers.values():
    print("Country name is " + country)