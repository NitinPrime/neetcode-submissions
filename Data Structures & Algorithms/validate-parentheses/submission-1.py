class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        resp = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in resp:
                if stack and stack[-1] == resp[c]:
                    stack.pop()
                
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False