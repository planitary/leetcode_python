from typing import List


class Insert:
    def binaryInsert(self,nums:List[int], x:int):
        nums.sort()
        start,end = 0,len(nums) - 1
        mid = end // 2
        while start <= mid:
            if x < nums[mid]:
                end = mid - 1
            elif x > nums[mid]:
                start = mid + 1
            elif x == nums[mid]:
                break
            mid = (start + end) // 2
        # 找到了插入的位置
        nums.insert(mid,x)

if __name__ == "__main__":
    s = Insert()
    nums = [12,44,25,7,89,30,26,9,42]
    nums.sort()
    print("插入前:",nums)
    s.binaryInsert(nums,30)
    nums.sort()
    print("插入后:",nums)