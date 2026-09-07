class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)

        # Equal subsets are impossible
        if total % k != 0:
            return False

        target = total // k

        # Larger numbers first for faster backtracking
        nums.sort(reverse=True)

        # If the largest number is bigger than target
        if nums[0] > target:
            return False

        buckets = [0] * k

        def backtrack(index):
            # All numbers are placed successfully
            if index == len(nums):
                return True

            num = nums[index]

            for i in range(k):

                # Cannot exceed target
                if buckets[i] + num <= target:

                    buckets[i] += num

                    if backtrack(index + 1):
                        return True

                    # Undo choice
                    buckets[i] -= num

                # Avoid trying other empty buckets
                if buckets[i] == 0:
                    break

            return False

        return backtrack(0)