
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        See TS version for Big O

        ##hashmaps
        """
        cache = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in cache:
                return [i, cache[diff]]
            cache[num] = i
        
        return []
