#Give a array of element return the distinct element
# Example
# 1:
#
# Input: nums = [1, 2, 3, 1]
# Output: [1,2,3]

# Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: [1,2,3,4]

from typing import List
class Solution:
    def return_distinct_element(self,num:List[int])->List[int]:
        myhashset=set()

        for n in num:
            if n not in myhashset:
                myhashset.add(n)



        return myhashset

if __name__=='__main__':
    abc=Solution()
    print(abc.return_distinct_element([1, 2, 3, 1]))
    print(abc.return_distinct_element([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))