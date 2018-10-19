class ResizableStack:
    def __init__(self, initial_capacity):
        if initial_capacity < 1:
            raise ValueError("Capacity should be a positive number")

        self.size = 0
        self.capacity = initial_capacity
        self.array = [None] * initial_capacity

    def push(self, item):
        if self.size == self.capacity:          # current capacity is exceeded
            self._resize(self.capacity * 2)

        self.array[self.size] = item
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        self.size -= 1
        result = self.array[self.size]

        if self.capacity > 1 and self.size < self.capacity // 4:  # array is less than one quarter full
            self._resize(self.capacity // 2)

        return result

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.array[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def print(self):
        if self.size == 0:
            print("Stack is empty")

        for i in range(self.size - 1, -1, -1):
            print(self.array[i])