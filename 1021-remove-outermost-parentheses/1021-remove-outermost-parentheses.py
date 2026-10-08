class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        d=0
        for c in s:
            if c=="(":
                if d:
                    ans+=c
                d+=1
            else:
                d-=1
                if d:
                    ans+=c
        return ans