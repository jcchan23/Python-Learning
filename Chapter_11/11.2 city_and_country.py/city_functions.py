def city_country(city_name,country_name,population=''):
    if population:
        full_name = city_name.title() + ', ' + country_name.title() + \
                    ' - population ' + str(population)
    else:
        full_name = city_name.title() + ', ' + country_name.title()
    return full_name