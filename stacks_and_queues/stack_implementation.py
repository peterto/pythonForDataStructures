# last in, first out, LIFO
class Stack:
    # size_of_stack = 0
    # items = []

    def __init__(self):
        self.items = []
        # self.size_of_stack = 0

    def push(self, item):
        self.items.append(item)
        # self.size_of_stack += 1

    def pop(self):
        self.items.pop()
        # self.size_of_stack -= 1

    def peek(self):
        # return self.items[self.size_of_stack - 1]
        return self.items[len(self.items) - 1]

    def isEmpty(self) -> bool:
        # if self.size_of_stack == 0:
        #     return True
        # return False
        return self.items == 0

    def size(self) -> int:
        # return self.size_of_stack
        return len(self.items)

# s = Stack()
#
# print(s.isEmpty())
# s.push(1)
# s.push("string")
# s.push(True)
# print(s.isEmpty())
# print(s.peek())
# s.pop()
# s.pop()
# s.pop()
# print(s.isEmpty())
