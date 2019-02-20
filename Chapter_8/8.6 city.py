def city_country(city_name,country):
    full_name = city_name.title() + ' ' + country.title()
    return full_name.title()

print(city_country('Guang Zhou','China'))
print(city_country('New York','USA'))
print(city_country('London','England'))