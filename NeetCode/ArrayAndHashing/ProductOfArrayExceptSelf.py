from typing import List
class Solution:
    def productofself(self,arr):
        finalarr=[1]*len(arr)
        for i in range(len(arr)):
            finalarr[i] = 1
            for j in range(len(arr)):
                if(j!=i):
                    finalarr[i] = finalarr[i] * arr[j]
        return finalarr



if __name__=="__main__":
    obj=Solution()
    arr=[1,2,4,6]
    arr2=[-1,0,1,2,3]
    print(obj.productofself(arr))
    print(obj.productofself(arr2))
