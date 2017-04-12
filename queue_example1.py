from pythonds.basic.queue import Queue


class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return (self.items) == 0

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):

        return self.items.pop()

    def size(self):
        return len(self.items)



x = Queue()
x.enqueue(1)
x.enqueue(2)

print(x.dequeue())
