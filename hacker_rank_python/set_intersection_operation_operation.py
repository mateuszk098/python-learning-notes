"""
The students of District College have subscriptions to English and French
newspapers. Some students have subscribed only to English, some have 
subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed
to the English newspaper, one set has subscribed to the French newspaper.
Your task is to find the total number of students who have subscribed
to both newspapers.

See description at https://www.hackerrank.com/challenges/py-set-intersection-operation
"""

n1 = int(input())
s1 = set(map(int, input().split()))

n2 = int(input())
s2 = set(map(int, input().split()))

students = s1.intersection(s2)
print(len(students))
