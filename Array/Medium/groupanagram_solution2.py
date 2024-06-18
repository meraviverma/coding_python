import collections
from typing import List

class Solution:
    def groupAnagram(self,strs: List[str])->List[List[str]]:
        ans=collections.defaultdict(list)

        for s in strs:
            count=[0] * 26
            for c in s:
                count[ord(c) - ord("a")] +=1
            ans[tuple(count)].append(s)

        return ans.values()
    
if __name__=='__main__':
    abc=Solution()
    print(abc.groupAnagram(["eat","tea","tan","ate","nat","bat"]))
    