# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
#
# Example
# 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example
# 2:
#
# Input: s = "rat", t = "car"
# Output: false

#Using all the character of s we can create t. If it is possible we call it as anagram

class Solution:
    def validanagram(self,str1:str,str2:str)->bool:

        if(len(str1) != len(str2)):
            return False
        myhashmap1,myhashmap2={},{}

        for i in range(len(str1)):
                myhashmap1[str1[i]]=1+myhashmap1.get(str1[i],0)
                myhashmap2[str2[i]] = 1 + myhashmap2.get(str2[i], 0)
        for c in myhashmap1:
            if myhashmap1[c] != myhashmap2.get(c,0):
                return False

        return True
