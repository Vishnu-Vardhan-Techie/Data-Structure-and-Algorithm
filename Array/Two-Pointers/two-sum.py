from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = len(nums)
        for i in range(count):
            for j in range(i + 1, count):
                if nums[i] + nums[j] == target:
                    return [i, j]

solution = Solution()
nums = [2,7,11,15]
target = 9
print(solution.twoSum(nums, target))