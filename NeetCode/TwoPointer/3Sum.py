#Link
#https://leetcode.com/problems/3sum/description/
from collections import defaultdict
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

    def threeSumHashMap(self,nums:List[int])->List[List[int]]:
        nums.sort()
        count=defaultdict(int)

        for num in nums:
            count[num] += 1

        res=[]
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res

    def threesumTwoPointer(self,nums:List[int])->List[List[int]]:
        res=[]
        nums.sort()

        for i,a in enumerate(nums):
            if a > 0:
                break

            if i>0 and a== nums[i-1]:
                continue

            l,r=i+1,len(nums) - 1

            while l < r:
                threeSum=a + nums[i] + nums[r]
                if threeSum > 0 :
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l-1] and l < r:
                        l +=1

        return  res


if __name__=="__main__":
    obj=Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    nums2=[-3,3,4,-3,1,2]
    print(obj.threeSumBrutForce(nums))
    print(obj.threeSumBrutForce(nums2))
    print(obj.threeSumHashMap(nums))
    print(obj.threesumTwoPointer(nums))

