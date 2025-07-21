from typing import List, Set, Tuple

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        TIME: Always O(n^2) as the nested loops cost the most, sorting is cheaper at O(n log n)
        SPACE: Worst-case O(n^2) when every possible triplet exists
        """
        # DEBRIEF:
        # Q asks us to find all 3 num combos (order-insensitive) where sum (a + b + c) = 0
        # Q samples reassurance that order DOES NOT MATTER! (win)
        # Remembering 2Sum, we can iterate O(n) over nums (this is our 'a' num), and perform 2Sum to get 'b' and 'c'
        # ALGO SUMMARY:
        #   Store triplets in a set (set of tuples to be hashable)
        #       this is how we avoid dupe triplets
        #   Pre-sort nums once prior, why?:
        #       Allows us to avoid dupes in outer-loop
        #       Allows us to use 2-pointer strat in 2Sum fn calls
        #   For each iteration:
        #       Outer loop gives us our starting number 'a'
        #       Get the remainder (a + ? = 0)
        #       Call 2Sum fn with the remainder
        #       2Sum uses a 2 pointer strat (shrinking window)
        #       2Sum gives us all pairs (b + c = ?)
        #       These are our triplets (a + b + c = 0)
        triplets: Set[Tuple[int, int, int]] = set()
        nums_sorted = sorted(nums)

        # Outer-loop - the first num 'a' in our triplet
        for a_idx, a in enumerate(nums_sorted):
            # bcuz nums is sorted, skip if the previous num is the same num (already processed)
            if a_idx > 0 and a == nums_sorted[a_idx - 1]:
                continue
            remainder_to_zero = flip(a)
            valid_pairs = twoSum(nums_sorted, remainder_to_zero, a_idx)
            for pair in valid_pairs:
                b, c = pair
                triplets.add((a, b, c))

        return [list(t) for t in triplets]

def flip(num):
    return -num

def twoSum(nums_sorted: List[int], target_sum: int, a_idx: int) -> List[Tuple[int, int]]:
    # Only process (start the window) to the right of a's index
    #   why? this won't miss any pairs (run through on paper)
    left, right = a_idx + 1, len(nums_sorted) - 1
    valid_pairs: List[Tuple[int, int]] = []

    while left < right:
        b, c = nums_sorted[left], nums_sorted[right]
        curr_sum = b + c

        if curr_sum == target_sum:
            valid_pairs.append((b, c))
            # Shrink both ways
            left += 1
            right -= 1
        # Shrink either way
        elif target_sum < curr_sum:
            right -= 1
        else:
            left += 1
    return valid_pairs
