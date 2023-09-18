"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。 不需要考虑数组中超出新长度后面的元素。
示例 2：

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3。不需要考虑数组中超出新长度后面的元素。
"""
from typing import List

# 同leetcode26的思路，只不过这次判断单位为后两个元素
class Solution:
    def removeDuplicates(self,nums: List[int]) -> int:
        if nums is None:
            return 0
        i = 0
        while i < len(nums) - 2:
            if nums[i + 2] == nums[i]:
                nums.remove(nums[i + 2])
            else:
                i += 1
        return len(nums)

s = Solution()
ll = [1,2,2,2]
print(s.removeDuplicates(ll))
print(ll)