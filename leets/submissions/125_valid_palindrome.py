class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        TIME: Always O(n/2) = O(n) when window shrinks (both ends) each iteration
        SPACE: Always O(1) as using pointers only

        ##two-pointers
        """
        # We need 2 pointers closing in on the mid point
        #   ^ Handles even n odd cases
        # Loop with each iteration:
        #   moving pointers 1 char
        #   moving pointers until the next alpha-num char
        #   lowercase the chars and compare
        left = 0
        right = len(s) - 1
        while left < right:
            # Iterate left and right inwards
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1
            
            # By here we have 2 valid apha-num chars to compare
            if s[left].lower() != s[right].lower():
                return False
            
            # Progress for the next iteration
            left += 1
            right -= 1
        return True