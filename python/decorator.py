# Let's compose a decorator with the following responsibilities:
#  1. Measurement of inner function's execution time
#  2. Printing out diagnostic information about the callee


from time import perf_counter, sleep


def decorator(func):
    def inner(*args, **kwargs):

        time_started = perf_counter()
        func(*args, **kwargs)
        print(f'Execution of `{func.__name__}` took {perf_counter() - time_started:.3f}s')

    return inner


# Is a syntactic sugar. Just an alternate form of `callee = decorator(callee)`.
@decorator
def callee(arg):
    print(f"I'm processing {arg}...")
    sleep(2)
    return arg


if __name__ == '__main__':
    callee(42)
