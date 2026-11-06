from collections import defaultdict

class Solution:
    def countServers(self,n,logs,x,queries):
        logs.sort(key=lambda a:a[1])
        arr=sorted((q,i) for i,q in enumerate(queries))
        cnt=defaultdict(int)
        ans=[0]*len(queries)
        l=r=active=0

        for q,i in arr:
            while r<len(logs) and logs[r][1]<=q:
                s=logs[r][0]
                if cnt[s]==0:
                    active+=1
                cnt[s]+=1
                r+=1

            while l<r and logs[l][1]<q-x:
                s=logs[l][0]
                cnt[s]-=1
                if cnt[s]==0:
                    active-=1
                l+=1

            ans[i]=n-active

        return ans