from datetime import datetime, timedelta
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
    # the result list
    lst = []

    for i in _birthdates:
        # Get the date of the birthday. String format: dd-mm-yyyy
        date = datetime.strptime(_birthdates[i], '%d-%m-%Y')
        # If the birthday is in the interval 'remaining' is the days remaining, False otherwise
        remaining = birthday_in_interval(date, interval)
        if remaining:
            # Add the birthday to the list, refer to docstring for the format
            # The age (third element) is calculated as the difference between the year of the next
            # birthday date and the birth year, that's why the remaining days are added to the current date,
            # as the birthday could be in the following year.
            lst.append((i, date, (_now + timedelta(days=remaining)).year - date.year, remaining))

    return lst


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
    # Todo: redo, adding the interval to the current date not limiting the interval to 2 years

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
