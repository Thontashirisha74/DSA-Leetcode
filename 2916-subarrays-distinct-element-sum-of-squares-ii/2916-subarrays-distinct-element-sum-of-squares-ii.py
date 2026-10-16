class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        mod=10**9+7
        n=len(nums)
        last={}
        tree=[0]*(4*n)
        lazy=[0]*(4*n)
        sq=[0]*(4*n)
        def update(o,l,r,L,R):
            if L<=l and r<=R:
                sq[o]=(sq[o]+2*tree[o]+r-l+1)%mod
                tree[o]=(tree[o]+r-l+1)%mod
                lazy[o]+=1
                return
            m=(l+r)//2
            if lazy[o]:
                for c,a,b in ((o*2,l,m),(o*2+1,m+1,r)):
                    sq[c]=(sq[c]+2*lazy[o]*tree[c]+lazy[o]*lazy[o]*(b-a+1))%mod
                    tree[c]=(tree[c]+lazy[o]*(b-a+1))%mod
                    lazy[c]+=lazy[o]
                lazy[o]=0
            if L<=m:
                update(o*2,l,m,L,R)
            if R>m:
                update(o*2+1,m+1,r,L,R)
            tree[o]=(tree[o*2]+tree[o*2+1])%mod
            sq[o]=(sq[o*2]+sq[o*2+1])%mod
        ans=0
        for i,x in enumerate(nums):
            update(1,0,n-1,last.get(x,-1)+1,i)
            last[x]=i
            ans=(ans+sq[1])%mod
        return ans