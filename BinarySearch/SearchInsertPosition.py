# Given a sorted array and a target value, return the index if the
# target is found. If not, return the index where it would be if it were
# inserted in order. You may assume no duplicates in the array.
#
#
# Example:
#
#
# Input: [1,3,5,6], 5
# Output: 2
# Input: [1,3,5,6], 2
# Output: 1

from typing import List
def SearchInsert(nums:List[int],target:int)->int:
    left,right=0,len(nums)
    while left < right:
        mid=left+(right-left)//2
        if nums[mid] >= target:
            right=mid
        else:
            left = mid + 1
    return left

if __name__=="__main__":
    arr=[1,3,5,6]
    search_elem=2
    print(SearchInsert(arr,search_elem))
