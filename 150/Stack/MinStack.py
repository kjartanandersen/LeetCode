
class MinStack:

    def __init__(self):
        pass
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

if __name__ == "__main__":

    minStack = MinStack()
    print("Start: " + str(minStack.stack))
    minStack.push(1)
    print("After push(1): " + str(minStack.stack))
    minStack.push(2)
    print("After push(2): " + str(minStack.stack))
    minStack.push(0)
    print("After push(0): " + str(minStack.stack))
    print("getMin(): " + str(minStack.getMin())) # return 0
    minStack.pop()
    print("After pop(): " + str(minStack.stack))
    print("top(): " + str(minStack.top()))       # return 2                      
    print("getMin(): " + str(minStack.getMin())) # return 1
    
    
    

    