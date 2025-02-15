#Link
#https://leetcode.com/problems/3sum/description/

#
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
#

from typing import List
class Solution:

    #Brut Force
    """
       Time & Space Complexity for Sorting
           Time complexity: O(n*n*n)
           Space complexity: O(m)
           here m is the number of triplets and n is the length of the given array.
    """
    def threeSumBrutForce(self,nums:List[int])->List[List[int]]:
        res=set()
        nums.sort()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp=[nums[i],nums[j],nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]

if __name__=="__main__":
    obj=Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(obj.threeSumBrutForce(nums))

