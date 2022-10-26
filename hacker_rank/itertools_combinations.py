# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s, n = input().strip().split()

for k in range(1, int(n)+1):
    comb = list(combinations(s, k))
    comb_sort = [sorted(sublist) for sublist in comb]
    comb_concat = list(map(''.join, comb_sort))
    print(*sorted(comb_concat), sep='\n')
