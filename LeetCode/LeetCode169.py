from typing import List
import collections
"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：

输入：nums = [3,2,3]
输出：3
示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = collections.Counter(nums)
        for k,v in num_count.items():
            if v > len(nums) / 2:
                return k

s = Solution()
ll = [2,2,4,2,4,4,4,5,4,4,6]
print(s.majorityElement(ll))