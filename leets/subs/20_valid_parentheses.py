class Solution:
    def isValid(self, s: str) -> bool:
        """
        TIME: Always O(n) - loop through each char
        MEMORY: Worst-case O(n) - no brackets close

        ##stacks
        """
        # A string is just a list (as in we should loop over chars)
        # We will use another DS while we loop as a mirror of the input (that we can mutate)
        # We will add each open bracket, but as soon as we add a close bracket we 
        #   attempt to pop (should correspond if valid) basically it's FILO for open brackets
        #   so use a stack
        stack = []

        # Use a hashmap for O(1) lookups on pairs (as we know AOT)
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        # Example run through for a valid s = '({[]})':
        #   (     PUSH!
        #   ({    PUSH!
        #   ({[   PUSH!
        #   ({[]  POP!
        #   ({}   POP!
        #   ()    POP!
        #   _     EMPTY!
        for char in s:
            canClose = char in pairs and stack and stack[-1] == pairs[char]
            if canClose:
                stack.pop()
                continue
            
            stack.append(char)

        return len(stack) == 0