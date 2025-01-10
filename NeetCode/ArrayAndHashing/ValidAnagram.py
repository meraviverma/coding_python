"""
Given two strings s and t, return true if the two strings are anagrams of each other,
otherwise return false.

An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.
"""
from typing import List


class Solution:
    """
           Time complexity: O(nlogn + mlogm)
           space complexity: O(1) or O(n+m) depends on sorting algorithm
        """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    """
        Time complexity: O(n+m)
        space complexity: O(1)
        """

    def isAnagramhashtable(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

    """
        Time complexity: O(n+m)
        space complexity: O(1)
        """

    def isAnagramhashtableoptimal(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True


if __name__ == "__main__":
    s = "racecar"
    t = "carrace"
    s1 = "jar"
    t1 = "jam"
    myobj = Solution()
    print(myobj.isAnagram(s, t))
    print(myobj.isAnagram(s1, t1))

    print(myobj.isAnagramhashtable(s, t))
    print(myobj.isAnagramhashtable(s1, t1))

    print(myobj.isAnagramhashtableoptimal(s, t))
    print(myobj.isAnagramhashtableoptimal(s1, t1))
