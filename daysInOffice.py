import calendar

def cal_time():
    months = []
    for i in range(1, 13):
        months.append(calendar.month_name[i])
    print(months)
    print(calendar.month(2025, 1))

import calendar

def get_working_days(year, month):
    """Gets working days in a given month, excluding weekends."""

    working_days = []
    cal = calendar.Calendar()

    for day in cal.itermonthdays2(year, month):
        if day[0] != 0 and day[1] < 5:  # 0 is day of month, 1 is weekday (0-6, Mon-Sun)
            working_days.append(day[0])

    return working_days



if __name__ == '__main__':
    cal_time()

    year = 2025
    month = 1  # December
    working_days = get_working_days(year, month)
    print(working_days)

