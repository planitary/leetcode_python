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
            value = int(i) + int(num2[j]) + int(col)
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

    # 将位数少的那个作为乘数(参与单个运算，竖式的下方）
    def is_multiplier(self, num1: str, num2: str) -> str:
        return num2 if len(num1) > len(num2) else num1

    # 位数多的为被乘数（循环运算，竖式的上方）
    def is_multiplicand(self, num1: str, num2: str) -> str:
        return num1 if len(num1) > len(num2) else num2

    def multiply(self, num1: str, num2: str) -> str:
        multiplier = self.is_multiplier(num1, num2)
        multiplicand = self.is_multiplicand(num1,num2)
        global res_value
        exit_flag = len(multiplier) - 1
        # 部分和的另一个加数
        part_sum = "0"
        while exit_flag >= 0:
            col = 0
            multi_str = ""
            for i in reversed(multiplicand):
                value = int(i) * int(multiplier[exit_flag]) + col
                col = 0
                if value >= 10:
                    # 积的结果取余数，进位为商
                    res_value = value % 10
                    col = value // 10
                else:
                    res_value = value
                multi_str += str(res_value)
            # 高位进位判断
            if col != 0:
                multi_str += str(col)
            # 反转结果参与部分和的运算并判断是否需要补0
            # 补0规则：最低位不补0,即每次运算后的部分和 * 10的n次方，n从0开始递增
            multi_str = multi_str[::-1]
            multi_str = int(multi_str) * (10 ** (len(multiplier) - 1 - exit_flag))
            # 计算部分和
            # print(multi_str)
            part_sum = self.addStrings(str(multi_str), part_sum)
            exit_flag -= 1
        return part_sum


s = Solution()
print(s.multiply("123", "456"))
