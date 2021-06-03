# на вход в виде аргумента командной строки получает дату в виде строки  (напр. 2021/04/19);
# печатает на экран часовые интервалы для этой даты с 10:00 до 15:00 (как в примеру выше).

appointments = [
    '10:00 - 11:00 CEST',
    '11:00 - 12:00 CEST',
    '12:00 - 13:00 CEST',
    '13:00 - 14:00 CEST',
    '14:00 - 15:00 CEST'
]

print("Please enter the date: yyyy/mm/dd")

date = input()

for appointment in appointments:
    print(date + ' ' + appointment)
