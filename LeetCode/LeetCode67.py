"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
示例 1：

输入:a = "11", b = "1"
输出："100"
示例 2：

输入：a = "1010", b = "1011"
输出："10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dis = len(a) - len(b)
        if dis > 0:
            b = "0" * abs(dis) + b
        else:
            a = "0" * abs(dis) + a
        j = len(b) - 1
        res = ""
        col = 0
        a = a[::-1]
        for i in range(len(a)):
            value = int(a[i]) + int(b[j]) + col
            col = 0
            if  value > 1:
                value %= 2
                col = 1
            res += str(value)
            j -= 1
        if col == 1:
            res += str(col)
        res = res[::-1]
        return res

s = Solution()
print(s.addBinary("1", "111"))