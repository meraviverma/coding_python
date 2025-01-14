from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

if __name__=="__main__":
    myobj=Solution()
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(myobj.groupAnagrams(strs))
