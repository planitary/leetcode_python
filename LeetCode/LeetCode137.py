"""
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
 *
 * 你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。
 *
 * 示例 1：
 *
 * 输入：nums = [2,2,3,2]
 * 输出：3
 * 示例 2：
 *
 * 输入：nums = [0,1,0,1,0,1,99]
 * 输出：99
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_d = {}
        for i in range(len(nums)):
            if nums[i] not in num_d:
                num_d[nums[i]] = 1
            else:
                count = num_d.get(nums[i])
                num_d[nums[i]] = count + 1
        for k,v in num_d.items():
            if v == 1:
                return k

if __name__ == "__main__":
    s = Solution()
    nums = [2,2,3,2]
    print(s.singleNumber(nums))