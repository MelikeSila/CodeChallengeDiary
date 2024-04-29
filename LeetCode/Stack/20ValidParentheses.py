class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) <= 1:
            return False

        from collections import deque

        stack = deque()
        stack.append(s[0])
        math_dict = { 
            ")" : "(", 
            "]" : "[",
            "}" : "{"
            }
        
        for i in range(1, len(s)):
            if s[i] == ")" or s[i] == "]" or s[i] == "}":
                if not stack or stack.pop() != math_dict[s[i]]:
                    return False
            else:
                stack.append(s[i])
        
        if len(stack) != 0:
            return False

        return True


