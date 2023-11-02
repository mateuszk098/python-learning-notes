"""
You are given a date. Your task is to find what the day is on that date.

See description at https://www.hackerrank.com/challenges/calendar-module
"""

import calendar


month, day, year = map(int, input().split())

num_day = calendar.weekday(year, month, day)
day_name = calendar.day_name[num_day]
day_name = day_name.upper()

print(day_name)
