"""
Description
Given an array of integers nums and an integer target, return the indices i and j such
that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the
condition.

Return the answer with the smaller index first.

"""
from typing import List
class Solution:

    """
    Time & Space Complexity for brutforce
    Time complexity: O(n*2)
    Space complexity: O(1)
    """
    def twosumbruteforce(self,myitem:List[int],target: int)->List[int]:
        for i in range(len(myitem)):
            for j in range(i+1,len(myitem)):
                if myitem[i] + myitem[j] == target:
                    return [i,j]
        return[]

    """
    Time & Space Complexity for sorting
    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    def twosumsorting(self,nums:List[int],target:int)->List[int]:
        A=[]
        for i,num in enumerate(nums):
            A.append([num,i])
        A.sort()

        i,j=0,len(nums) - 1
        while i < j:
            cur=A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1],A[j][1]),
                max(A[i][1],A[j][1])]
            elif cur < target:
                i+=1
            else:
                j-=1
        return []


    """
    Time & Space Complexity two sum
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def twoSumhashmap(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

    """
    Time & Space Complexity optimal
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def towsumhashmapoptimal(selfself,nums:List[int],target:int)->List[int]:
        indices={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in indices:
                return [indices[diff],i]
            else:
                indices[n]=i
        return[]


if __name__=="__main__":
    myobj=Solution()
    input=[4,5,6]
    target=10
    print(myobj.twosumbruteforce(input,target))
    print(myobj.twosumsorting(input, target))
    print(myobj.twoSumhashmap(input, target))
    print(myobj.towsumhashmapoptimal(input, target))




