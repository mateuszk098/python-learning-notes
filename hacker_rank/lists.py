if __name__ == '__main__':
    N: int = int(input())
    my_lst: list = []

    for _ in range(N):
        command: list = input().strip().split()
        if command[0] == 'insert':
            my_lst.insert(int(command[1]), int(command[2]))
        if command[0] == 'print':
            print(my_lst)
        if command[0] == 'remove':
            my_lst.remove(int(command[1]))
        if command[0] == 'append':
            my_lst.append(int(command[1]))
        if command[0] == 'sort':
            my_lst.sort()
        if command[0] == 'pop':
            my_lst.pop()
        if command[0] == 'reverse':
            my_lst.reverse()
