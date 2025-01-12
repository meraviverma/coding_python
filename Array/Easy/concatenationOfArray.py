# https://leetcode.com/problems/concatenation-of-array/
#
# Given an integer array nums of length n, you want to create an array ans of length 2n
# where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
#
# Return the array ans.
# Example 1:
#
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:
#
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]

from typing import List

class Solution:
    def concatenationofarray(self,myitem:List[int])->List[int]:
        newitem=[]
        n=len(myitem)
        for i in range(len(myitem)):
            newitem.insert(i,myitem[i])
            newitem.insert(i+n,myitem[i])

        return newitem

    def concatenationofarray_solution2(self, myitem:List[int]) -> List[int]:
        #Two copies of array need to be copied into a single array
        newitem=[]
        for i in range(2):#If you want to append x times instead of 2 pass x
            for n in myitem:
                newitem.append(n)

        return newitem

    def concatenationofarray_solution3(self, myitem:List[int]) -> List[int]:
        return myitem*2


if __name__=='__main__':
    myobj=Solution()
    print(myobj.concatenationofarray([1,2,1]))
    print(myobj.concatenationofarray_solution2([1, 2, 1]))
    print(myobj.concatenationofarray_solution3([1, 2, 1]))