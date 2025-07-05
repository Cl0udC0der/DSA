# 1 <= n <= 8
# It simulates a tree of depth 2n (where the end nodes denote the correct possible combinations)
#only add open parenthesis if open < n, only add close if close < open
# valid IIF open == closed == n

#If you map out the viable end results, there are rules that you will inevitably follow. 
# 1) Add an open parenthesis if open < n, add close if close < open
# 2) Ending condition IIF open == close ==n
# So you apply the rule to a closure function to maintain state of stack and result while p
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res
            