import sys


"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。"""
class Solution:
    def reverse(self, x: int) -> int:

        s = str(x)
        negative_signal_s = ""
        # 判断是否含有负号
        if s[0] == "-":
            negative_signal_s = s[0]
            s = s[1:]
        reverse_s = s[::-1]
        negative_signal_s += reverse_s
        if int(negative_signal_s) < -2 ** 31 or int(negative_signal_s) > 2 ** 31 - 1:
            return 0
        else:
            return int(negative_signal_s)

    def reverse2(self,x : int) -> int:
        flag_x = (1 << 31) -1
        if x < 0:
            flag_x = 1 << 31
        abs_x = abs(x)
        y = 0
        while abs_x != 0:
            y = y * 10 + abs_x % 10
            if y > flag_x :
                return 0
            abs_x //= 10
        return y if x > 0 else -y



    # def temp(self,s):
    #     print(s)
    #     print(-2*31)
    #     return str(s) < str(-2 ** 31)

s = Solution()
# print(s.reverse(0))
# print(s.temp(-123))

print(s.reverse2(0))