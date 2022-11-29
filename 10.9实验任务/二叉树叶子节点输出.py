import random


class queue:
    def __init__(self):
        self.lst = []
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        self.lst.append(item)
        self.tail = self.tail + 1

    def dequeue(self):
        try:
            item = self.lst[self.head]
            self.head = self.head + 1
            return item
        except self.head == self.tail:
            print("这个队列是空的")


class node:
    def __init__(self, num):
        self.key = num
        self.parent = None
        self.left = None
        self.right = None


class tree:
    def __init__(self):
        self.root = None

    def insert(self, Node: node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if Node.key < x.key:
                x = x.left
            else:
                x = x.right
        Node.parent = y
        if y is None:
            self.root = Node
        elif Node.key < y.key:
            y.left = Node
        else:
            y.right = Node


if __name__ == '__main__':
    times = 10
    Max = 20
    t = tree()
    d = []
    cnt = 0
    for i in range(times):
        digit = random.randint(0, Max)
        d.append(digit)
        n = node(digit)
        t.insert(n)
    q = queue()
    q.enqueue(t.root)
    result = []
    while not q.head == q.tail:
        tmp = 0
        lst = []
        n = q.dequeue()
        lst.append(n.key)
        if n.left is not None:
            q.enqueue(n.left)
        if n.right is not None:
            q.enqueue(n.right)
        if n.left is None and n.right is None:
            result.append(n)
    print(d)
    print("叶子节点为: ", end=" ")
    for i in result:
        print(i.key, end=" ")
