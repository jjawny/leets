class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        TIME: Always O(n)
        SPACE: Worst-case O(n) if we encounter no dupes and store all n in seen_chars
        ##two-pointers ##sliding-window
        """
        # Q screams use a sliding window (2 pointers strat)
        # Track seen_chars in a hashmap as O(1) ops + ordered in Python 3.7+ (unlike Set)
        #   only keys are important, value is unused
        seen_chars = {}
        max_substring_len, left = 0, 0

        for right in range(len(s)):
            curr_char = s[right]
            if curr_char not in seen_chars:
                seen_chars[curr_char] = None # Value does not matter, use None for 16B mem
                continue
            # By here we encountered a dupe:
            #   1. Save the current substring length (if it's larger)
            substring_len = right - left
            max_substring_len = max(max_substring_len, substring_len)

            #   2. 'Heal' aka move the start of the window up/right until
            #       the dupe char (exclusive - dupe char is the next start)
            while s[left] != curr_char and left < right:
                if s[left] in seen_chars:
                    del seen_chars[s[left]]
                left += 1
            
            # Finally shift the start window past the duplicate char as 0-based index
            left += 1

        # Handle the final length (loop finished and no dupe was encountered right at the end)
        final_substring_len = len(s) - left
        max_substring_len = max(max_substring_len, final_substring_len)
        return max_substring_len
