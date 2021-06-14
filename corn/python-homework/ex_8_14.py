def car_information(marka, model, **any_info):
    car = {}
    car["marka"] = marka
    car["model"] = model
    for k, v in any_info.items():
        car[k] = v
    return car


x = car_information('aidi', '100', color='red', size_wheel='24')
print(x)
