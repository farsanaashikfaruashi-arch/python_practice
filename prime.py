def prime(n):
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime number")
            return
    print("Prime number")
prime(5)
