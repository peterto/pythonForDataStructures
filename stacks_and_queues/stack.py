class Stack:

    def __init__(self):
        self.items = []

    def pop(self):
        item = self.peek()
        if len(self.items) != 0:
            self.items.pop()
            return item

    def push(self, item):
        self.items.append(item)
        # self.size += 1
        # self.items[self.size] = item

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def size(self):
        return len(self.items)


