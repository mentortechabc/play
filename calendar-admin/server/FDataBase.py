import sqlite3
from datetime import datetime, timedelta
import sys
if "C:\learning\play\calendar-admin" not in sys.path:
    sys.path.append("C:\learning\play\calendar-admin")
from convert_time import utc_to_local,utc_to_local_format



class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_slots(self):
        sql = '''SELECT start_interval FROM Slots Where booking_id IS NULL'''
        # lst=[]
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            # print(res)
            # for x in res:
            #     x = x[0]
            #     lst.append(x)
            # print(lst)
            # return res
            if res:
                return res
        except:
            print('Ошибка чтения из БД')
        return []

    def add_users_info(self, user_name, user_email, message,start_interval, end_interval):
        try:
            self.__cur.execute(
                "INSERT INTO BookingInfo VALUES(NULL,?,?,?)", (user_name, user_email, message))
            self.__cur.execute("SELECT id FROM BookingInfo WHERE name == (?) AND email == (?) AND topic == (?)",
                    (user_name, user_email, message))
            booking_id = self.__cur.fetchall()
            for x in booking_id:
                res = x[0]
            params_start = start_interval.split(' ')
            params_end = end_interval.split(' ')
            params_start = 'T'.join(params_start)
            params_end = 'T'.join(params_end)
            params_start = utc_to_local(params_start)
            params_end = utc_to_local(params_end)
            print(params_start,params_end)
            while params_start < params_end:
                self.__cur.execute(
                    "UPDATE Slots SET booking_id = (?) WHERE start_interval = (?)", (res, params_start))
                params_start += timedelta(minutes=15)
            self.__db.commit()
        except sqlite3.Error as e:
            print(e)
            print("error")
            return False
        return True