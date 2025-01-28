"""
https://leetcode.com/problems/product-of-array-except-self/

Description
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in
O(n)
O(n) time without using the division operation?
"""
from typing import List

class Solution:
    """
    Time & Space Complexity for brutforce
    Time complexity: O(n*2)
    Space complexity: O(1)
    """
    def ProductExceptSelfBruteForce(self,arr):
        finalarr=[1]*len(arr)
        for i in range(len(arr)):
            finalarr[i] = 1
            for j in range(len(arr)):
                if(j!=i):
                    finalarr[i] = finalarr[i] * arr[j]
        return finalarr

    """
        Time & Space Complexity for brutforce
        Time complexity: O(n)
        Space complexity: O(1)
    """

    def ProductExceptSelfPrefixSufix(self,nums:List[int])->List[int]:
        res=[1]*len(nums)

        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix *= nums[i]
        postfix=1
        for i in range(len(nums) - 1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res




if __name__=="__main__":
    obj=Solution()
    arr=[1,2,4,6]
    arr2=[-1,0,1,2,3]
    print(obj.ProductExceptSelfBruteForce(arr))
    print(obj.ProductExceptSelfBruteForce(arr2))

    print(obj.ProductExceptSelfPrefixSufix(arr))
    print(obj.ProductExceptSelfPrefixSufix(arr2))

