'''
Open files using 'with'.
'''

# Typical open and close.
f = open('file_open_text.txt', 'r', encoding='utf-8')
file_contents1: str = f.read()
f.close()
print(file_contents1)

# Open using 'with' - python decides when to close file.
with open('file_open_text.txt', 'r', encoding='utf-8') as f:
    file_contents2: str = f.read()
print(file_contents2)
