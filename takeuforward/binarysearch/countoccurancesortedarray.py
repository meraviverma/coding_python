from typing import List
class Solution:
    #brute force approach
    #time complexity O(n)
    #space complexity O(1)
    def findelement(self,arr:[int],n:int,x:int)->int:
        cnt=0
        for i in range(n):
            if arr[i]==x:
                cnt+=1

        return cnt
    
    #optimal approach
    def findelementoptimal(self,arr:[int],n:int,x:int)->int:
        low=0
        high=len()

    
if __name__ == "__main__":
    arr=[2,4,6,8,8,8,11]
    n=7
    x=8

    abc=Solution()
    ans=abc.findelement(arr,n,x)  
    print(ans) 
    

