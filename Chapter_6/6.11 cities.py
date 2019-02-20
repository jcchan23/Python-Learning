cities = {
    'Guang Zhou':{
        'country':'china',
        'population':'12,000,000',
        'fact':'best food',
    },
    'Chang Sha':{
        'country':'china',
        'population':'5,000,000',
        'fact':'pepper',
    },
    'London':{
        'country':'England',
        'population':'100,000',
        'fact':'fog',
    },
}
for city_name,city_info in cities.items():
    print("\ncity name: " + city_name)
    print("\tcountry: " + city_info['country'])
    print("\tpopulation: " + city_info['population'])
    print("\tfact: " + city_info['fact'])
