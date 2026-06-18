# Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.

# Example 1:
# Input Format: arr[] = {1,2,4,7}, x = 6
# Result: 3
# Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

# Example 2:
# Input Format: arr[] = {1,2,4,7}, x = 2
# Result: 1
# Explanation: 2 is present in the array and so we will return its index i.e. 1

from typing import List

class Solution:
    def insert_position(self,arr:List[int],elem):
        low=0
        high=len(arr) - 1
        ans=len(arr)
        while(low<=high):
            mid = (low + high) // 2
            if (arr[mid] >= elem):
                ans=mid
                high=mid - 1
            else:
                low = mid + 1
        return ans
                

if __name__=="__main__":
    myobj=Solution()
    arr=[1,2,4,7]
    element=6
    print(myobj.insert_position(arr,element))
            