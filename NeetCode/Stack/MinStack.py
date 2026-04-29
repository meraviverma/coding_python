# Design a stack class that supports the push, pop, top, and getMin operations.
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in
# O
# (
# 1
# )
# O(1) time.
# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
#
# Output: [null,null,null,null,0,null,2,1]

class minstack:
    def __init__(self):
        self.min=float('inf')
        self.stack=[]
    def push(self,val)->None:
        if not self.stack:
            self.stack.append(0)
            self.min=val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min=val
    def pop(self)-> None:
        if not self.stack:
            return
        pop =self.stack.pop()

        if pop < 0:
            self.min =self.min - pop

    def top(self)-> int:
        top=self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min
    def getMin(self)->int:
        return self.min

if __name__=="__main__":
    obj=minstack()
    commands= ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
    output=[]

    obj = None
    i = 0
    while i < len(commands):
        cmd = commands[i]
        if cmd == "MinStack":
            obj = minstack()
            output.append(None)
        elif cmd == "push":
            val = commands[i + 1]
            obj.push(val)
            output.append(None)
            i += 1  # skip the value
        elif cmd == "pop":
            obj.pop()
            output.append(None)
        elif cmd == "top":
            output.append(obj.top())
        elif cmd == "getMin":
            output.append(obj.getMin())
        i += 1

    print("Output:", output)
