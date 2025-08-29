import math
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        See TS version for Big O

        ##sliding-window ##two-pointers ##binary-search
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            halfwayAmountBetweenLeftAndRight = math.floor((right - left) / 2)
            mid = left + halfwayAmountBetweenLeftAndRight
            midNum = nums[mid]
            
            if target == midNum:
                return mid
            elif target < midNum:
                right = mid - 1
            elif target > midNum:
                left = mid + 1
        
        return -1