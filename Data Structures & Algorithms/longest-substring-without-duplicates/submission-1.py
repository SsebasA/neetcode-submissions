class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        
        max_length = 1
        left = 0
        right = 0
        seen = set()

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            if s[right] not in seen:
                seen.add(s[right])
                curr_len = right - left + 1
                max_length = max(curr_len, max_length)
                right += 1
        
        return max_length