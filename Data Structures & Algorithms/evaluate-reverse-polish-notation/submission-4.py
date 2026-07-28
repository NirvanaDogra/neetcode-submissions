class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sumVal = 0
        for i in tokens:
            if i == '+':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                print(val1, val2)
                print(val1+val2)
                stack.append(val1+val2)

            elif i == '-':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                print(val1, val2)
                print(val1-val2)
                stack.append(val2-val1)
            
            elif i == '*':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                print(val1, val2)
                print(val1*val2)
                stack.append(val2*val1)
            
            elif i == '/':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                print(val1, val2)
                print(val2/val1)
                stack.append(val2/val1)
                
            else:
                stack.append(int(i))

            print(stack)
        return int(stack[0])