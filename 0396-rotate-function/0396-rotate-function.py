class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)

        total = sum(nums)

        current = 0

        for i in range(n):
            current += i * nums[i]

        maximum = current

        for i in range(n - 1, 0, -1):
            current = current + total - n * nums[i]
            maximum = max(maximum, current)

        return maximum