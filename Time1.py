import datetime as dt
import calendar

class Time(object):
    """Represents the time of day.

    attributes: hour, minute, second.
    """

def print_time(time):
    print('%.2d:%.2d:%.2d') % (time.hour, time.minute, time.second)

def is_after(t1, t2):
    # dhour = (t1.hour - t2.hour) * 3600
    # dminute = (t1.minute - t2.minute) * 60
    # dsecond = t1.second - t2.second
    # return (dhour + dminute + dsecond) > 0

    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

def increment(time, seconds):
    time.second += seconds
    time.minute += int(time.second / 60)
    time.hour += int(time.minute / 60)
    time.second = time.second % 60
    time.minute = time.minute % 60

def increment_new(time, seconds):
#     new_time = Time()
#     new_time.second = time.second + seconds
#     new_time.minute, new_time.second = divmod(new_time.second, 60)
#     new_time.hour, new_time.minute = divmod(new_time.minute, 60)

    seconds += time_to_int(time)
    return int_to_time(seconds)

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_toint(t2)
    return int_to_time(seconds)

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False

    if time.minute >= 60 or time.second >= 60:
        return False

    return True

def mul_time(time, n):
    return int_to_time(time_to_int(time) * n)

def avg_pace(time, distance):
    return mul_time(time, 1/distance)

def print_weekday():
    date = dt.date.today()
    week_n = date.weekday()
    day_names = calendar.day_name
    print("Today is %s." % day_names[week_n])

def age(bd):
    today = dt.datetime.today()
    return today - bd

def next_birthday(bd):
    today = dt.date.today()

    if today.month > bd.month or (today.month == bd.month and today.day >= bd.day):
        next_bd = dt.datetime(today.year + 1, bd.month, bd.day)
    else:
        next_bd = dt.datetime(today.year, bd.month, bd.day)

    return next_bd

def print_next_birthday(bd):
    curr_age = age(bd).days // 365
    next_bd = next_birthday(bd)
    today = dt.datetime.today()
    remaining = next_birthday(bd) - today
    minutes, seconds = divmod(remaining.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    print("Age: %s years.\nThere's %s days, %s hours, %s minutes and %s seconds remaining for the next birthday." % (curr_age, remaining.days, hours, minutes, seconds))

def double_day(bd1, bd2):
    orderT = [bd1, bd2]
    orderT.sort(reverse=True)
    newer, older = orderT
    age_diff = newer - older
    return newer + age_diff

def n_ble_day(bd1, bd2, n=2):
    orderT = [bd1, bd2]
    orderT.sort(reverse=True)
    newer, older = orderT
    age_diff = newer - older
    return newer + age_diff / (n - 1)

if __name__ == '__main__':
    t1 = Time()
    t1.hour = 8
    t1.minute = 59
    t1.second = 30

    t2 = Time()
    t2.hour = 11
    t2.minute = 59
    t2.second = 29

    # print(is_after(t1, t2))
    # print_weekday()

    birthday = dt.datetime(2003, 4, 23)
    birthday2 = dt.datetime(1995, 4, 23)
    # print_next_birthday(birthday)
    # print(double_day(birthday, birthday2))
    print(n_ble_day(birthday, birthday2, 5))
