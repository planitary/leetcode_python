"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
"""
from typing import List
import random

"""
快速选择算法，类似快速排序
"""
class Solution:
    # 因为切割函数将大的元素放在了左边，所以每次只需寻找基准值左侧的序列就行
    # 如果基准值的下标比k大，说明左侧一定存在第K大的元素（因为左侧都是大值）
    # 如果基准值的下标比K小，说明找过了，需要去右侧重新找（此时再往左侧找无意义，因为都是比第K个元素还大的值)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left ,right = 0,len(nums) - 1
        while left <= right:
            pivotal_index = self.partiton(nums,left,right)
            if pivotal_index == k - 1:
                return nums[pivotal_index]
            elif pivotal_index < k - 1:
                left = pivotal_index + 1
                # 对于有大量重复的值连续出现时，在向右寻找的过程中，若出现重复的值，则直接跳过，不在参与划分
                while left < k - 1 and nums[left] == nums[left - 1]:
                    left += 1
            else:
                # 同理，对于有大量重复的值连续出现时，在向左寻找的过程中，若出现重复的值则直接跳过
                right = pivotal_index - 1
                while right > k - 1 and nums[right] == nums[right + 1]:
                    right -= 1

    # 选取最右边的元素作为基准值，将大于基准值的元素放左边,小于基准值的元素继续遍历
    # 这里不交换小于基准值的元素是因为最后一步交换基准值后就可以保证左侧元素大于基准值，右侧元素小于基准值
    def partiton(self,nums:List[int],left,right) -> int:
        i = left
        pivotal_val = nums[right]
        for j in range(left, right):
            if nums[j] >= pivotal_val:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
        # 遍历完成后，基准值位置确定，基准值与i处的位置交换后即可得到基准值当前的位置（即i的值）
        nums[i],nums[right] = nums[right],nums[i]
        return i

if __name__ == "__main__":
    s = Solution()
    ll = [3,1,2,4]
    # for i in range(10):
    #     ll.append(random.randint(0,50))
    print(ll)
    new_ll :List[int] = sorted(ll,reverse= True)
    print(new_ll)
    print(s.findKthLargest(ll, 2))
