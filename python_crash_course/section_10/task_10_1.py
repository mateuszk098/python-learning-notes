'''
Simple file use.
'''

with open(file='file.txt', mode='r', encoding='utf-8') as f:
    content: str = f.read()  # All in one string

with open(file='file.txt', mode='r', encoding='utf-8') as f:
    contents_list: list = list(f)  # Each line is a single element

with open(file='file.txt', mode='r', encoding='utf-8') as f:
    contents_readlines: list = f.readlines()  # Each line is a single element

print(content)
print(contents_list)
print(contents_readlines)
