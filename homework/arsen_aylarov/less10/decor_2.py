def orifmetic(num):

    def wrapper(*args):
        first_num, second_num = num(*args)
        if first_num == second_num:
            return first_num + second_num
        elif first_num or second_num < 0:
            return first_num * second_num
        elif first_num > second_num:
            return first_num - second_num
        elif first_num < second_num:
            return first_num / second_num
    return wrapper


@orifmetic
def ori(a, b):
    return a, b

a = int(input('input first number: '))
b = int(input('input second number: '))
print(ori(a, b))

