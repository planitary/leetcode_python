from typing import List
import random

def quick_sort(nums:List[int], left,right):
    if left >= right:
        return
    mid = partition(nums,left,right)
    # 迭代左子列
    quick_sort(nums,left,mid - 1)
    # 迭代右子列
    quick_sort(nums,mid + 1,right)

def partition(nums:List[int], left,right) -> int:
    pivotal = left
    pivotal_val = nums[left]
    while left < right:
        # 从右往左找到一个比基准值小的，从左往右找到一个比基准值大的，找到后交换二者位置
        while left < right and nums[right] >= pivotal_val:
            right -= 1
        while left < right and nums[left] <= pivotal_val:
            left += 1
        nums[left],nums[right] = nums[right],nums[left]
        # // 遍历结束时，左右指针相遇的位置即为基准值欲插入的位置
    nums[left],nums[pivotal] = nums[pivotal],nums[left]
    return left

if __name__ == "__main__":
    ll = []
    for i in range(8):
        value = random.randint(0,100)
        ll.append(value)
    print("排序前:",ll)
    quick_sort(ll, 0, len(ll) - 1)
    print("排序后:",ll)