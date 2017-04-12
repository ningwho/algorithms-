from pythonds.basic.stack import Stack


class MyStack(object):
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
    def pop(self):
        item = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
    def peek(self):
        return self.data[len(self.data)-1]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size
s = MyStack()

print(s.size(4))
