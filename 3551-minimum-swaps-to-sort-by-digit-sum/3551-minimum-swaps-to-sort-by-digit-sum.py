class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        a=sorted(nums,key=lambda x:(sum(map(int,str(x))),x))
        pos={x:i for i,x in enumerate(a)}
        vis=[False]*n
        ans=0
        for i in range(n):
            if vis[i] or pos[nums[i]]==i:
                continue
            j=i
            size=0
            while not vis[j]:
                vis[j]=True
                j=pos[nums[j]]
                size+=1
            ans+=size-1
        return ans