# 225. implement stack using queues
import collections


class mystack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)

        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return print(self.q[0])

    def empty(self):
        return print(len(self.q) == 0)

    # 네가 구현
    def ptr(self):
        print("[", end= " ")
        for i in range(len(self.q)):
            print(self.q[i], end=" ")
        print("]")


stack = mystack()
stack.push(1)
stack.ptr()
stack.push(2)
stack.ptr()
stack.top()
stack.pop()
stack.ptr()
stack.empty()
