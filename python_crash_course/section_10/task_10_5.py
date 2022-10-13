'''
Simple file use.
'''


with open(file='file_task_10_5.txt', mode='w', encoding='utf-8') as f:
    while True:
        name: str = input("Enter your name or 'quit' to exit: ")
        if name == 'quit':
            break
        languages: str = input("Enter your favourite programming languages: ")
        f.write(f"{name} {languages.split()}\n")
