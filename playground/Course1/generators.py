def MyRangeGenerator(top):
    current = 0
    while current < top:
        yield current
        current += 1

# ==============   COROUTINES   ==================

'''def grep(pattern):
    print('start grep')
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('coroutine is closed')'''

def grep(pattern):
    print('grep started')
    while True:
        line = yield
        if pattern in line:
            print(line)


def grep_coroutine():
    g = grep('ttt')
    yield from g


def chain(x_iter, y_iter):
    yield from x_iter
    yield from y_iter

a = [1, 2, 3]
b = (4, 5)

for i in chain(a, b):
    print(i)
