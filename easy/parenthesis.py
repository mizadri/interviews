class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(":")", "[":"]", "{":"}"}
        for bracket in s:
            if bracket in brackets:
                stack.append(brackets[bracket])
            else:
                if len(stack) > 0 and stack[-1] == bracket:
                    stack.pop()
                else:
                    return False
                    
        if len(stack) == 0:
            return True
        else:
            return False