#!python3
from datetime import datetime, timedelta


class Person(object):
    def __init__(self, birthday):
        self._birthday = birthday

    @classmethod
    def from_datestring(cls, datestring):
        date = datetime.strptime(datestring, '%Y/%m/%d')
        return cls(birthday=date.year)

    def get_age(self):
        now = datetime.now()
        delta = timedelta(365 * self._birthday)
        diff = now - delta
        return '{} years, {} months and {} days'.format(
            diff.year,
            diff.month,
            diff.day
        )


p = Person.from_datestring('1994/03/29')
print(p.get_age())
