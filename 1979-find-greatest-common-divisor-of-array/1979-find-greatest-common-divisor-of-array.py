import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small=min(nums)
        lar=max(nums)
        gcd=math.gcd(small,lar)
        return gcd
        