"""
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
 *
 * 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
 *
 * 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
 * 示例 1：
 *
 * 输入：x = 4
 * 输出：2
 * 示例 2：
 *
 * 输入：x = 8
 * 输出：2
 * 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        half_x = x / 2
        i = 0
        res = 1
        while i <= half_x + 1:
            if i * i > x :
                res = i - 1
                break
            if i * i == x:
                res = i
                break
            i += 1
        return res

    def mySqrtOpt(self,x :int) -> int:
        # // 二分查找，每次查找当前值的一半，并进行比较，若当前值的平方大于x，缩短右区间；若小于x，缩短左区间
        start,end = 0,x
        mid = x // 2
        while start <= mid:
            # 平方>x,缩短右区间
            if mid * mid > x:
                end = mid - 1
            # 平方<x,缩短左区间
            elif mid * mid < x:
                start = mid + 1
            elif mid * mid == x:
                break
            mid = (start + end) // 2
        return mid

if __name__ == "__main__":
    s = Solution()
    print(s.mySqrtOpt(8))