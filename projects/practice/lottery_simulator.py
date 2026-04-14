from random import randint

class Die:
    def __init__(self):
        sides = 6
        self.sides = sides
    
    def roll_die(self):
        return randint(1,self.sides)

my_die = Die()
my_die.sides = 10
print(my_die.roll_die())

"""
from random import choice

n = list(range(1,11)) + list('abcde')
winning_numbers =[]

while len(winning_numbers)<4:
    winning_number = choice(n)
    winning_numbers.append(winning_number)
w_n = ' '.join(str(x) for x in winning_numbers)
print("The winning numbers are " + w_n)



times = 0
nn = []
my_w_n = ''
while my_w_n != w_n:
    nn.append(choice(n))  #ticket = [choice(n) for _ in range(4)] 在一次循环内调用四次choice
                          #这样times能更精准算出尝试了多少组
    times += 1
    my_w_n = ' '.join(str(x) for x in nn)
    if len(nn)>4:
        nn = []   # nn.clear() 也可以
        continue
    
print(my_w_n)
print(f"直到中奖总共循环了{times}次")
"""