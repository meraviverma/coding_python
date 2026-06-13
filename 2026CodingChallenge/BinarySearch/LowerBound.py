# Implement Lower Bound

# 23
# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

# What is lower bound?
# The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

# The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.

# Example 1:
# Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
# Result: 1
# Explanation: Index 1 is the smallest index such that arr[1] >= x.

# Example 2:
# Input Format: N = 5, arr[] = {3,5,8,15,19}, x = 9
# Result: 3
# Explanation: Index 3 is the smallest index such that arr[3] >= x.

from typing import List


class Solution:
    def lower_bound(self,arr:List[int],target):
        low=0
        high=len(arr) - 1
        ans=len(arr)
        
        while low <= high:
            mid = (low + high)//2
            if (arr[mid] >= target):
                ans=mid
                high=mid - 1
            else:
                low = mid + 1
        return ans
       

if __name__=="__main__":
    obj=Solution()
    arr=[3,6,8,9,21,43]
    target=9
    print(obj.lower_bound(arr,target))