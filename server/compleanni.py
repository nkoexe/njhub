from datetime import datetime
from json import dump, load
from os import fspath
from pathlib import Path


# Todo: check if a date is valid
# Todo: support for adding birthdays
# Todo: if script is run for a long time, update the now variable


with open(fspath(Path(__file__).resolve().parent / 'database/compleanni.json'), 'r') as f:
    _birthdates = load(f)


_now = datetime.now()


def get_birthdays(interval: int = 3) -> list:
    '''
    Get all birthdays in some interval of days.
    Returns a list of tuples, each containing the name, date, age and days remaining of a birthday.

    :param int interval: the interval to check
    :return: a list of tuples of the form (name: str, date: datetime, age: int, days_remaining: int)
    :rtype: list
    '''
    lst = []

    for i in _birthdates:
        date = get_date(_birthdates[i])
        remaining = birthday_in_interval(date, interval)
        if remaining:
            lst.append((i, date, _now.year - date.year, remaining))

    return lst


def get_date(date: str) -> datetime:
    '''
    Convert date string to datetime object.
    Ex: '01-01-2020' -> datetime(2020, 1, 1)

    :param str date: the date string
    :return: the datetime object
    :rtype: datetime
    '''
    return datetime.strptime(date, '%d-%m-%Y')


def birthday_in_interval(date: datetime, interval: int) -> int or bool:
    '''
    Check if a birthday is in some interval of days.
    Only considers day and month, the year is discarded.
    Returns the number of days remaining if the birthday is in the interval, False otherwise.

    :param datetime date: the date to check
    :param int interval: the interval to check
    :return: number of days remaining or False
    :rtype: int or bool
    '''
    date = date.replace(year=_now.year)
    remaining = (date - _now).days

    if 0 <= remaining <= interval:
        return remaining
    else:
        date = date.replace(year=_now.year + 1)
        remaining = (date - _now).days

        if 0 <= remaining <= interval:
            return remaining
        else:
            return False


if __name__ == '__main__':
    for i in get_birthdays(50):
        print(i)
