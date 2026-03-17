class Solution:
    def maxScore(self, cardpoints: list[int], k: int) -> int:
        count = len(cardpoints)
        window_size = count - k

        current_window_sum = sum(cardpoints[:window_size])
        min_window_sum = current_window_sum

        for index in range(window_size, count):
            current_window_sum += cardpoints[index] - cardpoints[index - window_size]
            min_window_sum = min(min_window_sum, current_window_sum)

        return sum(cardpoints) - min_window_sum


cardpoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
points = Solution()
result = points.maxScore(cardpoints, k)
print(f"The Maximum points you can obtain from cards {result}")
