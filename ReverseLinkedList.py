#from Cython.Compiler.ExprNodes import ListNode
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
"""
    def append(self, node):
        if self.count == 0:
            self.head = node
            self.count = 1

        else:
            cur_node = self.head
            prev_node = None

            while cur_node != None and cur_node.data <= node.data:
                prev_node = cur_node
                cur_node = cur_node.next

            node.next = cur_node

            if prev_node = None:
                self.head = node

            else:
                prev_node.next = node
            self.count += 1
"""



def reverseList(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next. prev
        return reverse(next, node)

    return reverse(head)

listnodes = [1, 2, 3, 4, 5]
#print(reverseList(listnodes()))
k_reverse = reverseList()
for n in listnodes:
    node = ListNode(n)
    k_reverse(node)

print(listnodes)
