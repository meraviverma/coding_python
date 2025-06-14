class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''

if __name__=="__main__":
    s = "([{}])"
    myobj=Solution()
    myobj.isValid(s)
    