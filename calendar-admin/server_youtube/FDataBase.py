import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_slots(self):
        sql = '''SELECT start_interval FROM Slots Where booking_id IS NULL'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print('Ошибка чтения из БД')
        return []

    def add_users_info(self, user_name, user_email, message,start_interval, end_interval):
        print(user_name, user_email, message,start_interval, end_interval)
        try:
            self.__cur.execute(
                "INSERT INTO BookingInfo VALUES(NULL,?,?,?)", (user_name, user_email, message))
            self.__db.commit()
        except sqlite3.Error as e:
            print(e)
            print("error")
            return False
        return True
