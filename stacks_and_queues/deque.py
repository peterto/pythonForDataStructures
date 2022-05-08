# unrestricted in adding and removing
# items can be added to front or back
class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def size(self) -> int:
        return len(self.items)

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)
        # item = self.items[0]
        #
        # for i in range(len(self.items) - 1):
        #     self.items[i] = self.items[i + 1]
        # return item


d = Deque()
print(d.isEmpty())
d.addRear(1)

print(d.size())
print(d.isEmpty())

d.addFront(True)
print(d.removeRear())

d.addRear(2)

print(d.removeRear())
