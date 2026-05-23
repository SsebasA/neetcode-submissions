class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = [0] * 26
        maxLength = 0 
        left = 0
        max_f = 0
        right = 0

        while right < len(s):
            idx = ord(s[right]) - ord('A')
            maxFreq[idx] += 1
            len_window = right - left + 1
            max_f = max(max_f, maxFreq[idx])
            if (len_window - max_f) > k:
                idx = ord(s[left]) - ord('A')
                maxFreq[idx] -= 1
                left += 1
            else:
                maxLength = max(len_window, maxLength)
            
            right += 1
            
        return maxLength
        
        

