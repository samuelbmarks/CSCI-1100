def fib(n):
    if n <= 1:
        return n
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

if __name__ == "__main__":
    print(fib(0))
    print(fib(1))
    print(fib(2))
    print(fib(5))
    print(fib(10))
