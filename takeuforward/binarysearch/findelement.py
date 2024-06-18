from typing import List
class Solution:
    def findelement(self,nums:List[int],target)->int:
        n=len(nums)
        low=0
        high=n-1
        while low <= high:
            mid=(low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] <  target:
                low = mid + 1
            else:
                high=mid +1
        return -1
    

if __name__ == "__main__":
    a=[1,2,3,4,6,7,7,7]
    target=7
    abc=Solution()
    ind=abc.findelement(a,target)
    if ind == -1:
        print("The target is not present")
    else:
        print("Target is present at ",ind)


