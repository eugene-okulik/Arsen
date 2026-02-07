import random


i = random.randrange(1, 4)

while i:
    numb = int(input('enter a number :'))
    if i == numb:
        break
    elif i != numb:
        print('попробуйте снова!')
print('поздравляю, вы угадали!!!')
