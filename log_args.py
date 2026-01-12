def log_args(func):
    def wrapper(a, b):
        print("Arguments:", a, b)
        return func(a, b)
    return wrapper
@log_args
def add(a, b):
    return a + b
print(add(30, 40))

