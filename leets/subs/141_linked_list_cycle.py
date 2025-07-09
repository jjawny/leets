from typing import Optional
from leets.shared.list_node import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        See TS version for Big O

        #linked-lists
        """
        if not head or not head.next:
            return False
        
        tortoise, hare = head, head.next
        
        while tortoise.next and hare.next and hare.next.next:
            if tortoise == hare:
                return True
            tortoise = tortoise.next
            hare = hare.next.next
        
        return False
