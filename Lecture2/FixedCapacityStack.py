class FixedCapacityStack:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity should be a positive number")

        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack is full")
        self.array[self.size] = item
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        self.size -= 1
        return self.array[self.size]

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.array[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def print(self):
        if self.size == 0:
            print("Stack is empty")

        for i in range(self.size - 1, -1, -1):
            print(self.array[i])




