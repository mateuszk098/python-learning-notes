# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, n = input().strip().split()

perm = list(permutations(s, int(n)))
perm_concat = list(map(''.join, perm))

print(*sorted(perm_concat), sep='\n')
