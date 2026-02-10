def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibo = fib()
count = 1

while count < 100001:
    count += 1
    num = next(fibo)
    if count in (5, 200, 1000):
        print(num)
