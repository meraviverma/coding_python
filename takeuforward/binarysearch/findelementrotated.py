# Problem Statement: Given an integer array arr of size N, sorted in ascending 
# order (with distinct values) and a target value k. Now the array is rotated at some 
# pivot point unknown to you. Find the index at which k is present and if k is not present return -1.

from typing import List

class findelemntrotate:
    #O(n)
    #Linear Search
    def findelelmnt(self,nums:List[int],elem:int)->int:
        for i in range(len(nums)):
            if(nums[i] == elem):
                return i
            
        return -1
    
    #O(log(n))
    def findelementbs(self,nums:List[int],elem:int)->int:
        low=0
        high=len(nums)-1

        while(low <= high):
            mid=(low+high)//2
            if(nums[mid] == elem):
                return mid

            #If mid element is greater than low then it means left part is sorted
            if(nums[low] <= nums[mid]):
                if(nums[low] <= elem and elem <= nums[mid]):
                    high=mid - 1
                else:
                    low = mid+1
            else:
                if(nums[mid] <= elem and elem <= nums[high]):
                    low=mid +1
                else:
                    high = mid -1
        return -1


if __name__=="__main__":
    a=[8,9,10,1,2,3,4,6,7]
    target=1
    abc=findelemntrotate()
    index=abc.findelementbs(a,target)
    if index == -1:
        print("Element Not FOund")
    else:
        print("Element Found at Index: ",index)


