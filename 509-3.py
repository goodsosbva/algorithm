# 두 변수만 이용해 공간 절약
class Solution:
    def fib(self, N: int) -> int:
        x, y = 0, 1
        for i in range(0, N):
            x, y = y, x + y
        return x


n = int(input())
sol = Solution()
chk = sol.fib(n)
print(chk)