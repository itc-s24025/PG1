from datetime import date
day_now = date.today()
print(day_now)

xday = date(2024, 4, 5)
zday = date(2005, 10, 22)

td = day_now - xday
ts = day_now - zday
print(f"入学してから{td}")
print(f"生まれてから{ts}")
