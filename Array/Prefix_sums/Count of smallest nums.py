class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        new_list = []

        for index_1 in range(len(nums)):
            count = 0

            for index_2 in range(index_1 + 1, len(nums)):

                if nums[index_2] < nums[index_1]:
                    count += 1

            new_list.append(count)
        return new_list


nums = [5, 2, 6, 1]
solution = Solution()
result = solution.countSmaller(nums)
print("Count of smallest numbers After self:", result)
