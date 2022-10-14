# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    _ = input()
    my_arr = list(map(int, input().strip().split()))
    A = set(map(int, input().strip().split()))
    B = set(map(int, input().strip().split()))

    happines = 0
    for element in my_arr:
        if element in A:
            happines += 1
        if element in B:
            happines -= 1

    print(happines)
