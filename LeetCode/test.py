def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib (n - 2)

if __name__ == "__main__":
    i = 0
    while i < 100:
        print(fib(i))
        i += 1