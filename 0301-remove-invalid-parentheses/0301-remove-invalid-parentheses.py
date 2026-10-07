class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        result=[]
        def isValid(s):
            count=0
            for c in s:
                if c=="(":
                    count+=1
                elif c==")":
                    count-=1
                    if count<0:
                        return False
            return count==0
        def dfs(s,start,l_rem,r_rem):
            if l_rem==0 and r_rem==0:
                if isValid(s):
                    result.append(s)
                return
            for i in range(start,len(s)):
                if i>start and s[i]==s[i-1]:
                    continue
                if s[i]=="(" and l_rem:
                    dfs(s[:i]+s[i+1:],i,l_rem-1,r_rem)
                elif s[i]==")" and r_rem:
                    dfs(s[:i]+s[i+1:],i,l_rem,r_rem-1)
        l_rem=r_rem=0
        for c in s:
            if c=="(":
                l_rem+=1
            elif c==")":
                if l_rem:
                    l_rem-=1
                else:
                    r_rem+=1
        dfs(s,0,l_rem,r_rem)
        return result