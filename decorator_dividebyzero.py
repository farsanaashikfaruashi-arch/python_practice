def no_zero(f):
    def w(a, b):
        if b == 0:
            print("Cannot divide by zero")
        else:
            f(a, b)
    return w
@no_zero
def divide(a, b):
    print(a / b)
divide(10, 2)
divide(10, 0)
