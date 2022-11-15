"""
See description at https://www.hackerrank.com/challenges/zipped

The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = input().strip().split()

lst = [list(map(float, input().strip().split())) for _ in range(int(x))]
z = list(zip(*lst))
avg = [sum(sublist)/len(sublist) for sublist in z]
print(*avg, sep='\n')
