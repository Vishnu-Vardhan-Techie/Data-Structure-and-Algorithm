class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # 1. Use an array of size 128 (to cover all standard ASCII)
        target_counts = [0] * 128
        unique_t = 0
        for char in t:
            index = ord(char)
            if target_counts[index] == 0:
                unique_t += 1
            target_counts[index] += 1
        
        # 2. Window state
        window_counts = [0] * 128
        formed = 0
        left = 0
        min_len = float('inf')
        res = (0, 0)
        
        # 3. Slide Right
        for right in range(len(s)):
            char_index = ord(s[right])
            window_counts[char_index] += 1
            
            # If current character's frequency matches the target
            if target_counts[char_index] > 0 and window_counts[char_index] == target_counts[char_index]:
                formed += 1
            
            # 4. Shrink Left
            while formed == unique_t:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = (left, right)
                
                left_index = ord(s[left])
                window_counts[left_index] -= 1
                
                # If we lose a required character's frequency
                if target_counts[left_index] > 0 and window_counts[left_index] < target_counts[left_index]:
                    formed -= 1
                
                left += 1
                
        start, end = res
        return s[start:end+1] if min_len != float('inf') else ""

s = "ADOBECODEBANC"
t = "ABC"
solution = Solution()
print(solution.minWindow(s, t))