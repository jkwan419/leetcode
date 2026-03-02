class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {"}": "{", "]": "[", ")": "("}

        for c in s:
            if not c in bracket_map:
                stack.append(c)
            else:
                if stack and stack[-1] == bracket_map[c]:
                    stack.pop()
                else:
                    return False

        return not stack
