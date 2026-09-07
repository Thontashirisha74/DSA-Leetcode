class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        if len(s) < k:
            return 0
        
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in count:
            
            if count[char] < k:
                
                parts = s.split(char)
                
                return max(
                    self.longestSubstring(part, k)
                    for part in parts
                )

        return len(s)