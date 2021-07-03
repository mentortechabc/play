import datetime

t1 = datetime.datetime.fromisoformat("2020-01-02T13:15")

for x in range(10):
    start = t1 + datetime.timedelta(days=x)
    end = start + datetime.timedelta(minutes=30)
    print(start.isoformat(), end.isoformat())