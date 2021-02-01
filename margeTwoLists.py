#from typing import List
#from Cython.Compiler.ExprNodes import ListNode
from pythonProject1.CodingInterView.panlindromeLinkedList import ListNode


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1

    if l1:
        l1.next = mergeTwoLists(l1.next, l2)

    return l1

