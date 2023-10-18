"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
"""
import sys
from typing import List


# 滑动窗口优化：右指针依次进行累加，当超过指定值时，左指针移动，并将其从累加结果中删除，直到累加和重新小于指定值时，右指针再开始累加
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums) + 1
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] >=  target:
                return 1
            return 0
        left,right = 0,0
        sum = 0
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                min_length = min(min_length,right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        if min_length == len(nums) + 1:
            return 0
        return min_length

s = Solution()
print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))