class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod=10**9+7
        n=len(nums)
        c=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            c[i][0]=c[i][i]=1
            for j in range(1,i):
                c[i][j]=(c[i-1][j-1]+c[i-1][j])%mod
        def dfs(a):
            if len(a)<3:
                return 1
            left=[x for x in a if x<a[0]]
            right=[x for x in a if x>a[0]]
            return c[len(left)+len(right)][len(left)]*dfs(left)%mod*dfs(right)%mod
        return (dfs(nums)-1)%mod