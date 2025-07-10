from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int | None:
        """
        TIME: Always O(n) as we loop over all tokens
        MEMORY: Worst-case O(n) for the stack if no operator tokens (no pops to eval etc)

        ##stacks ##hashmaps
        """
        # So every operator encountered means we pops the stack twice,
        #   eval the nums, then pushes the result back
        stack: List[int] = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue
            
            # FYI num_2 is popped first
            num_2 = safe_pop(stack)
            num_1 = safe_pop(stack)

            # Do not use falsey checks here as nums could be 0 (valid)
            if num_1 is None or num_2 is None:
                continue
            
            res = None

            match token:
                case "+":
                    res = num_1 + num_2
                case "-":
                    res = num_1 - num_2
                case "*":
                    res = num_1 * num_2
                case "/":
                    # "The division between two integers always truncates toward zero."
                    #   aka we need to ensure floats are rounded down to ints
                    res = int(num_1 / num_2)

            print(f"{num_1} {token} {num_2} = {res}")
            
            if res is not None:
              stack.append(res)
        return stack.pop() if stack else None

def safe_pop(stack: List) -> int | None:
    return stack.pop() if len(stack) > 0 else None