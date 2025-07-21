from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        TIME: Always O(n) to iterate once
        SPACE: Always O(1) as in-place mutation (no copies/extra space of size n used)

        ##two-pointers
        """
        # Q is unnecessarily (seems intentionally) confusing...
        # TLDR we need to:
        #   - Mutate the nums in place
        #   - 'shifting' all unique items to the start, rest is ignored
        #   - Maintain asc order
        #   - Return the length (k)
        # Q checks the nums after mutation and the k we return
        if not nums:
            return 0

        # next_valid_idx is the next slot
        #   to shift a newly encountered num into
        #   this also acts as the total count
        i, next_valid_idx = 1, 1
        while i < len(nums):
            # Bcuz we maintain asc order, we can easily check the prev num for dupes, safe as i starts at 1
            prev = nums[i - 1]
            if prev != nums[i]:
                nums[next_valid_idx] = nums[i]
                next_valid_idx += 1
            i += 1
        return next_valid_idx
