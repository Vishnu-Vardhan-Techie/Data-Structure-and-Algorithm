class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curSum = numbers[left] + numbers[right]

            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return []


numbers = [2,7,11,15]
target = 9
solution = Solution()
result = solution.twoSum(numbers, target)
print(result)