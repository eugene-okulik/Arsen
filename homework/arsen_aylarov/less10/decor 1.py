def fin(func):

    def inner():
        print('started')
        func()
        print('finished')
    return inner

@fin
def printer():
    print('other line')

printer()

