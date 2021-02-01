"""List = []
q: List = []

#head = [int(x) for x in (input()).split('->')]
#print(head)
head = LinkedList()

if not head:
    print('false')

node = head

while node is not None:
    q.append(node.val)
    print(q)
    node = node.next """


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List
#from Cython.Compiler.ExprNodes import ListNode


def isPalindrome(head: ListNode) -> bool:
    q: List = []

    if not head:
        return True
    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


#ListNodes = [1, 2, 3]
print(isPalindrome(ListNode()))
