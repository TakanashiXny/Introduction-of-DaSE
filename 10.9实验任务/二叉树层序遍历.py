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
    times = 30
    Max = 100
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
    cnt = 1
    layer = 1
    while not q.head == q.tail:
        print(f"第{layer}层结点: ", end=" ")
        tmp = 0
        for i in range(cnt):
            n = q.dequeue()
            print(n.key, end=" ")
            if n.left is not None:
                q.enqueue(n.left)
                tmp += 1
            if n.right is not None:
                q.enqueue(n.right)
                tmp += 1
            cnt = tmp
        layer += 1
        print()
