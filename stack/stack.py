class BoundedArrayStack:
    def __init__(self, capacity):
        if capacity <= 0:
            raise Exception("Capacity must be greater than 0")

        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack is full")

        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        item = self.stack[self.top]
        self.top -= 1
        return item

    def __repr__(self):
        return f"BoundedArrayStack({self.stack[:self.top + 1]})"

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def size(self):
        return self.top + 1

    def clear(self):
        self.top = -1
        self.stack = [None] * self.capacity
