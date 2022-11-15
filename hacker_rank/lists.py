"""
See description at https://www.hackerrank.com/challenges/python-lists

Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where 
each command will be of the 7 types listed above. Iterate through each command in order 
and perform the corresponding operation on your list.
"""

if __name__ == "__main__":
    N: int = int(input())
    my_lst: list = []

    for _ in range(N):
        command: list = input().strip().split()
        if command[0] == "insert":
            my_lst.insert(int(command[1]), int(command[2]))
        if command[0] == "print":
            print(my_lst)
        if command[0] == "remove":
            my_lst.remove(int(command[1]))
        if command[0] == "append":
            my_lst.append(int(command[1]))
        if command[0] == "sort":
            my_lst.sort()
        if command[0] == "pop":
            my_lst.pop()
        if command[0] == "reverse":
            my_lst.reverse()
