import time,re
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib (n - 2)

if __name__ == "__main__":

    s = "5123"
    pattern = re.compile(r"\d +")
    numbers = pattern.match(s)
    print(numbers)
    # print(numbers.group())
    # s = s[::-1]


    # while right < len(s):
    #     if s[right] == " ":
    #         while left < right - 1:
    #             s[left],s[right - 1] = s[right - 1],s[left]
    #             left += 1
    #             right -= 1
    #         left = right + 1
    #         right = left + 1
    #     right += 1
    # print(s)

