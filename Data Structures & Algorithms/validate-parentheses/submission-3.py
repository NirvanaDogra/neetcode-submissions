class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        for i in s[1:]:
            if len(stack) != 0:
                if i == "}" and stack[-1]=="{":
                    stack.pop()
                elif i == ']' and stack[-1]=='[':
                    stack.pop()
                elif i == ")" and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        print(stack)
        return len(stack) == 0

        