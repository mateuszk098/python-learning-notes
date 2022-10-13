'''
Simple file use.
'''

name: str = input('Enter your name: ')

with open(file='file_task_10_3.txt', mode='w', encoding='utf-8') as f:
    f.write(name)
