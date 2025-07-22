from collections import defaultdict
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        TIME: Always O(n + m + log k) for initial loop, heapify, and popping
        MEMORY: Worst-case O(n) for the hashmap if all nums are unique
        ##heap ##hashmap
        """

        # 1. Count at O(n)
        hashmap = defaultdict(int) # default to 0s
        for n in nums:
            hashmap[n] += 1
        
        # 2. Extracting k largest sounds like a max heap solution
        #    Prepare the heap (a list) with negative so max is at top during heapify
        heap = [(-count, num) for num, count in hashmap.items()]
        heapq.heapify(heap)

        # 3. Each heap pop is O(log m), so O(k * log m)
        response = []
        for i in range(k):
            response.append(heapq.heappop(heap)[1])

        return response
