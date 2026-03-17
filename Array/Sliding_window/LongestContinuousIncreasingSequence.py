class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        current_streak = 1
        max_length = 1
        for index in range(1, len(nums)):

            if nums[index] > nums[index - 1]:
                current_streak += 1
            else:
                current_streak = 1

            max_length = max(max_length, current_streak)

        return max_length


nums = [1, 3, 5, 4, 7]
solution = Solution()
result = solution.findLengthOfLCIS(nums)
print(f"The Longest Continuous Increase Sequence is: {result}")
