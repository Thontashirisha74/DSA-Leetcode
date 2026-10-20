class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n=len(nums)
        a=sorted(nums)
        ans=0
        def is_rotation(x,y):
            k=len(x)
            t=x+x[:-1]
            lps=[0]*k
            j=0
            for i in range(1,k):
                while j and y[i]!=y[j]:
                    j=lps[j-1]
                if y[i]==y[j]:
                    j+=1
                    lps[i]=j
            j=0
            for v in t:
                while j and v!=y[j]:
                    j=lps[j-1]
                if v==y[j]:
                    j+=1
                    if j==k:
                        return True
            return False
        for k in range(1,n+1):
            if n%k==0 and all(is_rotation(nums[i:i+k],a[i:i+k]) for i in range(0,n,k)):
                ans+=k
        return ans