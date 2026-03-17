class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        longest = 0

        for index in range(1, len(arr) - 1):

            if arr[index - 1] < arr[index] > arr[index + 1]:

                left = index - 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                right = index + 1
                while right < len(arr) - 1 and arr[right + 1] > arr[right]:
                    right += 1

                current_mountain_length = right - left + 1
                longest = max(longest, current_mountain_length)

        return longest


test_array = [2, 1, 4, 7, 3, 2, 5]
solution = Solution()
result = solution.longestMountain(test_array)
print(f"The longest Mountain length is: {result}")
