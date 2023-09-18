"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_ll = []
        # 特判
        if len(nums) < 3:
            return res_ll
        length = len(nums)
        start = 0
        left = start + 1
        right = length -1
        nums.sort()
        while start < length and left < right and nums[start] <= 0:
            # // 遇到重复的值就跳过，如果新的初始指针和上一次相同，则必然结果和上次一样
            if start > 0 and nums[start] == nums[start - 1]:
                start += 1
                left = start + 1
                continue
            value = nums[start] + nums[left] + nums[right]
            if value < 0:
                left += 1
            elif value > 0:
                right -= 1
            elif value == 0:
                temp_ll = [nums[start],nums[left],nums[right]]
                res_ll.append(temp_ll)
                left += 1
                right -= 1
#               // 当前判断结束后，分别移动左右指针，判断左右指针是否和上一次的值一样
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
                while nums[right] == nums[right + 1] and left < right:
                    right -= 1
                # 当前循环没有结果，初始指针右移，右指针还原
            if left >= right:
                start += 1
                left = start + 1
                right = length - 1
        return res_ll

s = Solution()
print(s.threeSum([0,0,0,0]))
