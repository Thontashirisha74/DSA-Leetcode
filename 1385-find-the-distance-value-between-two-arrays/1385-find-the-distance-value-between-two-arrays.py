class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ans=0
        for x in arr1:
            i=bisect_left(arr2,x)
            if i<len(arr2) and abs(arr2[i]-x)<=d:
                continue
            if i>0 and abs(arr2[i-1]-x)<=d:
                continue
            ans+=1
        return ans
        