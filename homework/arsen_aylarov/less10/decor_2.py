def orifmetic(num):

    def wrapper(*args):
        first_num, second_num = args
        if first_num == second_num:
            return num(first_num, second_num, '+')
        elif first_num or second_num < 0:
            return num(first_num, second_num, '*')
        elif first_num > second_num:
            return num(first_num, second_num, '-')
        elif first_num < second_num:
            return num(first_num, second_num, '/')
    return wrapper


@orifmetic
def ori(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


a = int(input('input first number: '))
b = int(input('input second number: '))
print(ori(a, b))
