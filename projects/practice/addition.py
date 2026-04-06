""" 
print("Give me two numbers,I'll add them")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    if second_number == 'q':
        break
    try:answer = int(first_number) + int(second_number)
    except ValueError:
        print("please enter a number:")
    else:print(answer)


from pathlib import Path

path = Path('cats.txt')
path2 = Path('dogs.txt')
try:
    contents = path.read_text(encoding='utf-8')
    contents += '\n'+ path2.read_text(encoding='utf-8')
except FileNotFoundError:
    pass
else:
    animals = contents.split()    #可以直接写:print(contents)
    for animal in animals:
        print(animal)
"""

from pathlib import Path
path = Path('gudengbao.txt')

def count_words(path):
    return path.lower().count('the ')  
    
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
        print("error")
else:
    print(count_words(contents))  