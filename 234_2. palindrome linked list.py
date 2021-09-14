# 연결 리스트 팬린드롬 판별 - 런너 방법
# 연결 리스트를 내가 직접 구현
# 팬린드롬 자체는 매우 쉬움 ( 234. palindrome linked list ) 와 연결 리스트 구조는 동일
import ctypes


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


def isPalindrome(head: Node) -> bool:
    rev = None
    slow = fast = head
    cnt = 0
    # 런너 이용
    while fast and fast.next:
        cnt += 1
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
        # print(slow.dat4a, slow.next.data)
    print("cnt", cnt)
    # 팬린드롬 판별
    # print(rev.data, slow.data)
    # print(ctypes.c_int.from_address(0x000001C98A231FD0).value)
    while rev and rev.data == slow.data:
        print(rev.data, slow.data)
        slow, rev = slow.next, rev.next
    return not rev


head = Node(1)
head.add(Node(2))
head.add(Node(3))
head.add(Node(2))
head.add(Node(1))

ans = isPalindrome(head)
print(ans)


