""""
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请不要使用除法，且在 O(n) 时间复杂度内完成此题。
示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenth = len(nums)
        left_ll, right_ll = [],[]
        left_ll.append(1)
        right_ll.append(1)
        for i in range(lenth - 1):
            left_ll.append(nums[i] * left_ll[i])
        nums.reverse()
        for j in range(lenth - 1):
            right_ll.append(nums[j] * right_ll[j])
        right_ll.reverse()
        for k in range(lenth):
            nums[k] = left_ll[k] * right_ll[k]
        return nums

s = Solution()
ll = [-1,1,0,-3,3]
print(s.productExceptSelf(ll))