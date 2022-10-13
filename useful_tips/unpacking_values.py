'''
Unpacking values.
'''

# 3 and 4 will be assigned to c, which is a list
a, b, *c, d = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)
print(d)

# Ignore 3 and 4 value from list
a, b, *_, d = [1, 2, 3, 4, 5]
print(a)
print(b)
print(d)
