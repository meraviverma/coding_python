class StackTut:
    def create_stack(self):
        stack=[]
        return stack
    def check_empty(self,stack):
        return len(stack)==0
    def push(self,stack,item):
        stack.append(item)
        print("pushed item:" + str(item))
    def pop(self,stack):
        if(self.check_empty(stack)):
            return "stack is empty"

        return stack.pop()

    def print_stack(self, stack):
        print("Stack (top → bottom):", list(reversed(stack)))


if __name__=="__main__":
    obj=StackTut()
    stack=obj.create_stack()
    obj.push(stack,3)
    obj.push(stack,5)
    obj.push(stack,40)
    obj.print_stack(stack)

    obj.pop(stack)
    obj.print_stack(stack)

