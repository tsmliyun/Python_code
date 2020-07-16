def new_tips(argv):
    def tips(func):
        def nei(a, b):
            print('start %s' % argv)
            func(a, b)
            print('stop')

        return nei

    return tips


@new_tips('add')
def add(a, b):
    print(a + b)


@new_tips('sub')
def sub(a, b):
    print(a - b)


print(add(4, 5))
print(sub(8, 5))
