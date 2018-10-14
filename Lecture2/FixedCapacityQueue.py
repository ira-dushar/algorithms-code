class FixedCapacityQueue:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity should be a positive number")

        self.capacity = capacity
        self.size = 0
        self.head = 0    # index of the first element
        self.tail = -1   # index of the last element
        self.array = [None] * capacity

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Stack is full")

        self.tail = (self.tail + 1) % self.capacity
        self.array[self.tail] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        item = self.array[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1

        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def print(self):
        if self.size == 0:
            print("Stack is empty")

        index = self.head
        while 1:
            print(self.array[index])
            index = (index + 1) % self.capacity
            if index == (self.tail + 1) % self.capacity:
                break
