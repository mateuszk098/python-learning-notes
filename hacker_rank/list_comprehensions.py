if __name__ == '__main__':
    x: int = int(input())
    y: int = int(input())
    z: int = int(input())
    n: int = int(input())

    permutations: list[list[int]] = [[i, j, k] for i in range(x+1) for j in range(y+1)
                                     for k in range(z+1) if i+j+k != n]

    print(permutations)
