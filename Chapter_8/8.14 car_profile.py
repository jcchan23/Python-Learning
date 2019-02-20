def car_profile(builder,model,**car_info):
    info = {}
    info['builder_name'] = builder
    info['version'] = model

    for key,value in car_info.items():
        info[key] = value
    return info

car = car_profile('subaru','outback',color = 'blue',tow_package = True)
print(car)