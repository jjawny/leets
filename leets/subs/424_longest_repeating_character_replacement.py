from typing import Optional, Tuple


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        TIME: Always O(n) for the main loop
        SPACE: Worst-case O(26) = O(1) when HashmapWrapper's hashmap is full (A..Z)
        ##two-pointers ##sliding-window
        """
        # DEBRIEF:
        #   - Find the largest window
        #   - The largest window will be the combo of the most frequent char like 'A' + k any other chars before/after/in-between
        # PSUEDO CODE:
        #   - Keep track of the count of alpabet (A..Z) char count
        #   - For the most common char - keep track of the its key during updates to avoid future O(n) lookup
        #   - Formula: window - most_common_char_count = other_chars_count, if other_chars_count >= k, the window is valid
        #   - If not valid, capture the substring's length (if greater than previous max) and shift window up until valid again (decrease char count as the start/left pointer of window slides up)

        left = 0
        max_substring_len = 0
        hashmap_wrapper = HashmapWrapper()

        def is_valid(l, r):
            substring_len = (r - l) + 1 # +1 to include curr char (as 0-based indexed)
            most_frequent_char_count = hashmap_wrapper.top_char[1] if hashmap_wrapper.top_char else 0
            other_chars_allowed_count = substring_len - most_frequent_char_count
            return other_chars_allowed_count <= k

        for right in range(len(s)):
            char = s[right]
            hashmap_wrapper.increment(char)
            substring_len = right - left # +1 to include curr char (as 0-based indexed)
            max_substring_len = max(max_substring_len, substring_len)
            # Heal the window if it's invalid, moving the start/left until valid again
            while not is_valid(left, right):
                hashmap_wrapper.decrement(s[left])
                left += 1

        # Capture the final substring
        max_substring_len = max(max_substring_len, len(s) - left)

        return max_substring_len

# Use a wrapper to simplify our main algo
class HashmapWrapper:
    def __init__(self):
        self.hashmap = {}
        self.top_char: Optional[Tuple[str, int]] = None

    # Keeps top_char up-to-date at O(1)
    def increment(self, char):
        next_count = self.hashmap.get(char, 0) + 1
        self.hashmap[char] = next_count
        if not self.top_char or next_count > self.top_char[1]:
            self.top_char = (char, next_count)
    
    # Worst-case: O(26)
    # Keeps top_char up-to-date by iterating over all kv pairs for chars A..Z at most
    #   this only happens if we are updating top_char's char
    def decrement(self, char):
        next_count = self.hashmap.get(char, 1) - 1
        self.hashmap[char] = next_count
        if self.top_char and self.top_char[0] == char:
            for k, v in self.hashmap.items():
                if v > self.top_char[1]:
                    self.top_char = (k, v)
