class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i == '(':
                stack.append('(')
            if i == ')':
                if(len(stack) == 0):
                    return False
                if stack.pop() != '(':
                    return False
                
            if i == '{':
                stack.append('{')   
            if i == '}':
                if(len(stack) == 0):
                    return False
                if stack.pop() != '{':
                    return False
                
            if i == '[':
                stack.append('[')    
            if i == ']':
                if(len(stack) == 0):
                    return False
                if stack.pop() != '[':
                    return False
        
        if len(stack) == 0:
            return True
        return False