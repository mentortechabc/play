# 8-7 .
# Альбом: напишите функцию make_album(), которая
# строит словарь с описанием музыкального альбома.
# Функция должна получать имя исполнителя и название альбома
# и возвращать словарь, содержащий эти два вида информации .
# Используйте функцию для создания трех словарей, представляющих разные альбомы .
# Выведите все возвращаемые значения, чтобы показать,
# что информация правильно сохраняется во всех трех словарях .
# Добавьте в make_album() дополнительный параметр для сохранения количества дорожек в альбоме .
# Если в строку вызова включено значение количества дорожек,
# добавьте это значение в словарь альбома .
# Создайте как минимум один новый вызов функции с передачей количества дорожек в альбоме .

# 8-8 .
# Пользовательские альбомы: начните с программы из упражнения 8-7 .
# Напишите цикл while, в котором пользователь вводит исполнителя и название альбома .
# Затем в цикле вызывается функция make_album() для введенных пользователей
# и выводится созданный словарь .
# Не забудьте предусмотреть признак завершения в цикле while .

def make_album(singer_name, album_name, tracks_amount=0):
    singer = singer_name.title()
    album = album_name.title()

    if tracks_amount != 0:
        return {'singer': singer, 'album': album, 'tracks_amount': tracks_amount}

    return {'singer': singer, 'album': album}

# tests


def should_print_3_dictionaries():
    print("\nWith 3 dictionaries")
    print(make_album("billie ailish", "billie"))
    print(make_album("Mettalica", "Nothing else matters"))
    print(make_album("Nirvana", "Like a teen spirit"))


def should_return_album_with_tracks_amount():
    print("\nWith tracks amount")
    print(make_album("KINO", "Zvezda po imeni solnze", 5))


def should_handle_input_albums():
    print("\nHello! Answer the questions about the album you'd like to add")
    print("\n(enter 'q' at any time to quit)")
    while True:
        print("\nPlease tell me the title of the album")
        print("(enter 'q' at any time to quit)")
        album = input("Album: ")
        if album == 'q':
            break
        print("\nPlease tell me singer's name")
        print("(enter 'q' at any time to quit)")
        singer_name = input("Singer: ")
        if singer_name == 'q':
            break
        print("\nResult:")
        print(make_album(singer_name, album))


should_print_3_dictionaries()
should_return_album_with_tracks_amount()
should_handle_input_albums()
