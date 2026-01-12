def positive_number(func):
    def wrapper(n):
        if n>0:
            func(n)
        else:
            print(" positive numbers ")
    return wrapper
@positive_number
def square(n):
    print(n * n)
square(15)
square(-3)
