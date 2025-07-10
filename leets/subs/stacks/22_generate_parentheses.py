from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        BIG O:
          If a backtracking algo restricts branches to valid permutations ONLY
          the space/time is O(number of valid perms)
          there are 4ⁿ / √n valid perms because:
            - There is a total of 2^(2n) possible states for strings w '(' and ')'
            - But because we restrict to valid perms, this becomes Catalan number of possible states
            - so space/time is O(4ⁿ / √n)

        ##stacks ##backtracking
        """
        result = []

        # Topics hint at backtracking or DP... (doing backtracking v)
        # This is like DFSing but we actually generate the tree as we search
        # The tree is each combo/permutation, and we need rules for when
        #   to branch and when to stop
        def backtrack(string="", n_opened=0, n_closed=0):
            # We must have a condition for when to stop (find valid permutations)
            #   valid = all pairs are closed = we need strings w len 2x n
            if len(string) == n * 2:
                result.append(string)
                return
            
            # Conditions for all next valid possible permutations
            # Each recursive call branches down 2 paths: add opening or closing bracket
            # Always run opening bracket case first as starting w a closing bracket is invalid
            if n_opened < n:
                backtrack(string + "(", n_opened + 1, n_closed)
            if n_closed < n_opened:
                backtrack(string + ")", n_opened, n_closed + 1)

        backtrack()
        return result