class Solution:
    def largestNumber(self, nums):

        str_nums = []
        for num in nums:
            str_nums.append(str(num))

        self._quick_sort(str_nums, 0, len(str_nums) - 1)

        result = ""
        for s in str_nums:
            result += s

        if result == "" or result[0] == "0":
            return "0"

        return result

    def _quick_sort(self, arr, low, high):
        if low < high:
            pivot_index = self._partition(arr, low, high)
            self._quick_sort(arr, low, pivot_index - 1)
            self._quick_sort(arr, pivot_index + 1, high)

    def _partition(self, arr, low, high):

        pivot = arr[high]
        i = low - 1

        for j in range(low, high):

            if arr[j] + pivot > pivot + arr[j]:
                i += 1

                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

        temp = arr[i + 1]
        arr[i + 1] = arr[high]
        arr[high] = temp
        return i + 1


# --- Code to run in VS Code ---

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1

    test_1 = [3, 30, 34, 5, 9]
    print(f"Input: {test_1} | Output: {solution.largestNumber(test_1)}")

    # Test Case 2

    test_2 = [0, 0]
    print(f"Input: {test_2}    | Output: {solution.largestNumber(test_2)}")
