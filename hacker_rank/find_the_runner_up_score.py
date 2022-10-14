if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # In set we have only unique values
    larr = list(set(arr))
    result = sorted(larr)[-2]
    print(result)
