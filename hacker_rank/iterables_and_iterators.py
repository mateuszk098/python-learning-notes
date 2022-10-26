# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input().strip())
elements = input().strip().split()
k = int(input().strip())

# indices_comb = list(combinations(range(1, n+1), k))
# indices = [i+1 for i, x in enumerate(elements) if x == 'a']

# sum = 0

# for sublist in indices_comb:
#     for index in sublist:
#         if index in indices:
#             sum += 1
#             break

# print(f'{sum/len(indices_comb):.3f}')


elements_comb = list(combinations(elements, k))
comb_with_a = [combination for combination in elements_comb if 'a' in combination]
print(f'{len(comb_with_a)/len(elements_comb):.3f}')
