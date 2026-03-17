class Solution:
    def characterReplacement(self, s:str, k: int) -> int:
        if k == 0 or not s:
            return 0
            
        char_counts = {}
        left = 0
        max_len = 0
    
        for right in range(len(s)):
            char_counts[s[right]] = char_counts.get(s[right], 0) + 1
            
            while len(char_counts) > k:
                char_counts[s[left]] -= 1
                if char_counts[s[left]] == 0:
                    del char_counts[s[left]]
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len


s = 'eceba'
k = 2
solution = Solution()
print(solution.characterReplacement(s, k))