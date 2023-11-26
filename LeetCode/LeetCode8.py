"""
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
 *
 * 函数 myAtoi(string s) 的算法如下：
 *
 * 读入字符串并丢弃无用的前导空格
 * 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
 * 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
 * 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
 * 如果整数数超过 32 位有符号整数范围 [−2^31,  2^31 − 1] ，需要截断这个整数，使其保持在这个范围内。
 * 具体来说，小于 −2^31 的整数应该被固定为 −2^31 ，大于 2^31 − 1 的整数应该被固定为 2^31 − 1 。
 * 返回整数作为最终结果。
 * 注意：
 *
 * 本题中的空白字符只包括空格字符 ' ' 。
 * 除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
"""
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        # 先去除多余的空格，读取第一位来确定符号
        s = s.strip()
        if s == "":
            return 0
        sign: str = s[0]
        if sign == "-" or sign == "+":
            s = s[1:]
        if s == "" or not s[0].isdigit():
            return 0
        # 读取到的值进行累加，python中的int没有固定的位数，理论上可以存储无限的位数
        left_min = -2 ** 31
        right_max = 2 ** 31 - 1
        boundary = right_max // 10
        str_sum = 0
        for i in range(len(s)):
            if s[i].isdigit():
                if str_sum > boundary or str_sum == boundary and int(s[i]) > 7:
                    if sign == '-':
                        return left_min
                    else:
                        return right_max
                else:
                    str_sum = str_sum * 10 + int(s[i])
            else:
                break
        if sign == "-":
            return -1 * int(str_sum)
        return int(str_sum)


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("2147483646"))
