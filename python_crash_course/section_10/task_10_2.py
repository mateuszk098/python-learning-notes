'''
Simple file use.
'''

with open(file='file.txt', mode='r', encoding='utf-8') as f:
    content: str = f.read()

content = content.replace('illum', 'Python')
print(content)
