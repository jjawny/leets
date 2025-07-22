from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a hashmap to keep track of annagram lists
        # Loop s in strs:
        #   Create a sorted s (for hashmap lookup)
        #   If not found aka new annagram?
        #       k = sorted, v = unsorted (for response)
        #   If found aka permutation of existing annagram?
        #       append unsorted to list

        hashmap = {}
        for s in strs:
            s_sorted = ''.join(sorted(s))
            # Add to existing list
            if s_sorted in hashmap:
                hashmap[s_sorted].append(s)
                continue
            # Add to new list
            hashmap[s_sorted] = [s]
        return [v for k, v in hashmap.items()]
