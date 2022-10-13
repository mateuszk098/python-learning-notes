'''
Simple exception handling with file.
'''

fname: str = input('Enter filename: ')

try:
    with open(file=fname, mode='r', encoding='utf-8') as f:
        content: str = f.read()
except FileNotFoundError:
    print('File not found! Try again!')
else:
    print(content)
