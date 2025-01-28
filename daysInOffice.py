import calendar
import holidays
from datetime import date



def cal_time(year,month):
    months = []
    for i in range(1, 13):
        months.append(calendar.month_name[i])
    return calendar.month(year, month)

def get_working_days(year, month):
    us_holidays = holidays.US()
    working_days = []
    cal = calendar.Calendar()

    for day in cal.itermonthdays2(year, month):
        if day[0] != 0 and day[1] < 5:  # 0 is day of month, 1 is weekday (0-6, Mon-Sun)
            day_to_check = str(month) +'/' + str(day[0]) + '/' + str(year)
            if day_to_check not in us_holidays:
                working_days.append(day[0])
    return working_days

def min_days_in_office(working_days):
    if (len(working_days) % 2):
       min_days = str((len(working_days) + 1) / 2)
    else:
       min_days = str(len(working_days) /2)
    return min_days


if __name__ == '__main__':

    runtime_date = date.today()
#    print(cal_time(runtime_date.year,runtime_date.month))

    working_days = get_working_days(runtime_date.year, runtime_date.month)
    print('Min days in office needed= ', min_days_in_office(working_days))