class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n=len(nums)
        k=(1<<30)-1
        for i in range(n):
            if nums[i]!=i:
                k&=nums[i]
        return k if k!=(1<<30)-1 else 0