"""
Students of District College have subscriptions to English and French
newspapers. Some students have subscribed to English only, some have
subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed
to the English newspaper, and one set has subscribed to the French
newspaper. Your task is to find the total number of students who have
subscribed to either the English or the French newspaper but not both.

See description at https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation
"""

n1 = int(input())
s1 = set(map(int, input().split()))

n2 = int(input())
s2 = set(map(int, input().split()))

students = s1.symmetric_difference(s2)
print(len(students))
