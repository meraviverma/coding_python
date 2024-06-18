from typing import List

class Solution:
    def groupAnagram(self,strs: List[str])->List[List[str]]:
        mp={}
        ans=[]
        #print(''.join(sorted(strs)))

        for s in strs:
            sorted_str=''.join(sorted(s))
            #sorted_str=sorted(s)
            #print(sorted_str)
            if sorted_str in mp:
                ans[mp[sorted_str]].append(s)
            else:
                mp[sorted_str]=len(ans)
                ans.append([s])
        return ans
    
if __name__=='__main__':
    abc=Solution()
    print(abc.groupAnagram(["eat","tea","tan","ate","nat","bat"]))