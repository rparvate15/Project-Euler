
import calendar

calendar.setfirstweekday(calendar.SUNDAY)

first_sundays = 0

for i in range(1901, 2001):
    for j in range (1, 13):
        testmonth = calendar.monthcalendar(i, j)
        if testmonth[0][0] == 1:
            first_sundays += 1
            print("true")
        else:
            print("false")

print(first_sundays)