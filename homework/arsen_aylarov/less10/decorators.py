def decor(func):

    def wrapper(fin):
        for i in range(fin):
            func()
    return wrapper


@decor
def ll():
    print("hello")


ll(4)
