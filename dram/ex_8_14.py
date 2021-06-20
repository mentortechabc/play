def make_car(brand, model, **additions):
    automobile = {'brand': brand, 'model': model}
    for key, value in additions.items():
        automobile[key] = value
    return automobile


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)