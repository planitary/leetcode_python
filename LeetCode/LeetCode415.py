"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。



示例 1：

输入：num1 = "11", num2 = "123"
输出："134"
示例 2：

输入：num1 = "456", num2 = "77"
输出："533"
示例 3：

输入：num1 = "0", num2 = "0"
输出："0"
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res_str = ""
        diff_length = len(num2) - len(num1)
        repeat_0 = "0" * abs(diff_length)
        if diff_length < 0:
            num2 = repeat_0 + num2
        if diff_length > 0:
            num1 = repeat_0 + num1
        # 进位标记
        col = 0
        j = len(num2) - 1
        for i in reversed(num1):
            # print(i)
            # print(reverse_num2)
            # print(col)
            value =  int(i) + int(num2[j]) + int(col)
            col = 0
            if value >= 10:
                value -= 10
                col = 1
            res_str += str(value)
            j -= 1
        # 计算完成后判断最高位是否有进位
        if col != 0:
            res_str += str(col)
        return res_str[::-1]

s = Solution()
print(s.addStrings("1", "9"))
