from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        TIME: Always O(n) as we iterate over each n (every time we shrink by 1 left or right)
        SPACE: Always O(1) as only a few constants (pointers, counters, etc)
        ##two-pointers
        """
        # The largest container should always be checked from the widest window first
        # Therefore use the 2-pointer strat (shrinking window)
        # PSEUDO-CODE:
        #   1x while loop for 2-pointer strat
        #   Each iteration save the current area (always on first time, only if > than prev onwards)
        #   Shrink left OR right, the shorter side as the taller side can support a larger area
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            # length (shortest height) * width (distance between l & r)
            length = min(height[left], height[right])
            width = right - left
            curr_area = length * width
            max_area = max(curr_area, max_area)
            left_is_shorter = height[left] == length
            if left_is_shorter:
                left += 1
            else:
                right -= 1
        return max_area
