def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    otp = input("Enter operation (+, -, *, /): ")
    if otp == "+":
        print(a + b)
    elif otp == "-":
        print(a - b)
    elif otp == "*":
        print(a * b)
    elif otp == "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print(a / b)
    else:
        print("Invalid operation")
calculator()


