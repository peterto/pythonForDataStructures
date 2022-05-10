from stacks_and_queues.stack import Stack


class Queues2Stacks(object):

    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()

    def enqueue(self, element):
        self.instack.push(element)

    def dequeue(self):

        if not self.outstack.isEmpty():
            for i in range(len(self.instack) - 1):
                self.outstack.push(self.instack.pop())

        self.outstack.pop()

    def size(self) -> int:
        return self.instack.size() + self.outstack.size()

    def isEmpty(self) -> bool:
        return self.instack.isEmpty() and self.outstack.isEmpty()
