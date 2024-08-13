import datetime
t_delta = datetime.timedelta(days=1)
dt3 = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt3 + t_delta)

