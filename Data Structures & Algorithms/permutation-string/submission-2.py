class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        s1_count = [0] * 26
        window_count = [0] * 26
        left = 0
        right = n 

        for ch in s1:
            idx = ord(ch) - ord('a')
            s1_count[idx] += 1
        
        for i in range(n):
            idx = ord(s2[i]) - ord('a')
            window_count[idx] += 1

        if s1_count == window_count:
            return True

        while right < len(s2):
            window_count[(ord(s2[left]) - ord('a'))] -= 1
            window_count[(ord(s2[right]) - ord('a'))] += 1

            if s1_count == window_count:
                return True

            right += 1
            left += 1
        
        return False
