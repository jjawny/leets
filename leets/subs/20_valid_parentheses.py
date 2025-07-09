class Solution:
    def isValid(self, s: str) -> bool:
        """
        TIME: Always O(n) - loop through each char
        MEMORY: Worst-case O(n) - no brackets close

        ##stacks
        """
        # OPTIMIZATIONS:
        # Use early guards to avoid hitting the O(n) loop
        #   We can check if s is immediately invalid:
        #  - Must start with an open bracket
        #  - Must end with a close bracket
        #  - Must have an even length (all brackets should come in pairs)
        hasOpenBracketFirst = s and s[0] in "({["
        hasCloseBracketLast = s and s[-1] in ")}]"
        hasEvenLength = len(s) % 2 == 0

        if not (hasOpenBracketFirst and hasCloseBracketLast and hasEvenLength):
            return False

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
            shouldClose = char in pairs
            if shouldClose:
                canClose = stack and stack[-1] == pairs[char]
                if canClose:
                    stack.pop()
                    continue
                else:
                    return False
            
            stack.append(char)

        return len(stack) == 0