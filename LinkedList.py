class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def add(self, node):
        if self.next is None:
            self.next = node
        else:
            n = self.next
            while True:
                if n.next is None:
                    n.next = node
                    break
                else:
                    n = n.next

    def select(self, idx):
        n = self.next
        for i in range(idx - 1):
            n = n.next
        return n.data

    def delete(self, idx):
        n = self.next
        for i in range(idx - 2):
            n = n.next
        t = n.next
        n.next = t.next
        del t

    def pop(self, idx):
        n = self.next
        for i in range(idx - 2):
            n = n.next
        t = n.next
        n.next = t.next
        return t

    def prt(self):
        print(self.data, end=" ")
        n = self.next
        while True:
            if n.next is None:
                print(n.data, end=" ")
                break
            else:
                print(n.data, end=" ")
                n = n.next
        print()

    def insert(self, idx, node):
        n = self.next
        for i in range(idx - 2):
            n = n.next
        t = n.next
        n.next = node
        node.next = t