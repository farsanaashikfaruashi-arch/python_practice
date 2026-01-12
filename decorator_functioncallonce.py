called = 0
def hello():
    global called
    if called == 0:
        print("Hello")
        called = 1
    else:
        print("Good")
hello()
hello()
