"""
Dr. John Wesley has a spreadsheet containing a list of student's 
IDs, MARKS, CLASS and NAME. Your task is to help Dr. Wesley calculate
the average marks of the students.

See description at https://www.hackerrank.com/challenges/py-collections-namedtuple
"""

from collections import namedtuple

n = int(input())
pattern = input().strip().split()

Student = namedtuple("Student", pattern)
sum = 0

for _ in range(n):
    ptrn = input().strip().split()
    s = Student(*ptrn)
    sum += int(s.MARKS)

result = sum / n
print(f"{result:.2f}")
