# Given an array of integers nums and an integer target, return indices of the two numbers such that they
# add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element
# twice.
# You can return the answer in any order.
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
from typing import List


class TwoSum:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        prevMap={} #val : index ## Initilize a Dictionary

        for i,n in enumerate(nums): ##Using enumerate loop through the List(i is the index 0 and n will will value at
            # index 0 and so on
            diff=target-n # Target - element at index 0
            if diff in prevMap: # If difference is present in Dictionary
                return [prevMap[diff],i]
            prevMap[n]=i # If that number is not seen before insert into prevMap with key as that value and value as
            # index where it was seen in List {2:0}

        return

if __name__=='__main__':
    abc=TwoSum()
    print(abc.twoSum([2,7,11,15],9))