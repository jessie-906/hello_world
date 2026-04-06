from pathlib import Path
"""
path = Path('Learning_Python.txt')
contents = path.read_text()
print(contents)

for line in contents.splitlines():
    print("\n" + line)

contents.replace('Python','C++')
print("\n" + contents.replace('Python','C++')) 
"""
path = Path('guest.txt')

contents = ''
while True:
    content = input("what's your name:")
    contents += (content + "\n")
    path.write_text(contents)