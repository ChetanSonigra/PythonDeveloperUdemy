#datetime module
#store date and time in variables
#calculation with time
#display them in different ways

import datetime, zoneinfo

mytime = datetime.time(15,45)
print(mytime, mytime.minute, mytime.second, mytime.fold, mytime.tzinfo , type(mytime))

myday = datetime.date(2024,1,30)
print(myday, myday.day, myday.year, type(myday))
print(myday.ctime(), myday.today(), myday.min)

mydate = datetime.datetime(2023,5, 22, 11,30,00,500, zoneinfo('US/Eastern'))
print(mydate)
mydate = mydate.replace(month=11)
print(mydate)

print(zoneinfo.available_timezones())


birth = datetime.date(1998, 12,23)
death = datetime.date(2050, 5, 10)
life = death - birth
print(life, life.days, type(life))


wokeup = datetime.datetime(2023,11,27,5,30,20)
went_to_sleep = datetime.datetime(2023,11,27,23,30,0)
wakefulness = went_to_sleep - wokeup
print(wakefulness, wakefulness.seconds, type(wakefulness))

