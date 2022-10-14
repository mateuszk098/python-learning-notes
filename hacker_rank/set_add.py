# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input().strip())
    stamps = set()

    for _ in range(n):
        stamp = input().strip()
        stamps.add(stamp)

    print(len(stamps))
