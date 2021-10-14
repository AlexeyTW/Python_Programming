import sys, functools


def logger(func):
    @functools.wraps(func)
    def writer(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'w') as file:
            file.write(str(result))
        return result
    return writer


def logger_with_param(filename):
    def decorator(func):
        def writer(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as file:
                file.write(str(result))
            return result
        return writer
    return decorator


def first_decorator(func):
    def wrapper():
        print('This is the first decorator')
        return func()
    return wrapper


def second_decorator(func):
    def wrapper():
        print('This is the second decorator')
        return func()
    return wrapper

@first_decorator
@second_decorator
def decorated():
    print('Finally Called ...')


decorated()