class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length = 0
        left_pointer = 0
        sub_str = set()
        size = len(s)
        for i in range(size):
            while s[i] in sub_str:
                sub_str.remove(s[left_pointer])
                left_pointer+=1
            
            sub_str.add(s[i])
            max_length = max(max_length,i - left_pointer+1)
        return max_length
