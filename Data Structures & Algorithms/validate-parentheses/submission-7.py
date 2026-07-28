class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBrackets = "([{"
        closeBrackets = ")]}"

        openCount = 0
        closeCount = 0
        for char in s:
            if openCount == closeCount and char in openBrackets:
                openCount+=1
                stack.append(char)
            elif openCount == closeCount and char in closeBrackets:
                return False
            elif openCount > closeCount:
                if char in openBrackets:
                    openCount+=1
                    stack.append(char)
                if char in closeBrackets:
                    closeCount+=1
                    posOpen = openBrackets.index(stack[-1])
                    posClose = closeBrackets.index(char)
                    
                    if posOpen != posClose:
                        return False
                    else:
                        stack.pop()

        print(openCount, closeCount)
        if openCount == closeCount:
            return True
        else:
            return False
 
            