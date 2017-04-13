import datetime

d = datetime.date(2017, 4, 8);
print(d)

today = datetime.date.today()
print(today)
print(today.year)
print(today.weekday())
print(today.isoweekday())

tdelta = datetime.timedelta(days = 7)
print(today - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

birthday = datetime.date(2018, 3, 22)
till_days = birthday - today
print(till_days)

