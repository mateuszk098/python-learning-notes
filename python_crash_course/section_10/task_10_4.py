'''
Simple file use.
'''


with open(file='file_task_10_4.txt', mode='w', encoding='utf-8') as f:
    while True:
        name: str = input("Enter your name or 'quit' to exit: ")
        if name == 'quit':
            break
        f.write(f"{name}\n")
