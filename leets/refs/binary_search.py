from typing import List, Optional


def binary_search(sorted_arr: List[int], target: int) -> Optional[int]:
  left_idx, right_idx = 0, len(sorted_arr) - 1
  found_idx = None # Start w not found

  while left_idx <= right_idx and not found_idx:
    mid_idx = (left_idx + right_idx) // 2
    mid = sorted_arr[mid_idx]
  
    if target == mid:
      found_idx = mid_idx
    elif target > mid:
      left_idx = mid_idx + 1
    else:
      right_idx = mid_idx - 1

  return found_idx
