"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
 * <p>
 * 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
 * <p>
 * 你可以假设除了整数 0 之外，这个整数不会以零开头。
 * <p>
 * 示例 1：
 * <p>
 * 输入：digits = [1,2,3]
 * 输出：[1,2,4]
 * 解释：输入数组表示数字 123。
 * 示例 2：
 * <p>
 * 输入：digits = [4,3,2,1]
 * 输出：[4,3,2,2]
 * 解释：输入数组表示数字 4321。
 * 示例 3：
 * <p>
 * 输入：digits = [0]
 * 输出：[1]
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 末尾非9的情况
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1
            return digits
        # 末尾为9，处理循环进位
        n = len(digits) - 1
        col = 0
        digits[n] += 1
        while n >= 0:
            digits[n] += col
            if digits[n] > 9:
                digits[n] = 0
                col = 1
            else:
                col = 0
            n -= 1
        if digits[0] == 0:
            digits.insert(0,1)
        return digits

if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([9,9]))

