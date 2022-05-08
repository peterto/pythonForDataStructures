# first in, first out, FIFO

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
        # item = self.items[0]
        #
        # for i in range(len(self.items) - 1):
        #     self.items[i] = self.items[i + 1]
        # return item

    def isEmpty(self) -> bool:
        return self.items == []

    def size(self) -> int:
        return len(self.items)


q = Queue()

print(q.isEmpty())
q.enqueue(1)
q.enqueue("string")
q.enqueue(True)
print(q.isEmpty())
# print(q.dequeue())
print(q.dequeue())
q.dequeue()
q.dequeue()
print(q.isEmpty())
