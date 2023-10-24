"""
峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
示例 1：

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
示例 2：

输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
"""
from typing import List


class Solution:
    # 注意隐藏信息，数组左右越界处均为无穷小，意味着我们只要向数值大的方向找，始终能找到一个拐点
    # 使用二分查找每次缩小一个区间段，向左或向右查找（这里向左），比较前一个数和当前数的大小
    # 前一个数大，左边存在峰值，缩小右区间，当前值大，右侧存在峰值，缩小左区间
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0,len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
        return left

if __name__ == "__main__":
    s =Solution()
    nums:List[int] = [1,2,1,3,5,6,4]
    print(s.findPeakElement(nums))
