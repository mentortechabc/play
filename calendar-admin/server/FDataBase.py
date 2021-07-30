import sqlite3
from datetime import datetime, timedelta
import sys
if "C:\learning\play\calendar-admin" not in sys.path:
    sys.path.append("C:\learning\play\calendar-admin")
from convert_time import utc_to_local,local_to_utc



class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_slots(self):
        sql = '''SELECT start_interval FROM Slots Where booking_id IS NULL'''
        lst=[]
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            for x in res:
                x = x[0]
                lst.append(utc_to_local(x))
            return lst
        except:
            print('Ошибка чтения из БД')
        return []

    def add_users_info(self, user_name, user_email, message,start_interval, end_interval):
        try:
            self.__cur.execute(
                "INSERT INTO BookingInfo VALUES(NULL,?,?,?)", (user_name, user_email, message))
            self.__cur.execute("SELECT MAX(id) AS Last FROM BookingInfo")
            booking_id = self.__cur.fetchall()
            for x in booking_id:
                res = x[0]
            params_start = local_to_utc(start_interval)
            params_end = local_to_utc(end_interval)
            self.__cur.execute(
                    "UPDATE Slots SET booking_id = (?) WHERE start_interval BETWEEN (?) AND (?)", (res, params_start,params_end))
            self.__db.commit()
        except sqlite3.Error as e:
            print(e)
            print("error")
            return False
        return True