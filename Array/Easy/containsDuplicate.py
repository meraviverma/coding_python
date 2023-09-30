# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Example
# 1:
#
# Input: nums = [1, 2, 3, 1]
# Output: true
# Example
# 2:
#
# Input: nums = [1, 2, 3, 4]
# Output: false
# Example
# 3:
#
# Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true

# Time Complexity : o(n*2)
# Space Complexity : O(1)

# If we sort the array any duplicate if exist we have to iterate
# only once i.e. just check the neighbours
#
# TImeComplexit:
# O(nLog(n))
#
# Space Complexit:
# O(1) if we dont consider the space of sorting

#We can use Hashset and then check if element exist or not and if
#it doesn't exist insert into hashset.
# TimeComplexity: O(n)
# SpaceComplexity: O(n)

from typing import List

class Solution:
    def containsDuplicate(self,nums:List[int])->bool:
        prevmap={}
        for i,n in enumerate(nums):
            if n in prevmap:
                return True
            else:
                prevmap[i]=n

        return False

    def containduplicateusinghashset(self,nums:List[int])->bool:
        myhashset=set()

        for n in nums:
            if n in myhashset:
                return True
            myhashset.add(n)
        return False



if __name__=='__main__':
    abc=Solution()
    print(abc.containsDuplicate([1, 2, 3, 1]))
    print(abc.containduplicateusinghashset([1, 2, 3, 1]))
