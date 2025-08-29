from typing import List


class Solution:
    """
    TIME: Always O(n) as we shrink the window either side each iteration
    SPACE: Always O(1) as no copies/extra space of size n used

    ##two-pointers
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if target == total:
                return [left + 1, right + 1] # +1 for 1-based indexed (unnecessary and stupid)
            elif target < total:
                right -= 1
            else:
                left += 1
        return [-1, -1]