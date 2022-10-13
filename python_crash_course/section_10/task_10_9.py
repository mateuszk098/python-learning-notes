'''
Simple exception handling with file and quiet failure.
'''

fname: str = input('Enter filename: ')

try:
    with open(file=fname, mode='r', encoding='utf-8') as f:
        content: str = f.read()
except FileNotFoundError:
    pass
else:
    print(content)
