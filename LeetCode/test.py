import time
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib (n - 2)

if __name__ == "__main__":
    before = int(time.time() * 1000)
    print(before)
    time.sleep(3)
    after = int(time.time() * 1000)
    print(after)
    print((after - before) // 1000)