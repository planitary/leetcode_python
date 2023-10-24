"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
"""
from typing import List


class Solution:
    # 进行两次二分查找，第一次查找起始位置，第二次查找结束位置
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right = 0,len(nums) - 1
        idx1,idx2 = -1,-1
        res:List[int] = [idx1,idx2]
        if len(nums) == 0:
            return res
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                idx1 = mid
                right = mid - 1

        # 还原左右指针
        left,right = 0,len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                idx2 = mid
                left = mid + 1
        res = [idx1,idx2]
        return res

if __name__ == "__main__":
    s =Solution()
    nums:List[int] = []
    print(s.searchRange(nums, 0))
