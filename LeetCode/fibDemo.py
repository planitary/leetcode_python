
def fib_num(num):
    nl = []
    if num == 0:
        nl.append(num)
        return 0
    if num == 1:
        nl.append(num)
        return 1
    else:
        nl.append(num)
        return fib_num(num - 1) + fib_num(num - 2)

print(fib_num(15))


