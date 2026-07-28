class MinStack:

    def __init__(self):
        self.stack = []
        self.minInsert = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minInsert) == 0:
            self.minInsert.append(val)
        else:
            self.minInsert.append(min(self.minInsert[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minInsert.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minInsert[-1]
        
