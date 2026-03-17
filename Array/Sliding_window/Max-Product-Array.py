class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = max(nums)
        current_minimum = 1
        current_maximum = 1

        for value in nums:

            if value == 0:
                current_minimum = 1
                current_maximum = 1
                continue

            temporary_threshold = value * current_maximum
            current_maximum = max(
                value * current_maximum, value * current_minimum, value
            )
            current_minimum = min(temporary_threshold, value * current_minimum, value)

            result = max(result, current_maximum)

        return result


nums = [-2, 0, 1]
solution = Solution()
answer = solution.maxProduct(nums)
print(f"The Maximum Product SubArray: {answer}")
