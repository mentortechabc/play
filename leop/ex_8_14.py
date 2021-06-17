# 8-14 .
# Автомобили: напишите функцию для сохранения информации об автомобиле в словаре .
# Функция всегда должна возвращать производителя и название модели,
# но при этом она может получать произвольное количество именованных аргументов .
# Вызовите функцию с передачей обязательной информации и еще двух пар «имя—значение»
# (например, цвет и комплектация) .
# Ваша функция должна работать для вызовов следующего вида:
# car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)

# Выведите возвращаемый словарь и убедитесь в том, что вся информация была сохранена правильно .

def make_car(brand, model, **car_info):
    car_profile = {'brand': brand, 'model': model}

    for key, value in car_info.items():
        car_profile[key] = value

    return car_profile


car_profile_1 = make_car("subaru", "outback",
                         color="blue",
                         tow_package="True")

car_profile_2 = make_car("BMW", "outback",
                         color="red",
                         owner="Alice",
                         age="5 years")

car_profile_3 = make_car("Audi", "convertible",
                         bought_by="Anthony",
                         condition="new")

car_profile_4 = make_car("Renault", "convertible",
                         bought_by="Billy",
                         condition="used")

print(car_profile_1)
print(car_profile_2)
print(car_profile_3)
print(car_profile_4)
