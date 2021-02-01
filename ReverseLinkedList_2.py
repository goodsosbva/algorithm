head = [1, 2, 3, 4, 5]


node, prev = head, None

while node:
    next, node.next = node.next, prev
    prev, node = node, next

print(prev)
