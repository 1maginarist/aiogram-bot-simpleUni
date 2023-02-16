import datetime

months_30 = ['Январь', 'Июнь', 'Сентябрь', 'Ноябрь']
months_31 = ['Январь', 'Март', 'Май', 'Июль', 'Август', 'Октябрь', 'Декабрь']


def is_leap_year():
    current_year = datetime.datetime.now().year
    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        return True
    else:
        return False


def date_filter(month, date):
    max_days = 30 if month in months_30 else 31 if month in months_31 else 28 if not is_leap_year() else 29
    return date <= max_days


