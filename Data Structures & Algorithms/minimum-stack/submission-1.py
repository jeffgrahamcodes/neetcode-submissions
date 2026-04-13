class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        del self.stack[-1]
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minimum = self.stack[0]

        for i in range(len(self.stack)):
            if self.stack[i] < minimum:
                minimum = self.stack[i]

        return minimum
        
