class Solution:
    def minInsertions(self, s: str) -> int:
        ans=right=0
        i=0
        while i<len(s):
            if s[i]=="(":
                right+=2
                if right%2:
                    ans+=1
                    right-=1
            else:
                right-=1
                if right<0:
                    ans+=1
                    right=1
            i+=1
        return ans+right