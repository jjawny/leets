class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        ##two-pointers ##sliding-window ##hashmap
        """
        # PSEUDO CODE:
        # 1. Prepare s1 for comparison (s1's hashmap of chars n counts)
        # 2. Use a loop to build each window (window's hashmap of chars n counts)
        # 3. After each window is built, check if hashmaps match
        # 4.1. Yes? valid permutation
        # 4.2. No? reset and slide window up
        
        # EXAMPLE:
        # s1 = "abc"
        # s2 = "aaaabc"
        # Loop index 0: window is "aaa" → ❌ mismatch → reset
        # Loop index 1: window is "aaa" again → ❌ mismatch → reset
        # Loop index 2: window is "aab" → ❌ mismatch → reset
        # Loop index 3, window is "abc" → ✅ match → return True
        
        s1_hashmap, s2_hashmap = {}, {}
        for char in s1:
            increment(s1_hashmap, char)

        left, right = 0, 0
        while right < len(s2):
            increment(s2_hashmap, s2[right])
            sliding_window_len = (right - left) + 1

            # Continue building the current window's hashmap
            if sliding_window_len != len(s1):
                right += 1
                continue

            # Success case
            if s2_hashmap == s1_hashmap:
                return True
            
            # Reset case
            s2_hashmap.clear()
            left += 1
            right = left
        return False

def increment(hashmap_ref, char):
    hashmap_ref[char] = hashmap_ref.get(char, 0) + 1