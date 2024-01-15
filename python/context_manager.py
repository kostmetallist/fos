# At the very minimum, a context manager must 
# implement the following methods:
#  1. `__enter__`
#  2. `__exit__`


from traceback import print_tb


class FileManager:
    def __init__(self, *args):
        self.opened_file = open(*args)

    def __enter__(self):
        return self.opened_file

    def __exit__(self, type_, value, traceback):

        if value:
            print(*[
                'The following exception was detected:',
                f'{type_.__name__}: {value}',
            ], sep='\n')
            print_tb(traceback)

        self.opened_file.close()
        # Indicating the exception has been handled gracefully
        return True


if __name__ == '__main__':
    with FileManager('../LICENSE', 'r') as f:
        print(*f.readlines())

    with FileManager('../LICENSE', 'r') as f:
        # Explicitly raise an exception
        f.call_apriori_undefined_method()
