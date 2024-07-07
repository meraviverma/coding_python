# The lower bound algorithm finds the first or the smallest index in a sorted 
#array where the value at that index is greater than or equal to a given key i.e. x.
from typing import List
class Solution:
    #Time Complexity: O(N), where N = size of the given array.
    #Space Complexity: O(1) as we are using no extra space.
    def lowerbound(self,nums:List[int],target:int)->int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

    #optimal approach        
    def optimallowerbound(self,nums:List[int],target:int)->int:
        low=0
        high=len(nums) - 1
        ans=len(nums)

        while low <=high:
            mid=(low + high) // 2
            if nums[mid] >= target:
                ans=mid

                high=mid-1
            else:
                low = mid +1
        return ans
        

if __name__=="__main__":
    a=[1,2,3,4,6,7,7,7]
    target=9
    abc=Solution()
    print(abc.lowerbound(a,target))

    print(abc.optimallowerbound(a,target))