# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, n = input().strip().split()

comb = list(combinations_with_replacement(s, int(n)))
comb_sort = [sorted(sublist) for sublist in comb]
comb_concat = list(map(''.join, comb_sort))
print(*sorted(comb_concat), sep='\n')
