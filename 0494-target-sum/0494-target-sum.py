class Solution:
    def findTargetSumWays(self, nums, target):

        memo = {}

        def dfs(index, current_sum):

            if index == len(nums):
                if current_sum == target:
                    return 1
                return 0

            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            add = dfs(index + 1, current_sum + nums[index])
            subtract = dfs(index + 1, current_sum - nums[index])

            memo[(index, current_sum)] = add + subtract

            return memo[(index, current_sum)]

        return dfs(0, 0)