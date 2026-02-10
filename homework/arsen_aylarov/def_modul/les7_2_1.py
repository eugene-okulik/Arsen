def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

ff = fib()


count = 1

while count < 100001:
    count += 1
    num = next(ff)
    if count in (5, 200, 1000):
        print(num)
