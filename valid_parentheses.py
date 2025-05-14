class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if not c in bracketMap:
                stack.append(c)
            else:
                if stack and stack[-1] == bracketMap[c]:
                    stack.pop()
                else:
                    return False

        return not stack
