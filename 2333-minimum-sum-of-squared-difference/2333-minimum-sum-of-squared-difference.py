class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        d=[abs(a-b) for a,b in zip(nums1,nums2)]
        k=k1+k2
        if sum(d)<=k:
            return 0
        l,r=0,max(d)
        while l<r:
            m=(l+r)//2
            if sum(max(0,x-m) for x in d)<=k:
                r=m
            else:
                l=m+1
        ans=0
        for x in d:
            y=min(x,l)
            ans+=y*y
            k-=max(0,x-l)
        for x in d:
            if x>=l and k>0:
                ans-=l*l-(l-1)*(l-1)
                k-=1
        return ans