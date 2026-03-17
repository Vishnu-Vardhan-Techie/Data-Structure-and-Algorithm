class Solution:
    def longestPalindrome(self, s:str) -> str:
        result = ""
        result_length = 0

        for index in range(len(s)):
            # Odd Length

            left, right = index, index
            while left >= 0 and right < len(s) and s[left]==s[right]:

                if (right - left + 1) > result_length:
                    result = s[left:right + 1]
                    result_length = right - left + 1

                left -= 1
                right += 1

            # Even Length

            left, right = index, index + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:

                if (right - left + 1) > result_length:
                    result = s[left:right + 1]
                    result_length = right - left + 1
                
                left -= 1
                right += 1

        return result
 
s = "babad"
solution = Solution()
print(solution.longestPalindrome(s))