# Binary search is only applicable in a sorted search space. 
#The sorted search space does not necessarily have to be a sorted array. It can be anything but the search space must be sorted.
# In binary search, we generally divide the search space into two equal halves and then try to locate which half contains the target. According to that, we shrink the search space size.

#O(logN), where N = size of the given array.

# Note:
#Interviewr might ask what if the size is big 2^32 the in that case low+high//2 will overflow
#in that case we have to go with this approach
#mid=high+((low - high)//2)
from typing import List
class Solution:
    def findelement(self,nums:List[int],target:int)->int:
        n=len(nums)
        low=0
        high=n-1
        while low <= high:
            #mid=(low+high)//2 #this can lead to overflow
            mid=high+((low - high)//2) #case for where size is bigger
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] <  target:
                low = mid + 1
            else:
                high=mid - 1
        return -1
    
    #Recursive Approach
    #So the overall time complexity is O(logN), where N = size of the given array.
    def recursivefindelement(self,nums:List[int],low,high,target):
        if low > high: return -1

        mid=(low + high )//2

        if nums[mid] == target : return mid

        elif nums[mid] < target:
            return self.recursivefindelement(nums,mid + 1,high,target)
        else:
            return self.recursivefindelement(nums,low,mid - 1 ,target)


if __name__ == "__main__":
    a=[1,2,3,4,6,7,7,7]
    target=7
    abc=Solution()
    #ind=abc.findelement(a,target)
    ind=abc.recursivefindelement(a,0,len(a) -1,target)
    if ind == -1:
        print("Recursive approach: The target is not present")
    else:
        print("recursive Approach: Target is present at ",ind)

    ind2=abc.findelement(a,target)
    if ind2 == -1:
        print("Normal Approach: The target is not present")
    else:
        print("Normal Approach: Target is present at ",ind2)   



