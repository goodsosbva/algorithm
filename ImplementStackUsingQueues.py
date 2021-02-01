import collections


class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)

        for _ in range(len(self.q) - 1):
            print("for:", self.q)
            self.q.append((self.q.popleft()))

        print(self.q)

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


stackTest = MyStack()
stackTest.push(1)
stackTest.push(2)
stackTest.push(3)
stackTest.push(4)

#print(stackTest)
#print(len(stackTest))
#for i in stackTest:
#    print(i)


