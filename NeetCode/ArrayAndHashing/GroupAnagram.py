from collections import defaultdict
from typing import List
class Solution:

    """
    Time & Space Complexity for Sorting
        Time complexity: O(m*nlogn)
        Space complexity: O(m*n)
        Where m is the number of strings and n is the length of the longest string.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

    """
    Time & Space Complexity for HashTable
        Time complexity: O(m*n)
        Space complexity: O(m)
        Where m is the number of strings and n is the length of the longest string.
    """
    def groupAnagramsHashTable(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

if __name__=="__main__":
    myobj=Solution()
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(myobj.groupAnagrams(strs))
    print(myobj.groupAnagramsHashTable(strs))
