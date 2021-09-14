# 234. palindrome linked list
from collections import deque
from typing import List

# Definition for singly-linked list.
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


# 팬린드롬 판별
def isPalindrome(head: Node) -> bool:
    """q: List = []"""
    q: deque = deque()

    if not head:
        return True

    node = head
    print(node)
    # 리스트 변환
    while node is not None:
        q.append(node.data)
        node = node.next

    print(q)
    # 팰린드롬 판별
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True



"""def __repr__(self):
    return '<%s.%s object at %s>' % (
        self.__class__.__module__,
        self.__class__.__name__,
        hex(id(self))
    )"""


# print(head.select(2))
head = Node(1)
head.add(Node(2))
head.add(Node(2))
head.add(Node(2))
head.add(Node(1))

ans = isPalindrome(head)
print(ans)
