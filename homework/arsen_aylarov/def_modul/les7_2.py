import random


salary = int(input('Enter your salary: '))
bonus = bool(random.getrandbits(1))

if bonus is True:
    salary1 = salary
    salary1 += int(random.randint(1, 100))
    print(f'{salary}, {bonus} - ${salary1}')
else:
    print(f'{salary}, {bonus} - ${salary}')


def random_per(num):
    salary = num
    bonus = bool(random.getrandbits(1))

    if bonus is True:
        salary1 = salary
        salary1 += int(random.uniform(1, 100))
        print(f'{salary}, {bonus} - "${salary1}"')
    else:
        print(f'{salary}, {bonus} - "${salary}"')


random_per(int(input('Enter a number: ')))
