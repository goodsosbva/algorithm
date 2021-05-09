class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


a = abs(1000001000101)
sol = Solution()
chk = sol.hammingWeight(a)
print(chk)

