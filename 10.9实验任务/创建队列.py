class queue:
    def __init__(self):
        self.lst = []
        self.head = 0
        self.tail = 0

    def enqueue(self, num):
        self.lst[self.tail] = num
        self.tail = self.tail + 1

    def dequeue(self):
        try:
            item = self.lst[self.head]
            self.head = self.head + 1
        except self.head == self.tail:
            print("这个队列是空的")

    def get_head(self):
        try:
            item = self.lst[self.head]
            return item
        except self.head == self.tail:
            print("这个队列是空的")

    def get_tail(self):
        try:
            item = self.lst[self.tail-1]
            return item
        except self.head == self.tail:
            print("这个队列是空的")
