class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        TIME: O(n)
        SPACE: Worst-case O(n) if we encounter no dupes and store all of n in seen_chars
        ##two-pointers ##sliding-window
        """
        last_index = {}
        max_len = 0
        left = 0

        for right, char in enumerate(s):
            if char in last_index and last_index[char] >= left:
                left = last_index[char] + 1
            last_index[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
