from typing import List


class Solution:
    # 从头开始巡检，遇到相同的，记录其下标后从列表里剔除
    def removeElement(self, nums: List[int], val: int) -> int:
        ll_size = len(nums)
        if ll_size == 1:
            if nums[0] != val:
                return ll_size
        i = 0
        while i <= ll_size - 1:
            if nums[i] == val:
                nums.remove(nums[i])
                ll_size -= 1
            else:
                i += 1
        return ll_size

ll = [0,1,2,2,3,0,4,2]
s = Solution()
print(s.removeElement(ll, 2))
print(ll)