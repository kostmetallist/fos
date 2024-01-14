from time import sleep


def decorator(*params):
    def decorator_wrappee(func):
        def inner(*args, **kwargs):

            print(f'Sum of decorator\'s params: {sum(params)}')
            func(*args, **kwargs)

        return inner
    return decorator_wrappee


@decorator(1, 2, 3, 4, 5)
def callee(arg):
    print(f"I'm processing {arg}...")
    sleep(2)
    return arg


if __name__ == '__main__':
    callee(42)
