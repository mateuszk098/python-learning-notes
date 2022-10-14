# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n: int = int(input())
    t: tuple = tuple(map(int, input().split()))

    print(hash(t))  # Run with Pypy 3
