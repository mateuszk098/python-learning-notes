# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    _ = input()
    my_set1: set = set(map(int, input().strip().split()))
    _ = input()
    my_set2: set = set(map(int, input().strip().split()))
    symm_diff: list = sorted(my_set1 ^ my_set2)
    print(*symm_diff, sep='\n')
