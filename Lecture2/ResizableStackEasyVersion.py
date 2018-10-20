class ResizableStack:

    def __init__(self):
        self.list = []

    @property
    def size(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.list.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.list[len(self.list) - 1]

    def is_empty(self):
        return self.size == 0

    def print(self):
        if self.is_empty():
            print("Stack is empty")

        for i in range(len(self.list) - 1, -1, -1):
            print(self.list[i])



