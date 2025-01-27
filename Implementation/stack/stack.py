
class Stack():

    def __init__(self):     # initialize the stack upon creating an object
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
        # return not self.items

    def __str__(self):
        return str(self.items)



if __name__ == "__main__":
    stack = Stack()
    print("\nInitial Stack size -", stack.size())

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print("After pushing -", stack)

    stack.pop()
    print("After poping -", stack)

    print("Stack size -", stack.size())

    print("Stack peek -", stack.peek())

    print("Is stack empty? -", stack.is_empty())